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

import configparser
import os
from typing import Optional, Dict, Any

class ConfigManager:
    """
    Manages loading and providing access to application configuration from config.ini.
    """
    def __init__(self, config_file: str = 'config.ini'):
        self.config = configparser.ConfigParser()
        self.config_file = config_file
        self.load_config()

    def load_config(self) -> None:
        """Loads or reloads the configuration from the config file."""
        if not os.path.exists(self.config_file):
            print(f"Config file '{self.config_file}' not found. Creating default...")
            self._create_default_config()
            print(f"Default config file created: {self.config_file}")

        try:
            self.config.read(self.config_file)
        except configparser.Error as e:
            print(f"Error reading config file {self.config_file}: {e}")
            raise

    def _create_default_config(self) -> None:
        """Creates a basic default config.ini if one doesn't exist."""
        self.config['Paths'] = {
            'input_directory': './input_images',
            'output_directory': './output_processed_images',
            'names_file': './names.txt',
            'exclusion_reference_file': './excluded_sizes.txt',
            'scanner_output_directory': './scan_reports',
            'master_definitions_file': './core/resolution_definitions.py',
            'image_hashes_cache_file': './image_cache/hashes.txt',
            'duplicate_report_file': './scan_reports/duplicate_images.txt',
            'duplicate_action_directory': './duplicate_actions_archive' # <-- ADDED THIS LINE
        }
        self.config['ImageSettings'] = {
            'override_to_custom_resolution': 'false',
            'custom_width': '1920',
            'custom_height': '1080',
            'fallback_resolution_goal': '4k',
            'output_extension': 'jpg',
            'target_resolution_16_9': '4K UHD',
            'target_resolution_4_3': 'XGA',
            'target_resolution_1_1': 'Square',
            'target_resolution_9_16': 'FHD Portrait',
            'target_resolution_2_3': 'Common AI Gen Portrait',
            'target_resolution_5_8': 'Common AI Gen Portrait',
            'target_resolution_13_19': 'Common AI Gen Portrait'
        }
        self.config['Renaming'] = {
            'enable_random_rename': 'yes'
        }
        self.config['Scanner'] = {
            'enable_exclusion_reference': 'yes',
            'merge_to_master_definitions': 'no'
        }
        self.config['DuplicateFinder'] = {
            'enable_duplicate_detection': 'no',
            'hash_type': 'dhash',
            'hash_threshold': '8',
            'rebuild_hash_cache': 'no',
            'duplicate_action_type': 'none', # <-- ADDED THIS LINE
            'enable_duplicate_actions': 'no' # <-- ADDED THIS LINE
        }

        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

    def get(self, section: str, option: str, fallback: Optional[str] = None) -> str:
        """Gets a string option from the config."""
        return self.config.get(section, option, fallback=fallback)

    def getint(self, section: str, option: str, fallback: Optional[int] = None) -> int:
        """Gets an integer option from the config."""
        return self.config.getint(section, option, fallback=fallback)

    def getboolean(self, section: str, option: str, fallback: Optional[bool] = None) -> bool:
        """Gets a boolean option from the config."""
        return self.config.getboolean(section, option, fallback=fallback)

    def get_section_as_dict(self, section: str) -> Dict[str, str]:
        """Returns all options in a given section as a dictionary."""
        if self.config.has_section(section):
            return dict(self.config.items(section))
        return {}

    def set(self, section: str, option: str, value: Any) -> None:
        """Sets an option in the config (converts value to string) and saves it."""
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, str(value))
        self.save_config()

    def save_config(self) -> None:
        """Saves the current configuration to the config file."""
        try:
            with open(self.config_file, 'w') as configfile:
                self.config.write(configfile)
        except IOError as e:
            print(f"Error saving config file {self.config_file}: {e}")
            raise

# Example usage (for testing this module independently)
if __name__ == "__main__":
    temp_config_path = 'test_config.ini'
    if os.path.exists(temp_config_path):
        os.remove(temp_config_path)

    manager = ConfigManager(temp_config_path)
    print(f"Input Directory: {manager.get('Paths', 'input_directory')}")
    print(f"Output Extension: {manager.get('ImageSettings', 'output_extension')}")

    manager.set('ImageSettings', 'output_extension', 'png')
    print(f"New Output Extension: {manager.get('ImageSettings', 'output_extension')}")

    # Verify the config file was updated
    manager_reloaded = ConfigManager(temp_config_path)
    print(f"Reloaded config Output Extension: {manager_reloaded.get('ImageSettings', 'output_extension')}")
    print(f"Hash Type: {manager_reloaded.get('DuplicateFinder', 'hash_type')}")
    print(f"Duplicate Action Type: {manager_reloaded.get('DuplicateFinder', 'duplicate_action_type')}")

    if os.path.exists(temp_config_path):
        os.remove(temp_config_path) # Clean up
