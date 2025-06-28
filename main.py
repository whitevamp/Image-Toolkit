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

# This script initializes the application, sets up directories, and runs the GUI.
# It ensures that necessary configuration files and directories are created if they do not exist.
# It also checks for duplicate aspect ratios in the resolution definitions file at startup.
# This is the main entry point for the Image Toolkit application.
# This file is part of the Image Toolkit project, which provides tools for image processing and management.
# This file is responsible for setting up the application environment and launching the GUI.
# It is designed to be run as a standalone script, initializing the application and starting the GUI.


# main.py - Main entry point for the Image Toolkit application
import os
import sys
import configparser
import shutil # For initial directory setup
import ast # For safely evaluating strings from config
import importlib.util # For dynamic import of resolution_definitions.py

# Add the directory containing main.py to sys.path
# This ensures sibling modules like app_gui.py can be imported
script_dir_for_sys_path = os.path.dirname(os.path.abspath(__file__))
if script_dir_for_sys_path not in sys.path:
    sys.path.insert(0, script_dir_for_sys_path)

# Corrected import path for AppGUI (assuming app_gui.py is in the same directory as main.py)
from gui.app_gui import AppGUI
from core.config_manager import ConfigManager # This will now be the modified ConfigManager

# Define the initial content for resolution_definitions.py
# This will be written if the file doesn't exist or is empty.
_INITIAL_COMMON_RESOLUTIONS_CONTENT = """
COMMON_RESOLUTIONS_DEFINITIONS = {
    '16:9': {
        '720p': (1280, 720), # Commonly known as HD
        '1080p': (1920, 1080), # Commonly known as Full HD
        '1440p': (2560, 1440), # Commonly known as QHD or 2K
        '4K UHD': (3840, 2160),
        '8K UHD': (7680, 4320)
    },
    '4:3': {
        'VGA': (640, 480), # Often just called 'SD' but VGA is a specific historical term
        'SVGA': (800, 600),
        'XGA': (1024, 768),
        'SXGA+': (1400, 1050),
        'UXGA': (1600, 1200),
        'QXGA': (2048, 1536)
    },
    '21:9': {
        'UW-FHD': (2560, 1080),
        'UW-QHD': (3440, 1440),
        'UW-4K': (5120, 2160)
    },
    '16:10': {
        'WXGA': (1280, 800),
        'WXGA+': (1440, 900),
        'WSXGA+': (1680, 1050),
        'WUXGA': (1920, 1200)
    },
    '3:2': {
        'Surface Laptop': (2256, 1504),
        'Surface Pro': (2736, 1824)
    },
    '5:4': {
        'SXGA': (1280, 1024)
    },
    '1:1': {
        'Square': (1080, 1080),
        'Instagram': (640, 640),
        'Common AI Gen Square': (512, 512),
        'Higher Res Square': (2048, 2048)
    },
    '9:16': { # Portrait (inverse of 16:9)
        'FHD Portrait': (1080, 1920),
        'QHD Portrait': (1440, 2560),
        '4K Portrait': (2160, 3840)
    },
    '2:3': { # Portrait (inverse of 3:2)
        'Common AI Gen Portrait': (1024, 1536),
        'Medium Portrait': (1504, 2256)
    },
    '5:8': { # Portrait (inverse of 8:5)
        'Common AI Gen Portrait': (800, 1280),
        'Medium Portrait': (1000, 1600),
        'Large Portrait': (1250, 2000),
        'Extra Large Portrait': (1500, 2400),
        'Super Large Portrait': (2000, 3200),
        'Small Portrait': (400, 640),
        'Extra Small Portrait': (250, 400)
    },
    '13:19': { # Portrait (inverse of 19:13)
        'Common AI Gen Portrait': (832, 1216),
        'Small Portrait': (416, 608),
        'Extra Small Portrait': (208, 304),
        'Medium Portrait': (1040, 1520),
        'Large Portrait': (1300, 1900),
        'Extra Large Portrait': (1560, 2280),
        'Super Large Portrait': (1820, 2660),
        'Ultra Large Portrait': (2080, 3040)
    },
    '32:9': { # Super Ultrawide
        'Super Ultrawide FHD': (3840, 1080),
        'Super Ultrawide QHD': (5120, 1440),
        'Super Ultrawide 4K': (7680, 2160)
    },
    '5:3': { # Common for some older laptops/displays, slightly wider than 16:10
        'Common Laptop': (1280, 768),
        'HD-Ready': (1360, 768)
    },
    '2.35:1': { # Cinematic Aspect Ratio (often rounded to 21:9 or 2.39:1)
        'Cinema FHD': (1920, 817),
        'Cinema 4K': (4096, 1746)
    },
    '2.39:1': { # Wider Cinematic Aspect Ratio (common in films)
        'Cinema FHD': (1920, 803),
        'Cinema 4K': (4096, 1716)
    },
    '3:4': { # Portrait (inverse of 4:3)
        'VGA Portrait': (480, 640),
        'XGA Portrait': (768, 1024),
        'UXGA Portrait': (1200, 1600),
        'UXGA+ Portrait': (1536, 2048),
        'QHD-Equivalent Portrait': (1920, 2560),
        'XGA+ Portrait': (1152, 1536)
    },
    '10:16': { # Portrait (inverse of 16:10)
        'WXGA Portrait': (800, 1280),
        'WUXGA Portrait': (1200, 1920)
    },
    '9:21': { # Portrait (inverse of 21:9)
        'UW-FHD Portrait': (1080, 2560),
        'UW-QHD Portrait': (1440, 3440)
    },
    '850:1169': { # Specific Portrait Aspect Ratio
        'Custom Portrait': (850, 1169)
    },
    '1280:1811': { # Specific Portrait Aspect Ratio
        'Custom Portrait': (1280, 1811)
    },
    '4:5': {
        'Large 4:5 Portrait': (2048, 2560),
        'Medium 4:5 Portrait': (1024, 1280),
        'Desktop Portrait': (1280, 1600)
    }
}
"""

