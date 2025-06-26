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

import customtkinter as ctk
from core.config_manager import ConfigManager
from gui.app_gui import AppGUI
import os

# --- Full COMMON_RESOLUTIONS_DEFINITIONS for initial file creation ---
# This ensures that if resolution_definitions.py doesn't exist, it's populated
# with the complete, known set of definitions, preventing overwrites.
_INITIAL_COMMON_RESOLUTIONS_CONTENT = """from typing import Dict, Tuple

# Master dictionary of common aspect ratios and their associated resolutions
# This acts as the authoritative source for resolution definitions.
# This dictionary can be updated by the scanner's merging functions.
COMMON_RESOLUTIONS_DEFINITIONS: Dict[str, Dict[str, Tuple[int, int]]] = {
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
    },
    '3:5': {
        'Custom Portrait': (1680, 2800)
    },
    '7:10': {
        'Custom Portrait': (1400, 2000)
    },
    '19:24': {
        'Custom Portrait': (1216, 1536)
    },
    '47:53': {
        'Custom Portrait': (1504, 1696)
    },
    '53:88': {
        'Custom Portrait': (1696, 2816)
    },
    '55:84': {
        'Custom Portrait': (880, 1344)
    },
    '64:75': {
        'Custom Portrait': (1024, 1200)
    },
    '71:86': {
        'Custom Portrait': (1136, 1376)
    },
    '151:262': {
        'Custom Portrait': (1208, 2096)
    },
    '187:250': {
        'Custom Portrait': (1496, 2000)
    },
    '199:256': {
        'Custom Portrait': (995, 1280)
    },
    '201:308': {
        'Custom Portrait': (1608, 2464)
    },
    '730:499': {
        'Custom Landscape': (730, 499)
    },
    '832:1193': {
        'Custom Portrait': (832, 1193)
    },
    '1469:2560': {
        'Custom Portrait': (1469, 2560)
    },
    '1479:2560': {
        'Custom Portrait': (1479, 2560)
    },
    '1573:2560': {
        'Custom Portrait': (1573, 2560)
    },
    '1645:1152': {
        'Custom Landscape': (1645, 1152)
    },
    '55:69': { # From 165x207
        'Custom Portrait': (165, 207)
    },
    '64:81': { # From 1024x1296
        'Custom Portrait': (1024, 1296)
    },
    '160:263': { # Newly added
        'Common Portrait (160:263)': (1280, 2104)
    }
}
"""


def main():
    # Set the appearance mode and color theme
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # Initialize the configuration manager
    config_manager = ConfigManager(config_file='config.ini')

    # Create dummy directories if they don't exist, so the app starts cleanly
    os.makedirs(config_manager.get('Paths', 'input_directory'), exist_ok=True)
    os.makedirs(config_manager.get('Paths', 'output_directory'), exist_ok=True)
    os.makedirs(config_manager.get('Paths', 'scanner_output_directory'), exist_ok=True)

    # Create the image_cache directory for hashes
    os.makedirs(os.path.dirname(config_manager.get('Paths', 'image_hashes_cache_file')), exist_ok=True) # <-- ADDED THIS LINE

    # Create dummy names.txt and excluded_sizes.txt if they don't exist
    if not os.path.exists(config_manager.get('Paths', 'names_file')):
        with open(config_manager.get('Paths', 'names_file'), 'w') as f:
            f.write("Default\nName\nExample\n")
    if not os.path.exists(config_manager.get('Paths', 'exclusion_reference_file')):
        with open(config_manager.get('Paths', 'exclusion_reference_file'), 'w') as f:
            f.write("# Default exclusion list - add your sizes here (e.g., 1920x1080)\n")
            f.write("1920x1080\n")
            f.write("1024x768\n")

    # Ensure the master_definitions_file (resolution_definitions.py) exists with the full dictionary structure
    master_defs_path = config_manager.get('Paths', 'master_definitions_file')
    if not os.path.exists(master_defs_path):
        os.makedirs(os.path.dirname(master_defs_path), exist_ok=True)
        with open(master_defs_path, 'w') as f:
            f.write(_INITIAL_COMMON_RESOLUTIONS_CONTENT) # Write the full content
        print(f"Created default master definitions file: {master_defs_path}")


    # Create and run the GUI application
    app = AppGUI(config_manager)
    app.mainloop()

if __name__ == "__main__":
    main()
