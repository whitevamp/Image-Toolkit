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

# This code is part of the Image Toolkit project, which provides a configuration manager
# for loading and managing application settings from config files.

import configparser
import os
from typing import Optional, Dict, Any

class ConfigManager:
    """
    Manages loading and providing access to application configuration from config.ini.
    Can handle loading and saving specific sections to separate files.
    """
    def __init__(self, primary_config_path: str = 'config.ini', image_settings_config_path: str = 'image_settings.ini'):
        self.primary_config_path = primary_config_path
        self.image_settings_config_path = image_settings_config_path
        self.config = configparser.ConfigParser() # This will hold the merged view

        self._load_configs() # Load both primary and image settings

    def _load_configs(self) -> None:
        """Loads configurations from both primary and image settings files."""
        self._load_primary_config()
        self._load_image_settings_config()

    def _load_primary_config(self) -> None:
        """Loads or creates the primary configuration file."""
        if not os.path.exists(self.primary_config_path):
            print(f"Primary config file '{self.primary_config_path}' not found. Creating default...")
            self._create_default_primary_config()
            print(f"Default primary config file created: {self.primary_config_path}")

        try:
            self.config.read(self.primary_config_path)
        except configparser.Error as e:
            print(f"Error reading primary config file {self.primary_config_path}: {e}")
            raise

    def _load_image_settings_config(self) -> None:
        """Loads or creates the image settings configuration file."""
        if not os.path.exists(self.image_settings_config_path):
            print(f"Image settings config file '{self.image_settings_config_path}' not found. Creating default...")
            self._create_default_image_settings_config()
            print(f"Default image settings config file created: {self.image_settings_config_path}")

        try:
            # configparser.read() will merge sections, last read takes precedence
            self.config.read(self.image_settings_config_path)
        except configparser.Error as e:
            print(f"Error reading image settings config file {self.image_settings_config_path}: {e}")
            raise

    def _create_default_primary_config(self) -> None:
        """Creates a basic default config.ini if one doesn't exist."""
        default_primary_parser = configparser.ConfigParser()

        default_primary_parser['Paths'] = {
            'input_directory': './input_images',
            'output_directory': './output_processed_images',
            'names_file': './names.txt',
            'exclusion_reference_file': './excluded_sizes.txt',
            'scanner_output_directory': './scan_reports',
            'master_definitions_file': './core/resolution_definitions.py',
            'image_hashes_cache_file': './image_cache/hashes.txt',
            'duplicate_report_file': './scan_reports/duplicate_images.txt',
            'duplicate_action_directory': './duplicate_actions_archive'
        }
        default_primary_parser['Renaming'] = {
            'enable_random_rename': 'yes'
        }
        default_primary_parser['Scanner'] = {
            'enable_exclusion_reference': 'yes',
            'merge_to_master_definitions': 'no'
        }
        default_primary_parser['DuplicateFinder'] = {
            'enable_duplicate_detection': 'no',
            'hash_type': 'dhash',
            'hash_threshold': '8',
            'rebuild_hash_cache': 'no',
            'duplicate_action_type': 'none',
            'enable_duplicate_actions': 'no'
        }

        with open(self.primary_config_path, 'w') as configfile:
            default_primary_parser.write(configfile)
        self.config.read(self.primary_config_path)


    def _create_default_image_settings_config(self) -> None:
        """Creates a default image_settings.ini file if one doesn't exist."""
        default_image_settings_parser = configparser.ConfigParser()

        default_image_settings_parser['ImageSettings'] = {
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

        with open(self.image_settings_config_path, 'w') as configfile:
            default_image_settings_parser.write(configfile)
        self.config.read(self.image_settings_config_path)


    def get(self, section: str, option: str, fallback: Optional[str] = None) -> str:
        """Gets a string option from the merged config."""
        result = self.config.get(section, option, fallback=fallback)
        return result if result is not None else ""

    def getint(self, section: str, option: str, fallback: Optional[int] = None) -> int:
        """Gets an integer option from the merged config."""
        actual_fallback = fallback if fallback is not None else 0
        return self.config.getint(section, option, fallback=actual_fallback)

    def getboolean(self, section: str, option: str, fallback: Optional[bool] = None) -> bool:
        """Gets a boolean option from the merged config."""
        actual_fallback = fallback if fallback is not None else False
        return self.config.getboolean(section, option, fallback=actual_fallback)

    def get_section_as_dict(self, section: str) -> Dict[str, str]:
        """Returns all options in a given section from the merged config as a dictionary."""
        if self.config.has_section(section):
            return dict(self.config.items(section))
        return {}

    def set(self, section: str, option: str, value: Any) -> None:
        """Sets an option in the in-memory merged config (converts value to string).
        Does NOT automatically save to disk. Call save_configs() explicitly."""
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, str(value))


    def save_configs(self) -> None:
        """Saves the current configuration to their respective config files."""
        try:
            primary_parser = configparser.ConfigParser()
            for section in self.config.sections():
                if section != 'ImageSettings':
                    primary_parser[section] = self.config[section]

            with open(self.primary_config_path, 'w') as configfile:
                primary_parser.write(configfile)

            image_settings_parser = configparser.ConfigParser()
            if 'ImageSettings' in self.config:
                image_settings_parser['ImageSettings'] = self.config['ImageSettings']

            with open(self.image_settings_config_path, 'w') as configfile:
                image_settings_parser.write(configfile)

        except IOError as e:
            print(f"Error saving config files: {e}")
            raise