def create_initial_config_and_dirs(primary_config_path='config.ini', image_settings_config_path='image_settings.ini'):
    """
    Creates initial directories and default config files if they don't exist.
    Ensures resolution_definitions.py also exists and has default content.
    """
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = current_script_dir

    if os.path.basename(current_script_dir) == 'image_processing' and \
       os.path.exists(os.path.join(current_script_dir, 'Image-Toolkit', 'main.py')):
        script_dir = os.path.join(current_script_dir, 'Image-Toolkit')

    print(f"Debug: Determined project root directory (script_dir): {script_dir}")

    # Initialize ConfigManager here to ensure default files are created
    # This will create both config.ini and image_settings.ini if they don't exist
    config_manager_for_init = ConfigManager(primary_config_path, image_settings_config_path)

    # Use a regular ConfigParser to read/write for initial setup,
    # as ConfigManager handles defaults internally now.
    # The purpose of this function is to set up directories and ensure master_definitions_file
    # based on potentially *newly created* config files.
    config = configparser.ConfigParser()
    config.read([primary_config_path, image_settings_config_path]) # Read both into a temp parser

    # Define default paths relative to the *determined* script_dir
    # These will be written to the config files by ConfigManager's _create_default methods,
    # but we use them here for directory creation logic.
    default_input_dir = os.path.join(script_dir, 'input_images')
    default_output_dir = os.path.join(script_dir, 'output_processed_images')
    default_scanner_output_dir = os.path.join(script_dir, 'scan_reports')
    default_exclusion_file = os.path.join(script_dir, 'excluded_sizes.txt')
    default_master_defs_file = os.path.join(script_dir, 'core', 'resolution_definitions.py')
    default_hashes_cache_file = os.path.join(script_dir, 'image_cache', 'image_hashes.txt')
    default_duplicate_report_file = os.path.join(script_dir, 'duplicate_reports', 'duplicate_images.txt')
    default_duplicate_action_dir = os.path.join(script_dir, 'duplicate_actions_archive')
    default_names_file = os.path.join(script_dir, 'names.txt')

    # Create directories if they don't exist
    paths_to_ensure = [
        config.get('Paths', 'input_directory', fallback=default_input_dir),
        config.get('Paths', 'output_directory', fallback=default_output_dir),
        config.get('Paths', 'scanner_output_directory', fallback=default_scanner_output_dir),
        os.path.dirname(config.get('Paths', 'image_hashes_cache_file', fallback=default_hashes_cache_file)),
        os.path.dirname(config.get('Paths', 'duplicate_report_file', fallback=default_duplicate_report_file)),
        config.get('Paths', 'duplicate_action_directory', fallback=default_duplicate_action_dir)
    ]

    for path_value in paths_to_ensure:
        if not os.path.isabs(path_value):
            final_absolute_path = os.path.join(script_dir, path_value)
        else:
            final_absolute_path = path_value
        os.makedirs(final_absolute_path, exist_ok=True)
        print(f"Ensured directory: {final_absolute_path}")

    # Ensure resolution_definitions.py exists and has initial content
    master_defs_file_path_from_config = config.get('Paths', 'master_definitions_file', fallback=default_master_defs_file)
    if not os.path.isabs(master_defs_file_path_from_config):
        final_master_defs_file_path = os.path.join(script_dir, master_defs_file_path_from_config)
    else:
        final_master_defs_file_path = master_defs_file_path_from_config

    if not os.path.exists(final_master_defs_file_path) or os.path.getsize(final_master_defs_file_path) == 0:
        print(f"Creating initial '{final_master_defs_file_path}' with default common resolutions...")
        os.makedirs(os.path.dirname(final_master_defs_file_path), exist_ok=True)
        with open(final_master_defs_file_path, 'w') as f:
            f.write(_INITIAL_COMMON_RESOLUTIONS_CONTENT)
        print(f"Created initial resolution definitions file: {final_master_defs_file_path}")
    else:
        print(f"Resolution definitions file already exists: {final_master_defs_file_path}")

    # Ensure names.txt exists
    names_file_path = config.get('Paths', 'names_file', fallback=default_names_file)
    if not os.path.exists(names_file_path):
        print(f"Creating initial '{names_file_path}'...")
        with open(names_file_path, 'w') as f:
            f.write("image\nphoto\npicture\nlandscape\nportrait\nabstract\nvista\nscene\nart\n")
        print(f"Created initial names file: {os.path.abspath(names_file_path)}")

    # Ensure exclusion_reference.txt exists
    exclusion_file_path = config.get('Paths', 'exclusion_reference_file', fallback=default_exclusion_file)
    if not os.path.exists(exclusion_file_path):
        print(f"Creating initial '{exclusion_file_path}'...")
        with open(exclusion_file_path, 'w') as f:
            f.write("# Add resolutions to exclude from scanning (e.g., 1920x1080)\n")
        print(f"Created initial exclusion reference file: {os.path.abspath(exclusion_file_path)}")

    print(f"Configuration file '{primary_config_path}' and '{image_settings_config_path}' ensured/updated.")

# print("DEBUG: Before duplicate check block")
# Check for duplicate aspect ratios at startup
try:
    from core.definitions_dup_check import check_for_duplicate_aspect_ratios
    check_for_duplicate_aspect_ratios()
except Exception as e:
    print(f"[WARNING] Could not check for duplicate aspect ratios: {e}")

def main():
    """Main function to initialize and run the GUI application."""
    primary_config_file_path = 'config.ini'
    image_settings_config_file_path = 'image_settings.ini'

    # Ensure initial configuration and directories are set up
    create_initial_config_and_dirs(primary_config_file_path, image_settings_config_file_path)

    # Initialize ConfigManager with both config file paths
    config_manager = ConfigManager(primary_config_path=primary_config_file_path,
                                   image_settings_config_path=image_settings_config_file_path)

    # Now, run the GUI
    app = AppGUI(config_manager)
    app.mainloop()

if __name__ == "__main__":
    main()