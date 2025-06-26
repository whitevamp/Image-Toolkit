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
import imagehash
from typing import Dict, List, Tuple, Optional
import shutil # For file operations (move/copy)

# Import ConfigManager for path and setting retrieval
from core.config_manager import ConfigManager

class DuplicateFinder:
    """
    Detects duplicate and near-duplicate images using perceptual hashing,
    and provides options to move, copy, or delete them.
    """
    def __init__(self, config_manager: ConfigManager):
        self.config_manager = config_manager
        self.input_dir = self.config_manager.get('Paths', 'input_directory')
        self.hashes_cache_file = self.config_manager.get('Paths', 'image_hashes_cache_file')
        self.duplicate_report_file = self.config_manager.get('Paths', 'duplicate_report_file')
        self.duplicate_action_directory = self.config_manager.get('Paths', 'duplicate_action_directory')

        self.hash_type = self.config_manager.get('DuplicateFinder', 'hash_type', fallback='dhash').lower()
        self.hash_threshold = self.config_manager.getint('DuplicateFinder', 'hash_threshold', fallback=8)
        self.rebuild_hash_cache = self.config_manager.getboolean('DuplicateFinder', 'rebuild_hash_cache', fallback=False)
        self.duplicate_action_type = self.config_manager.get('DuplicateFinder', 'duplicate_action_type', fallback='none').lower()
        self.enable_duplicate_actions = self.config_manager.getboolean('DuplicateFinder', 'enable_duplicate_actions', fallback=False)

        # Supported hash types and their corresponding hash functions from imagehash
        self._hash_functions = {
            'ahash': imagehash.average_hash,
            'phash': imagehash.phash,
            'dhash': imagehash.dhash,
            'whash': imagehash.whash,
            # Add other hash types if needed, e.g., 'crop_resistant_hash': imagehash.crop_resistant_hash
        }
        self.image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

        # Ensure necessary directories exist
        os.makedirs(os.path.dirname(self.hashes_cache_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.duplicate_report_file), exist_ok=True)
        os.makedirs(self.duplicate_action_directory, exist_ok=True) # Ensure action directory exists

        print(f"Duplicate Finder Initialized:")
        print(f"  Input Directory: {os.path.abspath(self.input_dir)}")
        print(f"  Hash Type: {self.hash_type}")
        print(f"  Hash Threshold: {self.hash_threshold}")
        print(f"  Rebuild Cache: {self.rebuild_hash_cache}")
        print(f"  Cache File: {os.path.abspath(self.hashes_cache_file)}")
        print(f"  Report File: {os.path.abspath(self.duplicate_report_file)}")
        print(f"  Action Directory: {os.path.abspath(self.duplicate_action_directory)}")
        print(f"  Duplicate Action Type: {self.duplicate_action_type}")
        print(f"  Enable Duplicate Actions: {self.enable_duplicate_actions}")


    def _get_hasher(self):
        """Returns the selected hash function."""
        hasher = self._hash_functions.get(self.hash_type)
        if hasher is None:
            print(f"Warning: Unknown hash type '{self.hash_type}'. Defaulting to 'dhash'.")
            return imagehash.dhash
        return hasher

    def _load_hashes_from_cache(self) -> Dict[str, imagehash.ImageHash]:
        """Loads image hashes from the cache file."""
        cached_hashes = {}
        if os.path.exists(self.hashes_cache_file) and not self.rebuild_hash_cache:
            print(f"Loading hashes from cache: {os.path.abspath(self.hashes_cache_file)}")
            try:
                with open(self.hashes_cache_file, 'r') as f:
                    for line in f:
                        parts = line.strip().split(',', 1)
                        if len(parts) == 2:
                            filepath, hash_str = parts
                            try:
                                cached_hashes[filepath] = imagehash.hex_to_hash(hash_str)
                            except ValueError as ve:
                                print(f"Warning: Could not parse hash '{hash_str}' for file '{filepath}': {ve}. Skipping entry.")
                        else:
                            print(f"Warning: Invalid line in cache file: '{line.strip()}'. Skipping.")
                print(f"Loaded {len(cached_hashes)} hashes from cache.")
            except IOError as e:
                print(f"Error reading hash cache file '{self.hashes_cache_file}': {e}. Starting with empty cache.")
            except Exception as e:
                print(f"Unexpected error during cache loading: {e}. Starting with empty cache.")
        else:
            print("No existing hash cache found or rebuild requested. Starting with empty cache.")
        return cached_hashes

    def _save_hashes_to_cache(self, hashes: Dict[str, imagehash.ImageHash]):
        """Saves current image hashes to the cache file."""
        print(f"Saving {len(hashes)} hashes to cache: {os.path.abspath(self.hashes_cache_file)}")
        try:
            with open(self.hashes_cache_file, 'w') as f:
                for filepath, img_hash in hashes.items():
                    f.write(f"{filepath},{str(img_hash)}\n")
            print("Hash cache saved.")
        except IOError as e:
            print(f"Error saving hash cache file '{self.hashes_cache_file}': {e}.")

    def find_duplicates(self) -> List[Tuple[str, str]]:
        """
        Main function to find duplicate images.
        Returns a list of tuples, where each tuple contains paths to duplicate images.
        """
        print(f"\nStarting duplicate image detection in: {os.path.abspath(self.input_dir)}")

        current_hashes: Dict[str, imagehash.ImageHash] = self._load_hashes_from_cache()
        hasher = self._get_hasher()

        files_to_hash: List[str] = []
        all_image_paths = []

        # Collect all image paths and identify new/modified files
        for root, _, files in os.walk(self.input_dir):
            for filename in files:
                if filename.lower().endswith(self.image_extensions):
                    filepath = os.path.join(root, filename)
                    all_image_paths.append(filepath)
                    # Check if file needs hashing (not in cache or cache rebuild requested)
                    if self.rebuild_hash_cache or filepath not in current_hashes:
                        files_to_hash.append(filepath)

        print(f"Found {len(all_image_paths)} image files in total.")
        print(f"Hashing {len(files_to_hash)} new or updated images (or rebuilding cache).")

        # Generate hashes for new/updated images
        for filepath in files_to_hash:
            try:
                with Image.open(filepath) as img:
                    img_hash = hasher(img)
                    current_hashes[filepath] = img_hash
            except Exception as e:
                print(f"Error hashing {filepath}: {e}. Skipping.")

        # Remove hashes for files that no longer exist in the input directory
        # (This handles cases where images were deleted)
        keys_to_remove = [p for p in current_hashes if p not in all_image_paths]
        for key in keys_to_remove:
            del current_hashes[key]
            print(f"Removed hash for deleted file: {key}")

        self._save_hashes_to_cache(current_hashes) # Save updated cache

        # Now, compare hashes to find duplicates
        found_duplicates: List[Tuple[str, str]] = []

        # Convert the hash-to-filepaths map into a list of (filepath, hash) for comparison
        all_file_hashes = [(fp, h) for fp, h in current_hashes.items()]

        compared_pairs = set() # To avoid redundant comparisons (A,B is same as B,A)

        total_comparisons = len(all_file_hashes) * (len(all_file_hashes) - 1) // 2
        print(f"Starting {len(all_file_hashes)} image hash comparisons ({total_comparisons} pairs expected).")

        # Iterate through all unique pairs of hashes
        for i in range(len(all_file_hashes)):
            for j in range(i + 1, len(all_file_hashes)):
                filepath1, hash1 = all_file_hashes[i]
                filepath2, hash2 = all_file_hashes[j]

                # If hashes are identical, they are duplicates
                if hash1 == hash2:
                    if (filepath1, filepath2) not in compared_pairs and \
                       (filepath2, filepath1) not in compared_pairs:
                        found_duplicates.append((filepath1, filepath2))
                        compared_pairs.add((filepath1, filepath2))
                else:
                    # If hashes are different, check Hamming distance for near-duplicates
                    if hash1 - hash2 <= self.hash_threshold:
                        if (filepath1, filepath2) not in compared_pairs and \
                           (filepath2, filepath1) not in compared_pairs:
                            found_duplicates.append((filepath1, filepath2))
                            compared_pairs.add((filepath1, filepath2))

        # Write findings to a report file
        self._write_duplicate_report(found_duplicates)

        print(f"Duplicate detection complete. Found {len(found_duplicates)} duplicate/near-duplicate pairs.")
        return found_duplicates

    def _write_duplicate_report(self, duplicates: List[Tuple[str, str]]):
        """Writes the detected duplicate pairs to a report file."""
        print(f"Writing duplicate report to: {os.path.abspath(self.duplicate_report_file)}")
        try:
            with open(self.duplicate_report_file, 'w') as f:
                if not duplicates:
                    f.write("No duplicate or near-duplicate images found.\n")
                else:
                    f.write(f"Duplicate and Near-Duplicate Image Report (Threshold: {self.hash_threshold}, Type: {self.hash_type}):\n\n")
                    for pair in duplicates:
                        f.write(f"- {pair[0]}\n- {pair[1]}\n\n")
            print("Duplicate report written.")
        except IOError as e:
            print(f"Error writing duplicate report file '{self.duplicate_report_file}': {e}.")

    def perform_duplicate_action(self, duplicates: List[Tuple[str, str]], action_type: str) -> int:
        """
        Performs the specified action (move/copy) on one file from each duplicate pair.
        The first file in the tuple is considered the "original" to keep, and the second is the "duplicate" to act upon.
        """
        if action_type not in ['move', 'copy']:
            print(f"Invalid action type: '{action_type}'. Must be 'move' or 'copy'.")
            return 0

        action_count = 0
        action_dir = self.duplicate_action_directory
        os.makedirs(action_dir, exist_ok=True) # Ensure target directory exists

        print(f"\nPerforming duplicate action: '{action_type}' to '{os.path.abspath(action_dir)}'")

        for original_path, duplicate_path in duplicates:
            if not os.path.exists(duplicate_path):
                print(f"Skipping action for '{duplicate_path}': File does not exist.")
                continue

            try:
                # Construct target path, preserving relative directory structure if possible
                relative_path = os.path.relpath(duplicate_path, self.input_dir)
                target_path = os.path.join(action_dir, relative_path)

                os.makedirs(os.path.dirname(target_path), exist_ok=True)

                if action_type == 'move':
                    shutil.move(duplicate_path, target_path)
                    print(f"Moved: '{duplicate_path}' to '{target_path}'")
                elif action_type == 'copy':
                    shutil.copy2(duplicate_path, target_path) # copy2 preserves metadata
                    print(f"Copied: '{duplicate_path}' to '{target_path}'")
                action_count += 1
            except Exception as e:
                print(f"Error performing '{action_type}' on '{duplicate_path}': {e}")

        print(f"Completed '{action_type}' action for {action_count} duplicate files.")
        return action_count

    def delete_duplicates(self, duplicates_to_delete: List[str]) -> int:
        """
        Deletes the specified duplicate image files.
        This operation is permanent and irreversible.
        """
        deleted_count = 0
        print(f"\nAttempting to DELETE {len(duplicates_to_delete)} specified files. THIS IS IRREVERSIBLE!")

        for filepath in duplicates_to_delete:
            if not os.path.exists(filepath):
                print(f"Skipping deletion for '{filepath}': File does not exist.")
                continue

            try:
                os.remove(filepath)
                print(f"DELETED: '{filepath}'")
                deleted_count += 1
            except Exception as e:
                print(f"Error deleting '{filepath}': {e}")

        print(f"Completed deletion of {deleted_count} files.")
        return deleted_count

