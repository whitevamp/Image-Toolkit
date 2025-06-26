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
from typing import Tuple, Dict

# Import from our core modules
from core.config_manager import ConfigManager
from core.image_utils import (
    get_random_name,
    get_simplified_ratio_string, # Still useful for other outputs/understanding
    ASPECT_RATIO_TOLERANCE,
)
# Import COMMON_RESOLUTIONS_DEFINITIONS from its new dedicated file
from core.resolution_definitions import COMMON_RESOLUTIONS_DEFINITIONS

class ImageProcessor:
    """
    Handles the processing (resizing, format conversion, renaming) of image files
    based on configuration settings.
    """
    def __init__(self, config_manager: ConfigManager):
        self.config_manager = config_manager
        self.input_dir = self.config_manager.get('Paths', 'input_directory')
        self.output_dir = self.config_manager.get('Paths', 'output_directory')
        self.output_extension = self.config_manager.get('ImageSettings', 'output_extension').lower()
        self.enable_random_rename = self.config_manager.getboolean('Renaming', 'enable_random_rename')
        self.names_file = self.config_manager.get('Paths', 'names_file')

        self.override_custom = self.config_manager.getboolean('ImageSettings', 'override_to_custom_resolution')
        self.custom_width = self.config_manager.getint('ImageSettings', 'custom_width')
        self.custom_height = self.config_manager.getint('ImageSettings', 'custom_height')

        # Define image extensions here as an instance variable
        self.image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

        fallback_goal_str = self.config_manager.get('ImageSettings', 'fallback_resolution_goal')
        self.fallback_target_width, self.fallback_target_height = self._get_fallback_resolution_dimensions(
            fallback_goal_str, self.custom_width, self.custom_height
        )

        # Pre-calculate decimal aspect ratios for quick lookup from definitions
        # This will store (decimal_aspect_ratio, original_ar_string_key) tuples
        self.ar_decimal_key_map: List[Tuple[float, str]] = []
        for ar_str_def in COMMON_RESOLUTIONS_DEFINITIONS:
            try:
                # Use split(':') to handle "X:Y" or float strings like "2.35:1"
                parts = ar_str_def.split(':')
                if len(parts) == 2:
                    w_def = float(parts[0])
                    h_def = float(parts[1])
                    if h_def != 0:
                        self.ar_decimal_key_map.append((w_def / h_def, ar_str_def))
                    else:
                        print(f"Warning: Aspect ratio '{ar_str_def}' has zero height. Skipping calculation.")
                else:
                    print(f"Warning: Could not parse aspect ratio key '{ar_str_def}' from COMMON_RESOLUTIONS_DEFINITIONS. Skipping.")
            except (ValueError, ZeroDivisionError) as e:
                print(f"Warning: Error processing aspect ratio '{ar_str_def}' from COMMON_RESOLUTIONS_DEFINITIONS: {e}. Skipping.")

        # Sort by decimal value for potentially faster lookup or consistency (optional)
        self.ar_decimal_key_map.sort()


        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
        print(f"Image Processor Initialized:")
        print(f"  Input Directory: {os.path.abspath(self.input_dir)}")
        print(f"  Output Directory: {os.path.abspath(self.output_dir)}")
        print(f"  Output Extension: {self.output_extension}")
        print(f"  Random Renaming Enabled: {self.enable_random_rename}")
        print(f"  Override to Custom Resolution Enabled: {self.override_custom}")
        if self.override_custom:
            print(f"    All images will be resized to: {self.custom_width}x{self.custom_height}")
        else:
            print(f"  Fallback Resolution Goal: {self.fallback_target_width}x{self.fallback_target_height} ({fallback_goal_str})")

    def _get_fallback_resolution_dimensions(self, size_str: str, custom_width: int, custom_height: int) -> Tuple[int, int]:
        """Determines fallback target resolution dimensions based on configuration (for '4k', '1080p', 'custom')."""
        resolutions = {
            '1080p': (1920, 1080),
            '1440p': (2560, 1440),
            '4k': (3840, 2160)
        }
        if size_str.lower() == 'custom':
            if custom_width and custom_height:
                return (custom_width, custom_height)
            else:
                print("Warning: 'custom' fallback_resolution_goal selected but custom_width/height not set. Defaulting to 1080p.")
                return resolutions['1080p']
        elif size_str.lower() in resolutions:
            return resolutions[size_str.lower()]
        else:
            print(f"Warning: Invalid fallback_resolution_goal '{size_str}'. Defaulting to 1080p.")
            return resolutions['1080p']

    def process_images(self) -> int:
        """
        Scans, processes (resizes, converts, renames), and saves images.
        Returns the count of successfully processed images.
        """
        print(f"\nStarting image processing in: {os.path.abspath(self.input_dir)}")
        processed_count = 0

        # Get all aspect ratio specific targets from config
        ar_specific_targets = {}
        image_settings_dict = self.config_manager.get_section_as_dict('ImageSettings')
        for key, value in image_settings_dict.items():
            if key.startswith('target_resolution_'):
                # Convert 'target_resolution_X_Y' back to 'X:Y' or 'X.Y:Z'
                # Replace the first underscore for X_Y, then any subsequent for X.Y_Z
                ar_str_key = key.replace('target_resolution_', '', 1).replace('_', ':')
                ar_specific_targets[ar_str_key] = value

        for root, _, files in os.walk(self.input_dir):
            for filename in files:
                if filename.lower().endswith(self.image_extensions): # Use self.image_extensions
                    filepath = os.path.join(root, filename)
                    try:
                        with Image.open(filepath) as img:
                            print(f"\nProcessing: {filename} (Original: {img.width}x{img.height})")

                            target_width, target_height = 0, 0
                            chosen_method = "unknown"

                            if self.override_custom:
                                # If override is true, always use custom dimensions
                                target_width, target_height = self.custom_width, self.custom_height
                                chosen_method = "Custom Override (Direct Resize)"
                            else:
                                current_img_aspect = img.width / img.height if img.height != 0 else float('inf')
                                matched_ar_key = None

                                # Find the closest matching aspect ratio key based on decimal value
                                min_diff = float('inf')
                                for def_ar_decimal, def_ar_key in self.ar_decimal_key_map:
                                    diff = abs(current_img_aspect - def_ar_decimal)
                                    if diff < min_diff and diff <= ASPECT_RATIO_TOLERANCE:
                                        min_diff = diff
                                        matched_ar_key = def_ar_key # This is the string key like '16:9' or '2.35:1'

                                if matched_ar_key:
                                    # Found a matching aspect ratio in definitions
                                    # Now, check if there's a specific target level for it in config.ini
                                    target_level_str = ar_specific_targets.get(matched_ar_key) # Get level from config

                                    if target_level_str and matched_ar_key in COMMON_RESOLUTIONS_DEFINITIONS and target_level_str in COMMON_RESOLUTIONS_DEFINITIONS[matched_ar_key]:
                                        # Use the dimensions from the COMMON_RESOLUTIONS_DEFINITIONS
                                        target_width, target_height = COMMON_RESOLUTIONS_DEFINITIONS[matched_ar_key][target_level_str]
                                        chosen_method = f"Aspect Ratio Match ({matched_ar_key}) to {target_level_str}"
                                    else:
                                        # No specific target level set in config for this aspect ratio, or level not found in definitions.
                                        # Fall back to direct resize.
                                        print(f"  Warning: No specific target level ('{target_level_str}') found in definitions for AR '{matched_ar_key}'. Falling back to general goal.")
                                        target_width, target_height = self.fallback_target_width, self.fallback_target_height
                                        chosen_method = "Fallback (Direct Resize)"
                                else:
                                    # No close aspect ratio match found in predefined ARs at all, use fallback
                                    print(f"  No close aspect ratio match found for original ({img.width}x{img.height}, AR {current_img_aspect:.2f}). Using fallback.")
                                    target_width, target_height = self.fallback_target_width, self.fallback_target_height
                                    chosen_method = "Fallback (Direct Resize)"

                            # Perform the resize
                            print(f"  Chosen Method: {chosen_method}. Resizing to: {target_width}x{target_height}")
                            img = img.resize((target_width, target_height), Image.LANCZOS)

                            # Determine output filename and path
                            base_name = os.path.splitext(filename)[0]
                            if self.enable_random_rename:
                                new_name = get_random_name(self.names_file) + f"_{processed_count:04d}" # Add a counter for uniqueness
                            else:
                                new_name = base_name

                            if self.output_extension == 'original':
                                final_ext = os.path.splitext(filename)[1].lower()
                                if final_ext == '.jpeg':
                                    final_ext = '.jpg'
                                output_filepath = os.path.join(self.output_dir, f"{new_name}{final_ext}")
                            else:
                                output_filepath = os.path.join(self.output_dir, f"{new_name}.{self.output_extension}")

                            # Save the image
                            save_format = self.output_extension.upper() if self.output_extension != 'original' else img.format
                            if save_format == 'JPG':
                                save_format = 'JPEG'
                            elif save_format == 'TIF':
                                save_format = 'TIFF'

                            # Handle potential alpha channel issues (e.g., PNG to JPG)
                            if save_format == 'JPEG' and img.mode in ('RGBA', 'P'):
                                img = img.convert('RGB')
                            elif save_format == 'BMP' and img.mode == 'RGBA':
                                img = img.convert('RGB')

                            img.save(output_filepath, format=save_format)
                            print(f"  Saved: {os.path.basename(output_filepath)}")
                            processed_count += 1

                    except Exception as e:
                        print(f"Error processing {filename}: {e}")

        print(f"\nImage processing complete. Successfully processed {processed_count} images.")
        return processed_count
