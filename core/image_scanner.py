# Copyright (C) 2025 whitevamp
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from PIL import Image
from typing import Dict, Tuple, Set, List
import math
import ast # To safely parse Python dictionary strings from a file
import re  # For regular expressions to find the dictionary block

# Import from our core modules
from core.config_manager import ConfigManager
from core.image_utils import (
    get_simplified_ratio_string,
    is_portrait_ratio,
    ASPECT_RATIO_TOLERANCE,
)
# COMMON_RESOLUTIONS_DEFINITIONS is imported dynamically when needed for merging/template generation
# within specific functions, to ensure we always read the latest version from the file.
# It is still imported statically in image_processor and app_gui for their dropdowns/logic.


class ImageScanner:
    """
    Handles recursive directory scanning for images, extracting dimensions,
    and generating various reports and config templates.
    """
    def __init__(self, config_manager: ConfigManager):
        self.config_manager = config_manager
        self.input_dir = self.config_manager.get('Paths', 'input_directory')
        self.scanner_output_dir = self.config_manager.get('Paths', 'scanner_output_directory')
        self.enable_exclusion = self.config_manager.getboolean('Scanner', 'enable_exclusion_reference', fallback=False)
        self.exclusion_file_path = self.config_manager.get('Paths', 'exclusion_reference_file')
        self.master_definitions_file = self.config_manager.get('Paths', 'master_definitions_file')

        self.merge_to_master_definitions = self.config_manager.getboolean('Scanner', 'merge_to_master_definitions', fallback=False)

        # Ensure scanner output directory exists
        os.makedirs(self.scanner_output_dir, exist_ok=True)

        self.image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

        # COMMON_RESOLUTIONS_DEFINITIONS from the file is loaded only when needed for merging/template generation
        # Not pre-calculated here globally to ensure we read the latest for merge operations.
        # This will be passed to helper functions.

    def _load_excluded_sizes(self) -> Set[Tuple[int, int]]:
        """Loads image dimensions from a reference file to exclude them."""
        excluded_sizes = set()
        file_path = self.exclusion_file_path
        if not os.path.exists(file_path):
            print(f"Warning: Exclusion reference file '{file_path}' not found. No sizes will be excluded.")
            return excluded_sizes

        try:
            with open(file_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'): # Skip empty lines and comments
                        continue
                    try:
                        parts = line.split('x')
                        if len(parts) == 2:
                            width = int(parts[0])
                            height = int(parts[1])
                            excluded_sizes.add((width, height))
                        else:
                            print(f"Warning: Invalid format in exclusion file: '{line}'. Expected 'WIDTHxHEIGHT'.")
                    except ValueError:
                        print(f"Warning: Could not parse dimensions in exclusion file: '{line}'. Skipping.")
        except IOError as e:
            print(f"Error reading exclusion file '{file_path}': {e}")
        return excluded_sizes

    def _write_found_dimensions_file(self, found_dimensions: Dict[str, Dict[str, Tuple[int, int]]]):
        """Writes the collected dimensions to the output file in Python dictionary format."""
        output_path = os.path.join(self.scanner_output_dir, "found_image_dimensions.txt")
        print(f"\nWriting found dimensions report to: {os.path.abspath(output_path)}")

        with open(output_path, 'w') as f:
            f.write("COMMON_RESOLUTIONS: Dict[str, Dict[str, Tuple[int, int]]] = {\n")

            # Sort aspect ratios for consistent output order
            sorted_aspect_ratios = sorted(found_dimensions.keys(),
                                          key=lambda x: (float(x.split(':')[0])/float(x.split(':')[1])
                                                         if float(x.split(':')[1]) != 0 else float('inf')))

            for ar_str in sorted_aspect_ratios:
                f.write(f"    '{ar_str}': {{\n")

                # Sort resolutions within each aspect ratio by width
                sorted_levels = sorted(found_dimensions[ar_str].items(), key=lambda item: item[1][0])

                for level_name, dimensions in sorted_levels:
                    f.write(f"        '{level_name}': {dimensions},\n")
                f.write("    },\n")
            f.write("}\n")
        print(f"Found dimensions report written to: {os.path.abspath(output_path)}")

    def _write_config_template_file(self, common_res_definitions_ref: Dict[str, Dict[str, Tuple[int, int]]]):
        """
        Generates a 'for_config.txt' file with aspect ratio specific target resolution settings
        for ALL predefined aspect ratios in COMMON_RESOLUTIONS_DEFINITIONS.
        """
        output_path = os.path.join(self.scanner_output_dir, "for_config.txt")
        print(f"\nGenerating full config template to: {os.path.abspath(output_path)}")

        # Sort aspect ratios for consistent output order (by decimal value)
        sorted_ar_keys = sorted(common_res_definitions_ref.keys(), # Use the passed dictionary
                                key=lambda x: (float(x.split(':')[0]) / float(x.split(':')[1])
                                               if float(x.split(':')[1]) != 0 else float('inf')))

        with open(output_path, 'w') as f:
            f.write("# === Aspect Ratio Specific Target Resolutions ===\n")
            f.write("# For each aspect ratio group, specify the desired resolution level from the options below.\n")
            f.write("# This section can be copied into the [ImageSettings] section of your main config.ini.\n\n")

            for ar_str in sorted_ar_keys:
                levels = common_res_definitions_ref[ar_str]
                if not levels: # Skip if no levels defined for this aspect ratio
                    continue

                # Get sorted list of level names for the 'Options' comment
                sorted_level_names = sorted(levels.keys())
                options_comment = f"; Options: {', '.join(sorted_level_names)}"
                f.write(options_comment + "\n")

                # Determine a sensible default level for the config template
                default_level = ""
                if "4K UHD" in levels:
                    default_level = "4K UHD"
                elif "FHD Portrait" in levels:
                    default_level = "FHD Portrait"
                elif "Super Large Portrait" in levels:
                    default_level = "Super Large Portrait"
                elif "Large Portrait" in levels:
                    default_level = "Large Portrait"
                elif "Medium Portrait" in levels:
                    default_level = "Medium Portrait"
                elif "Common AI Gen Portrait" in levels:
                    default_level = "Common AI Gen Portrait"
                elif "UW-QHD" in levels:
                    default_level = "UW-QHD"
                elif "Square" in levels:
                    default_level = "Square"
                elif sorted_level_names:
                    default_level = sorted_level_names[0] # Fallback to the first available level

                # Construct the config key (e.g., target_resolution_16_9)
                config_key = f"target_resolution_{ar_str.replace(':', '_').replace('.', '_')}" # Replaced '.' with '_'
                f.write(f"{config_key} = {default_level}\n\n")

        print(f"Full config template written to: {os.path.abspath(output_path)}")

    def _write_custom_config_template_file(self, newly_found_aspect_ratios: Dict[str, Tuple[int, int]]):
        """
        Generates a 'for_config_custom.txt' file for newly discovered aspect ratios.
        """
        output_path = os.path.join(self.scanner_output_dir, "for_config_custom.txt")
        print(f"\nGenerating custom config template to: {os.path.abspath(output_path)}")

        # Sort aspect ratios for consistent output order
        sorted_ar_keys = sorted(newly_found_aspect_ratios.keys(),
                                key=lambda x: (float(x.split(':')[0]) / float(x.split(':')[1])
                                               if float(x.split(':')[1]) != 0 else float('inf')))

        with open(output_path, 'w') as f:
            f.write("# === Newly Discovered Aspect Ratio Target Resolutions ===\n")
            f.write("# These aspect ratios were found in your scanned images but are not predefined in the script.\n")
            f.write("# Copy these entries into the [ImageSettings] section of your main config.ini if desired.\n\n")

            for ar_str in sorted_ar_keys:
                # Determine if it's portrait or landscape for the default level name
                orientation_tag = "Portrait" if is_portrait_ratio(ar_str) else "Landscape"
                default_level = f"Custom {orientation_tag}" # Default level name for custom ARs

                options_comment = f"; Options: {default_level}" # Only one option for these dynamically found ones
                f.write(options_comment + "\n")

                config_key = f"target_resolution_{ar_str.replace(':', '_').replace('.', '_')}" # Replaced '.' with '_'
                f.write(f"{config_key} = {default_level}\n\n")

        print(f"Custom config template written to: {os.path.abspath(output_path)}")


    def _write_matched_missing_file(self, matched_missing_dims: Dict[str, List[Tuple[int, int]]]):
        """
        Generates a 'matched_missing.txt' file for dimensions matching a known aspect ratio
        but not explicitly defined as a level within that ratio. (Plain text list)
        """
        output_path = os.path.join(self.scanner_output_dir, "matched_missing.txt")
        print(f"\nGenerating matched missing dimensions report (plain text) to: {os.path.abspath(output_path)}")

        # Sort aspect ratios for consistent output
        sorted_ar_keys = sorted(matched_missing_dims.keys(),
                                key=lambda x: (float(x.split(':')[0]) / float(x.split(':')[1])
                                               if float(x.split(':')[1]) != 0 else float('inf')))

        with open(output_path, 'w') as f:
            f.write("# === Dimensions Matching Known Aspect Ratios But Not Explicitly Defined (Plain Text) ===\n")
            f.write("# These images have an aspect ratio that is listed in COMMON_RESOLUTIONS_DEFINITIONS,\n")
            f.write("# but their exact WIDTHxHEIGHT is not a named level within that aspect ratio group.\n")
            f.write("# Consider adding these as new levels to COMMON_RESOLUTIONS_DEFINITIONS if they are common.\n\n")

            for ar_str in sorted_ar_keys:
                f.write(f"Aspect Ratio: {ar_str}\n")
                # Sort dimensions within each aspect ratio
                sorted_dims = sorted(matched_missing_dims[ar_str])
                for w, h in sorted_dims:
                    f.write(f"  - {w}x{h}\n")
                f.write("\n")

        print(f"Matched missing dimensions report (plain text) written to: {os.path.abspath(output_path)}")

    def _load_definitions_from_file(self, file_path: str) -> Tuple[str, Dict[str, Dict[str, Tuple[int, int]]], str]:
        """
        Reads the content of a Python file, extracts the COMMON_RESOLUTIONS_DEFINITIONS dictionary,
        and returns the content before, the parsed dictionary, and content after the dictionary.
        """
        pre_dict_content = []
        dict_lines = []
        post_dict_content = []
        in_dict_block = False
        dict_var_found = False

        if not os.path.exists(file_path):
            # If the file doesn't exist, return empty strings and an empty dictionary
            # This is handled in main.py by creating a default file
            return "", {}, ""

        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Regex to find the start of the dictionary assignment
        # It's flexible for common whitespace and variable name variations
        # Also capture the actual variable name, in case it changes (though we expect COMMON_RESOLUTIONS_DEFINITIONS)
        start_pattern = re.compile(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*Dict\[str,\s*Dict\[str,\s*Tuple\[int,\s*int\]\]\]\s*=\s*({.*)$')

        i = 0
        while i < len(lines):
            line = lines[i]
            if not in_dict_block:
                match = start_pattern.match(line)
                if match:
                    dict_var_name = match.group(1)
                    dict_start_line_content = match.group(2) # E.g., "{ '16:9': { ... }"

                    if dict_var_name == "COMMON_RESOLUTIONS_DEFINITIONS": # Only target this specific variable
                        pre_dict_content.append(line.split(dict_start_line_content)[0]) # Keep everything before the dictionary start
                        dict_lines.append(dict_start_line_content) # Add the part of the line that is the dictionary start
                        in_dict_block = True
                        dict_var_found = True
                    else:
                        pre_dict_content.append(line) # Not our target variable, treat as pre-content
                else:
                    pre_dict_content.append(line)
            else: # in_dict_block is True
                dict_lines.append(line)
                # Check for the matching closing brace, accounting for nested braces
                # A simple count of '{' and '}' might not be perfect for all complex Python code,
                # but should work for a dictionary definition.
                if line.strip().startswith('}') and sum(l.count('{') for l in dict_lines) == sum(l.count('}') for l in dict_lines):
                    in_dict_block = False
                    # The remaining lines are post_dict_content
                    post_dict_content = lines[i+1:]
                    break # Exit loop after finding the dictionary and its context
            i += 1

        # If the dictionary wasn't found or was malformed, dict_lines might be empty/incomplete
        extracted_dict_str = "".join(dict_lines).strip()
        parsed_dict = {}

        if extracted_dict_str and dict_var_found:
            # Ensure it's a complete dictionary string before ast.literal_eval
            if not extracted_dict_str.startswith('{'):
                extracted_dict_str = '{' + extracted_dict_str
            if not extracted_dict_str.endswith('}'):
                # Attempt to fix if missing closing brace (for simple cases)
                extracted_dict_str += '}' * (extracted_dict_str.count('{') - extracted_dict_str.count('}'))

            try:
                # Use ast.literal_eval for safe parsing of Python literal structures
                parsed_dict = ast.literal_eval(extracted_dict_str)
                if not isinstance(parsed_dict, dict):
                    raise ValueError("Parsed content is not a dictionary.")
            except (ValueError, SyntaxError) as e:
                print(f"Error: Could not parse COMMON_RESOLUTIONS_DEFINITIONS from '{file_path}': {e}")
                print(f"Content attempted to parse: \n{extracted_dict_str[:500]}...") # Print first 500 chars for debug
                print("Please ensure the dictionary structure in the file is valid Python syntax.")
                parsed_dict = {} # Fallback to empty dict on parse error

        return "".join(pre_dict_content), parsed_dict, "".join(post_dict_content)

    def _write_definitions_to_file(self,
                                   data: Dict[str, Dict[str, Tuple[int, int]]],
                                   file_path: str,
                                   pre_content: str,
                                   post_content: str,
                                   var_name: str = "COMMON_RESOLUTIONS_DEFINITIONS"):
        """
        Writes a Python dictionary to a file in a formatted way,
        preserving pre-existing content around the dictionary definition.
        """
        print(f"\nWriting updated definitions to: {os.path.abspath(file_path)}")

        # Format the dictionary into a string
        dict_str_buffer = []
        # Reconstruct the variable assignment line
        dict_str_buffer.append(f"{var_name}: Dict[str, Dict[str, Tuple[int, int]]] = {{\n")

        sorted_ar_keys = sorted(data.keys(),
                                key=lambda x: (float(x.split(':')[0])/float(x.split(':')[1])
                                               if float(x.split(':')[1]) != 0 else float('inf')))

        for ar_str in sorted_ar_keys:
            dict_str_buffer.append(f"    '{ar_str}': {{\n")

            # Sort resolutions within each aspect ratio by width for consistent output
            sorted_levels = sorted(data[ar_str].items(), key=lambda item: item[1][0])

            for level_name, dimensions in sorted_levels:
                dict_str_buffer.append(f"        '{level_name}': {dimensions},\n")
            dict_str_buffer.append("    },\n")
        dict_str_buffer.append("}\n") # Closing brace for the dictionary itself

        # Reconstruct the full file content: pre-content + formatted dictionary + post-content
        full_content = pre_content + "".join(dict_str_buffer) + post_content

        with open(file_path, 'w') as f:
            f.write(full_content)
        print(f"Updated definitions written to: {os.path.abspath(file_path)}")


    def scan_images(self):
        """Main function to scan images, collect dimensions, and generate reports."""
        print(f"Starting image scan in: {os.path.abspath(self.input_dir)}")

        excluded_sizes = set()
        if self.enable_exclusion:
            excluded_sizes = self._load_excluded_sizes()
            print(f"Exclusion enabled. Will skip {len(excluded_sizes)} sizes from '{os.path.abspath(self.exclusion_file_path)}'.")

        found_dimensions_for_output: Dict[str, Dict[str, Tuple[int, int]]] = {} # For found_image_dimensions.txt
        newly_found_aspect_ratios: Dict[str, Tuple[int, int]] = {} # For for_config_custom.txt
        matched_missing_dimensions_for_reports: Dict[str, List[Tuple[int, int]]] = {} # For matched_missing.txt (both formats)

        # Load initial definitions and their context from the master file
        # This will be used for comparison during scan and for later rewriting
        pre_master_content, initial_master_defs, post_master_content = self._load_definitions_from_file(self.master_definitions_file)

        # Pre-calculate decimal aspect ratios for quick lookup using the freshly loaded definitions
        # This will store (decimal_aspect_ratio, original_ar_string_key) tuples
        ar_decimal_key_map_for_scan: List[Tuple[float, str]] = []
        for ar_str_def in initial_master_defs:
            try:
                # Use split(':') to handle "X:Y" or float strings like "2.35:1"
                parts = ar_str_def.split(':')
                if len(parts) == 2:
                    w_def = float(parts[0])
                    h_def = float(parts[1])
                    if h_def != 0:
                        ar_decimal_key_map_for_scan.append((w_def / h_def, ar_str_def))
                    else:
                        print(f"Warning: Aspect ratio '{ar_str_def}' has zero height. Skipping calculation.")
                else:
                    print(f"Warning: Could not parse aspect ratio key '{ar_str_def}' from initial master definitions. Skipping.")
            except (ValueError, ZeroDivisionError) as e:
                print(f"Warning: Error processing aspect ratio '{ar_str_def}' from initial master definitions: {e}. Skipping.")

        ar_decimal_key_map_for_scan.sort() # Sort for consistency/potential optimization


        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp') # Common image formats

        scanned_count = 0
        skipped_count = 0

        for root, _, files in os.walk(self.input_dir):
            for filename in files:
                if filename.lower().endswith(self.image_extensions):
                    filepath = os.path.join(root, filename)
                    try:
                        with Image.open(filepath) as img:
                            img_width, img_height = img.size
                            current_dimensions = (img_width, img_height)

                            if self.enable_exclusion and current_dimensions in excluded_sizes:
                                print(f"Skipping {filename}: Size {img_width}x{img_height} is in exclusion list.")
                                skipped_count += 1
                                continue

                            scanned_count += 1

                            current_decimal_ar = img_width / img_height if img_height != 0 else float('inf')
                            # The simplified string is still useful for initial reporting of found AR
                            aspect_ratio_str_found_simplified = get_simplified_ratio_string(img_width, img_height)

                            matched_ar_key_from_definitions = None # This will be the key like '16:9' or '2.35:1'
                            is_exact_dim_known_in_definitions = False

                            # Find the closest matching aspect ratio key from initial_master_defs based on decimal value
                            min_diff = float('inf')
                            for def_ar_decimal, def_ar_key in ar_decimal_key_map_for_scan:
                                diff = abs(current_decimal_ar - def_ar_decimal)
                                if diff < min_diff and diff <= ASPECT_RATIO_TOLERANCE:
                                    min_diff = diff
                                    matched_ar_key_from_definitions = def_ar_key

                            level_name_for_found_output = "" # Default, will be set below


                            if matched_ar_key_from_definitions:
                                # An aspect ratio from our definitions matched numerically
                                # Now check if the exact dimension is known within this matched aspect ratio's levels
                                if matched_ar_key_from_definitions in initial_master_defs:
                                    for named_level, named_dim in initial_master_defs[matched_ar_key_from_definitions].items():
                                        if named_dim == current_dimensions:
                                            is_exact_dim_known_in_definitions = True
                                            level_name_for_found_output = named_level # Use the exact named level if found
                                            break

                                if not is_exact_dim_known_in_definitions:
                                    # Aspect ratio is known, but this specific dimension isn't defined
                                    if matched_ar_key_from_definitions not in matched_missing_dimensions_for_reports:
                                        matched_missing_dimensions_for_reports[matched_ar_key_from_definitions] = []
                                    if current_dimensions not in matched_missing_dimensions_for_reports[matched_ar_key_from_definitions]: # Avoid duplicates within list
                                        matched_missing_dimensions_for_reports[matched_ar_key_from_definitions].append(current_dimensions)

                                    orientation_tag = "Portrait" if is_portrait_ratio(matched_ar_key_from_definitions) else "Landscape"
                                    # For the found_image_dimensions.txt, use the simplified string from the image if no exact match
                                    level_name_for_found_output = f"Custom {orientation_tag} (Matches {matched_ar_key_from_definitions})"
                                    print(f"Found {filename}: {img_width}x{img_height} (AR {current_decimal_ar:.2f} matches {matched_ar_key_from_definitions}) - KNOWN AR, NEW DIMENSION")
                                else:
                                    # Aspect ratio and exact dimension are known and matched a predefined named level
                                    print(f"Found {filename}: {img_width}x{img_height} (AR {current_decimal_ar:.2f} matches {matched_ar_key_from_definitions}) - KNOWN AR & DEFINED DIM ({level_name_for_found_output})")
                            else:
                                # No close aspect ratio match found in predefined ARs at all, this is a completely new AR
                                if aspect_ratio_str_found_simplified not in newly_found_aspect_ratios:
                                    newly_found_aspect_ratios[aspect_ratio_str_found_simplified] = current_dimensions # Store just one example dimension

                                orientation_tag = "Portrait" if is_portrait_ratio(aspect_ratio_str_found_simplified) else "Landscape"
                                level_name_for_found_output = f"Custom {orientation_tag} (New AR {aspect_ratio_str_found_simplified})"
                                print(f"Found {filename}: {img_width}x{img_height} ({aspect_ratio_str_found_simplified}) - COMPLETELY NEW ASPECT RATIO")

                            # Add to the found_dimensions_for_output dictionary (for found_image_dimensions.txt)
                            # Use the simplified string as the key for found_dimensions_for_output for clarity in that report
                            if aspect_ratio_str_found_simplified not in found_dimensions_for_output:
                                found_dimensions_for_output[aspect_ratio_str_found_simplified] = {}

                            # If a named level was found, use that. Otherwise, use a descriptive custom name.
                            if level_name_for_found_output: # if already set by an exact match or new AR
                                found_dimensions_for_output[aspect_ratio_str_found_simplified][level_name_for_found_output] = current_dimensions
                            else: # This path should be hit if AR is known and exact dim is known
                                # Fallback, should ideally be covered by is_exact_dim_known_in_definitions above
                                found_dimensions_for_output[aspect_ratio_str_found_simplified][f"Known Level ({img_width}x{img_height})"] = current_dimensions

                    except Exception as e:
                        print(f"Error processing {filename}: {e}")

        print(f"\nScan complete. Scanned {scanned_count} unique image dimensions (skipped {skipped_count} due to exclusion).")

        # --- Generate all reports ---
        self._write_found_dimensions_file(found_dimensions_for_output)

        # For writing config templates, we'll use the initial master definitions loaded at the start of scan_images.
        self._write_config_template_file(initial_master_defs) # Generates for_config.txt (predefined ARs)

        self._write_custom_config_template_file(newly_found_aspect_ratios) # Generates for_config_custom.txt (newly found ARs)
        self._write_matched_missing_file(matched_missing_dimensions_for_reports) # Generates matched_missing.txt (plain text)

        # Prepare data for matched_missing_formatted_data
        matched_missing_formatted_data: Dict[str, Dict[str, Tuple[int, int]]] = {}
        for ar_str, dims_list in matched_missing_dimensions_for_reports.items():
            if ar_str not in matched_missing_formatted_data:
                matched_missing_formatted_data[ar_str] = {}
            for w, h in dims_list:
                # Ensure unique level names if multiple custom dimensions share the same AR
                orientation_tag = "Portrait" if is_portrait_ratio(ar_str) else "Landscape"
                level_name = f"Custom {orientation_tag} ({w}x{h})"
                matched_missing_formatted_data[ar_str][level_name] = (w, h)

        # Write matched_missing_formatted.txt (formatted dict for direct inclusion)
        self._write_definitions_to_file(matched_missing_formatted_data,
                                        os.path.join(self.scanner_output_dir, "matched_missing_formatted.txt"),
                                        pre_content="", # No pre/post content for this report file
                                        post_content="",
                                        var_name="COMMON_RESOLUTIONS_FOR_ADDITION")

        # --- Perform Merge if enabled ---
        if self.merge_to_master_definitions:
            self._merge_definitions_into_master_file(matched_missing_formatted_data)

    def _merge_definitions_into_master_file(self, new_definitions: Dict[str, Dict[str, Tuple[int, int]]]):
        """
        Merges new definitions (e.g., from scanned missing dimensions) into the master_definitions_file.
        This function reads the file, merges in memory, and rewrites the file content.
        """
        master_file_path = self.config_manager.get('Paths', 'master_definitions_file')
        print(f"\nAttempting to merge new definitions into master file: {os.path.abspath(master_file_path)}")

        # Load existing master definitions, preserving surrounding content
        pre_content, existing_definitions, post_content = self._load_definitions_from_file(master_file_path)

        # Merge new definitions into existing ones
        merged_definitions = existing_definitions.copy()
        newly_merged_count = 0

        for ar_str, new_levels in new_definitions.items():
            if ar_str not in merged_definitions:
                merged_definitions[ar_str] = {}
                print(f"  Added new Aspect Ratio: '{ar_str}'")

            for level_name, dimensions in new_levels.items():
                # Check if the exact (width, height) pair already exists for this AR
                if dimensions not in merged_definitions[ar_str].values():
                    merged_definitions[ar_str][level_name] = dimensions
                    print(f"  Merged new definition: '{ar_str}': {{'{level_name}': {dimensions}}}")
                    newly_merged_count += 1

        if newly_merged_count > 0:
            # Write the merged definitions back to the master file
            self._write_definitions_to_file(merged_definitions, master_file_path, pre_content, post_content)
            print(f"Merge operation complete. {newly_merged_count} new definitions added to master file: {os.path.abspath(master_file_path)}")
        else:
            print(f"No new definitions to merge into master file: {os.path.abspath(master_file_path)}")

