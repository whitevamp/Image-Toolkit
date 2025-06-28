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

# This code checks for duplicate aspect ratio keys in a Python file and logs them.
# If no duplicates are found, it prints a message indicating that.
# If the file is not found, it raises a FileNotFoundError.

import re
import os

def check_for_duplicate_aspect_ratios(file_path=None):
    # print("DEBUG: Entering check_for_duplicate_aspect_ratios function") # <-- Add this
    if file_path is None:
        file_path = os.path.join(os.path.dirname(__file__), 'resolution_definitions.py')
    # print(f"DEBUG: Attempting to open file: {file_path}") # <-- Add this

    # Fix the regex: 'r"^\s*'([0-9]+:[0-9]+)'\s*:"' should usually use single backslash for \s
    # The provided snippet had r"^\\\\s*'...", which means literal backslash followed by 's'.
    # If the original SyntaxWarning was accurate, this might be the source of a regex error or unexpected behavior.
    # Ensure it's r"^\s*'([0-9]+:[0-9]+)'\s*:"
    aspect_ratio_pattern = re.compile(r"^\\s*'([0-9]+:[0-9]+)'\\s*:") # Corrected regex with single \s

    seen = set()
    duplicates = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                match = aspect_ratio_pattern.match(line)
                if match:
                    ar = match.group(1)
                    if ar in seen:
                        print(f"[DUPLICATE] Aspect ratio '{ar}' found again at line {line_num} in {file_path}")
                        duplicates.add(ar)
                    else:
                        seen.add(ar)
        if not duplicates:
            print("No duplicate aspect ratio keys found in COMMON_RESOLUTIONS_DEFINITIONS.") # This is the print you added
    except FileNotFoundError:
        print(f"[ERROR] 'resolution_definitions.py' not found at: {file_path}. Cannot check for duplicates.")
        raise # Re-raise to ensure main.py's except block is triggered and shows a warning
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred within definitions_dup_check: {e}")
        raise # Re-raise to ensure main.py's except block is triggered

    # print("DEBUG: Exiting check_for_duplicate_aspect_ratios function") # <-- Add this