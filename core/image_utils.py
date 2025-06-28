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
import math

# Aspect Ratio Tolerance: How close a calculated aspect ratio needs to be
# to a common aspect ratio (e.g., 1.777... for 16:9) to be considered a match.
# A smaller number means stricter matching.
# For example, 0.01 would mean within 1% difference of the ratio.
# This tolerance helps account for slight variations due to source image quality,
# minor cropping, or floating-point inaccuracies.
ASPECT_RATIO_TOLERANCE = 0.005 # Adjusted to be slightly stricter, common for image aspect ratios

def get_simplified_ratio_string(width: int, height: int) -> str:
    """Calculates and returns the simplified aspect ratio string (e.g., "16:9")."""
    if height == 0:
        return "N/A" # Or raise an error, depending on desired behavior for zero height

    gcd_val = math.gcd(width, height)
    simplified_width = width // gcd_val
    simplified_height = height // gcd_val
    return f"{simplified_width}:{simplified_height}"

def is_portrait_ratio(ar_string: str) -> bool:
    """
    Determines if an aspect ratio string represents a portrait orientation.
    Handles both 'W:H' (e.g., '9:16') and decimal strings (e.g., '0.5625:1').
    """
    try:
        parts = ar_string.split(':')
        if len(parts) == 2:
            width = float(parts[0])
            height = float(parts[1])
            return height > width
        else:
            # Handle cases like "2.35:1" which is still landscape,
            # but relies on the actual decimal ratio to determine orientation.
            # If the aspect ratio string is not "W:H" format, we assume it's
            # a ratio normalized to 1 (e.g., "0.5625") or similar.
            # If it's a decimal form like 0.5625 (for 9:16), then width < height.
            # If it's 1.777... (for 16:9), then width > height.
            # Convert to actual float ratio to compare
            decimal_ratio = float(ar_string)
            return decimal_ratio < 1.0 # If width/height < 1, it's portrait
    except ValueError:
        print(f"Warning: Could not parse aspect ratio string for orientation: '{ar_string}'. Assuming landscape.")
        return False # Default to false if parsing fails

def get_random_name(names_file_path: str) -> str:
    """Reads a random name from the specified names file."""
    if not os.path.exists(names_file_path):
        print(f"Warning: Names file '{names_file_path}' not found. Using default name.")
        return "random_image"

    try:
        with open(names_file_path, 'r', encoding='utf-8') as f:
            names = [line.strip() for line in f if line.strip()]
        if names:
            return names[os.urandom(1)[0] % len(names)] # Cryptographically strong random index
        else:
            print(f"Warning: Names file '{names_file_path}' is empty. Using default name.")
            return "random_image"
    except Exception as e:
        print(f"Error reading names file '{names_file_path}': {e}. Using default name.")
        return "random_image"



