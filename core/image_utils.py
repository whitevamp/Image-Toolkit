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

import math
import random
import os
from typing import Dict, Tuple, List

# Import COMMON_RESOLUTIONS_DEFINITIONS from its dedicated file
from core.resolution_definitions import COMMON_RESOLUTIONS_DEFINITIONS

# Define a small tolerance for floating-point comparisons of aspect ratios
ASPECT_RATIO_TOLERANCE = 0.01

def get_simplified_ratio_string(width: int, height: int) -> str:
    """Calculates the simplified aspect ratio string (e.g., '16:9') for given dimensions."""
    if height == 0:
        return f"{width}:0" # Handle division by zero for height

    common_divisor = math.gcd(width, height)
    simplified_width = width // common_divisor
    simplified_height = height // common_divisor
    return f"{simplified_width}:{simplified_height}"

def is_portrait_ratio(ar_str: str) -> bool:
    """Checks if an aspect ratio string represents a portrait orientation (height > width)."""
    try:
        w, h = map(int, ar_str.split(':'))
        return h > w
    except ValueError:
        return False # Cannot determine if invalid format (e.g., "1.2:1")

def get_random_name(word_list_file: str, num_words: int = 2) -> str:
    """Generates a readable random name from a word list file."""
    if not os.path.exists(word_list_file):
        print(f"Warning: Word list file '{word_list_file}' not found. Generating a random string instead.")
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))

    try:
        with open(word_list_file, 'r') as f:
            words = [line.strip().capitalize() for line in f if line.strip()]
        if not words:
            print(f"Warning: Word list file '{word_list_file}' is empty. Generating a random string instead.")
            return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))

        return '_'.join(random.sample(words, min(num_words, len(words))))
    except IOError as e:
        print(f"Error reading word list file '{word_list_file}': {e}. Generating a random string instead.")
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