# Example usage (for testing this module independently)
if __name__ == "__main__":
    # Create a dummy config for testing
    temp_config_path = 'temp_config_duplicate.ini'
    if os.path.exists(temp_config_path):
        os.remove(temp_config_path)

    # Manually create a basic config file for this test
    with open(temp_config_path, 'w') as f:
        f.write("[Paths]\n")
        f.write("input_directory = ./test_duplicate_images\n")
        f.write("image_hashes_cache_file = ./test_duplicate_cache/hashes.txt\n")
        f.write("duplicate_report_file = ./test_duplicate_output/duplicate_report.txt\n")
        f.write("duplicate_action_directory = ./test_duplicate_archive\n") # New action dir
        f.write("\n[DuplicateFinder]\n")
        f.write("enable_duplicate_detection = yes\n")
        f.write("hash_type = dhash\n")
        f.write("hash_threshold = 5\n")
        f.write("rebuild_hash_cache = yes\n")
        f.write("duplicate_action_type = copy\n") # Test copy
        f.write("enable_duplicate_actions = yes\n") # Enable actions

    # Create dummy input images directory and some images
    os.makedirs('./test_duplicate_images', exist_ok=True)
    os.makedirs('./test_duplicate_cache', exist_ok=True)
    os.makedirs('./test_duplicate_output', exist_ok=True)
    os.makedirs('./test_duplicate_archive', exist_ok=True) # Ensure archive dir exists

    try:
        # Create unique images
        Image.new('RGB', (100, 100), color = 'red').save('./test_duplicate_images/red_sq.png')
        Image.new('RGB', (100, 100), color = 'blue').save('./test_duplicate_images/blue_sq.png')

        # Create duplicates/near-duplicates
        dup1_path = './test_duplicate_images/red_sq_copy.png'
        dup2_path = './test_duplicate_images/red_sq_slight_variation.png'
        Image.new('RGB', (100, 100), color = 'red').save(dup1_path)
        Image.new('RGB', (101, 101), color = (250, 0, 0)).save(dup2_path) # Slight size/color variation
        Image.new('RGB', (50, 50), color = 'red').save('./test_duplicate_images/red_sq_small.png') # Resized duplicate

        manager = ConfigManager(temp_config_path)
        finder = DuplicateFinder(manager)
        duplicates = finder.find_duplicates()

        print("\n--- Detected Duplicates ---")
        if duplicates:
            for d1, d2 in duplicates:
                print(f"  - {d1}\n  - {d2}\n")

            # Test perform_duplicate_action
            print("\n--- Testing Perform Duplicate Action (Copy) ---")
            # For testing, let's say we want to act on the second file of each pair
            files_to_action = [pair[1] for pair in duplicates]
            finder.perform_duplicate_action(duplicates, 'copy') # Using 'copy' based on config

            # Test delete_duplicates (only for a subset or dummy files to be safe)
            # CAUTION: This will permanently delete files!
            print("\n--- Testing Delete Duplicates (for red_sq_copy.png) ---")
            if os.path.exists(dup1_path): # Only delete if it still exists
                deleted_count = finder.delete_duplicates([dup1_path])
                print(f"Deleted {deleted_count} files in delete test.")

        else:
            print("No duplicates found.")

    finally:
        # Clean up dummy files/dirs
        import shutil
        if os.path.exists('./test_duplicate_images'): shutil.rmtree('./test_duplicate_images')
        if os.path.exists('./test_duplicate_cache'): shutil.rmtree('./test_duplicate_cache')
        if os.path.exists('./test_duplicate_output'): shutil.rmtree('./test_duplicate_output')
        if os.path.exists('./test_duplicate_archive'): shutil.rmtree('./test_duplicate_archive')
        if os.path.exists(temp_config_path): os.remove(temp_config_path)
