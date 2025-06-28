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

# This code is part of the Image Toolkit project, which provides a GUI for image processing,
# scanning, duplicate finding, and configuration management.

import customtkinter as ctk
import os
import threading
from tkinter import filedialog, messagebox
from typing import Any, List, Tuple
import importlib.util # Added for dynamic import

# Import core functionalities
from core.config_manager import ConfigManager
from core.image_scanner import ImageScanner
from core.image_processor import ImageProcessor
from core.duplicate_finder import DuplicateFinder
# COMMON_RESOLUTIONS_DEFINITIONS is now imported dynamically within methods where needed

class AppGUI(ctk.CTk):
    def __init__(self, config_manager: ConfigManager):
        super().__init__()
        self.config_manager = config_manager

        self.title("Image Toolkit") # Updated title
        self.geometry("900x800") # Increased height slightly for new content
        self.resizable(True, True)

        # Variables to store found duplicate paths for deletion
        self._found_duplicate_pairs: List[Tuple[str, str]] = []

        # --- License and About text content ---
        self.ABOUT_TEXT = """
Image Toolkit

Version: 1.0.0
Author: whitevamp
Contact: https://github.com/whitevamp/Image-Toolkit

Image Toolkit is a versatile Python-based application designed to help you
efficiently manage your digital image collection.

Key Features:
- **Image Processing:** Resize and convert images to various formats.
  Supports global custom resolutions or intelligent aspect-ratio-based scaling.
- **Image Scanning:** Analyze your image library, generate reports on dimensions,
  and identify resolutions that are not yet defined in the master definitions.
- **Duplicate Finder:** Detects duplicate and near-duplicate images using
  advanced perceptual hashing (aHash, pHash, dHash, wHash) with configurable
  thresholds. Includes options to move, copy, or permanently delete flagged duplicates.
- **Configurable Settings:** All paths, processing options, and duplicate
  finder parameters are easily configurable via a user-friendly GUI and config.ini.

This software is designed to streamline your workflow and help you maintain
a tidy and organized image library.
"""
        # Load GPL v3.0 text from the license file
        self.GPL_LICENSE_TEXT = self._load_gpl_license_text()

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- Console Output (MUST BE INITIALIZED EARLY) ---
        self.console_output = ctk.CTkTextbox(self, height=100, corner_radius=10)
        self.console_output.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.console_output.insert("end", "Application Ready.\n")
        self.console_output.configure(state="disabled")


        # --- Top Frame for Global Settings (Paths & Override) ---
        self.top_frame = ctk.CTkFrame(self, corner_radius=10)
        self.top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.top_frame.grid_columnconfigure((0,1), weight=1)

        self.input_dir_label = ctk.CTkLabel(self.top_frame, text="Input Directory:")
        self.input_dir_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.input_dir_entry = ctk.CTkEntry(self.top_frame, width=250, placeholder_text="Select input folder")
        self.input_dir_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        self.input_dir_entry.insert(0, self.config_manager.get('Paths', 'input_directory'))
        self.input_dir_button = ctk.CTkButton(self.top_frame, text="Browse", command=lambda: self._browse_directory(self.input_dir_entry, 'Paths', 'input_directory'))
        self.input_dir_button.grid(row=0, column=2, padx=10, pady=5)

        self.output_dir_label = ctk.CTkLabel(self.top_frame, text="Output Directory (Processed):")
        self.output_dir_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.output_dir_entry = ctk.CTkEntry(self.top_frame, width=250, placeholder_text="Select output folder")
        self.output_dir_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        self.output_dir_entry.insert(0, self.config_manager.get('Paths', 'output_directory'))
        self.output_dir_button = ctk.CTkButton(self.top_frame, text="Browse", command=lambda: self._browse_directory(self.output_dir_entry, 'Paths', 'output_directory'))
        self.output_dir_button.grid(row=1, column=2, padx=10, pady=5)

        self.scanner_output_dir_label = ctk.CTkLabel(self.top_frame, text="Output Directory (Scanner Reports):")
        self.scanner_output_dir_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.scanner_output_dir_entry = ctk.CTkEntry(self.top_frame, width=250, placeholder_text="Select scanner output folder")
        self.scanner_output_dir_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        self.scanner_output_dir_entry.insert(0, self.config_manager.get('Paths', 'scanner_output_directory'))
        self.scanner_output_dir_button = ctk.CTkButton(self.top_frame, text="Browse", command=lambda: self._browse_directory(self.scanner_output_dir_entry, 'Paths', 'scanner_output_directory'))
        self.scanner_output_dir_button.grid(row=2, column=2, padx=10, pady=5)

        self.override_custom_var = ctk.BooleanVar(value=self.config_manager.getboolean('ImageSettings', 'override_to_custom_resolution'))
        self.override_custom_checkbox = ctk.CTkCheckBox(self.top_frame, text="Override All to Custom Resolution", variable=self.override_custom_var, command=self._toggle_custom_resolution_fields)
        self.override_custom_checkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.custom_width_label = ctk.CTkLabel(self.top_frame, text="Custom Width:")
        self.custom_width_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.custom_width_entry = ctk.CTkEntry(self.top_frame, width=100)
        self.custom_width_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.custom_width_entry.insert(0, str(self.config_manager.getint('ImageSettings', 'custom_width')))

        self.custom_height_label = ctk.CTkLabel(self.top_frame, text="Custom Height:")
        self.custom_height_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.custom_height_entry = ctk.CTkEntry(self.top_frame, width=100)
        self.custom_height_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        self.custom_height_entry.insert(0, str(self.config_manager.getint('ImageSettings', 'custom_height')))

        self.fallback_goal_label = ctk.CTkLabel(self.top_frame, text="Fallback Resolution Goal:")
        self.fallback_goal_label.grid(row=6, column=0, padx=10, pady=(10,0), sticky="w")
        self.fallback_goal_options = ['1080p', '1440p', '4k', 'custom']
        self.fallback_goal_var = ctk.StringVar(value=self.config_manager.get('ImageSettings', 'fallback_resolution_goal'))
        self.fallback_goal_dropdown = ctk.CTkOptionMenu(self.top_frame, values=self.fallback_goal_options, variable=self.fallback_goal_var, command=lambda val: self._update_config_setting('ImageSettings', 'fallback_resolution_goal', val))
        self.fallback_goal_dropdown.grid(row=6, column=1, padx=10, pady=(0,10), sticky="ew")

        self._toggle_custom_resolution_fields() # Set initial state

        # --- Main Tabview for Operations ---
        self.tabview = ctk.CTkTabview(self, corner_radius=10)
        self.tabview.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.tabview.add("Image Processing")
        self.tabview.add("Image Scanning")
        self.tabview.add("Duplicate Finder")
        self.tabview.add("Tools & Settings")
        self.tabview.add("About")
        self.tabview.add("License")


        # --- Image Processing Tab ---
        self.tabview.tab("Image Processing").grid_columnconfigure(0, weight=1)

        self.process_button = ctk.CTkButton(self.tabview.tab("Image Processing"), text="Start Image Processing", command=self._start_image_processing_thread)
        self.process_button.grid(row=0, column=0, padx=20, pady=20)

        self.output_ext_label = ctk.CTkLabel(self.tabview.tab("Image Processing"), text="Output Extension:")
        self.output_ext_label.grid(row=1, column=0, padx=20, pady=(10,0), sticky="w")
        self.output_ext_options = ['original', 'jpg', 'png', 'webp', 'bmp', 'tiff']
        self.output_ext_var = ctk.StringVar(value=self.config_manager.get('ImageSettings', 'output_extension'))
        self.output_ext_dropdown = ctk.CTkOptionMenu(self.tabview.tab("Image Processing"), values=self.output_ext_options, variable=self.output_ext_var, command=lambda val: self._update_config_setting('ImageSettings', 'output_extension', val))
        self.output_ext_dropdown.grid(row=2, column=0, padx=20, pady=(0,10), sticky="ew")

        self.rename_var = ctk.BooleanVar(value=self.config_manager.getboolean('Renaming', 'enable_random_rename'))
        self.rename_checkbox = ctk.CTkCheckBox(self.tabview.tab("Image Processing"), text="Enable Random Renaming", variable=self.rename_var, command=lambda: self._update_config_setting('Renaming', 'enable_random_rename', self.rename_var.get()))
        self.rename_checkbox.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        # --- Image Scanning Tab ---
        self.tabview.tab("Image Scanning").grid_columnconfigure(0, weight=1)
        self.scan_button = ctk.CTkButton(self.tabview.tab("Image Scanning"), text="Start Image Scan & Generate Reports", command=self._start_image_scanning_thread)
        self.scan_button.grid(row=0, column=0, padx=20, pady=20)

        self.exclusion_var = ctk.BooleanVar(value=self.config_manager.getboolean('Scanner', 'enable_exclusion_reference'))
        self.exclusion_checkbox = ctk.CTkCheckBox(self.tabview.tab("Image Scanning"), text="Enable Exclusion Reference", variable=self.exclusion_var, command=lambda: self._update_config_setting('Scanner', 'enable_exclusion_reference', self.exclusion_var.get()))
        self.exclusion_checkbox.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.exclusion_file_label = ctk.CTkLabel(self.tabview.tab("Image Scanning"), text="Exclusion File:")
        self.exclusion_file_label.grid(row=2, column=0, padx=20, pady=(10,0), sticky="w")
        self.exclusion_file_entry = ctk.CTkEntry(self.tabview.tab("Image Scanning"), width=250, placeholder_text="Select exclusion file")
        self.exclusion_file_entry.grid(row=3, column=0, padx=20, pady=(0,10), sticky="ew")
        self.exclusion_file_entry.insert(0, self.config_manager.get('Paths', 'exclusion_reference_file'))
        self.exclusion_file_button = ctk.CTkButton(self.tabview.tab("Image Scanning"), text="Browse", command=lambda: self._browse_file(self.exclusion_file_entry, 'Paths', 'exclusion_reference_file'))
        self.exclusion_file_button.grid(row=3, column=1, padx=20, pady=(0,10))

        self.merge_master_var = ctk.BooleanVar(value=self.config_manager.getboolean('Scanner', 'merge_to_master_definitions'))
        self.merge_master_checkbox = ctk.CTkCheckBox(self.tabview.tab("Image Scanning"), text="Merge New Dims to Master Definitions", variable=self.merge_master_var, command=lambda: self._update_config_setting('Scanner', 'merge_to_master_definitions', self.merge_master_var.get()))
        self.merge_master_checkbox.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        self.master_defs_file_label = ctk.CTkLabel(self.tabview.tab("Image Scanning"), text="Master Definitions File:")
        self.master_defs_file_label.grid(row=5, column=0, padx=20, pady=(10,0), sticky="w")
        self.master_defs_file_entry = ctk.CTkEntry(self.tabview.tab("Image Scanning"), width=250, placeholder_text="Path to resolution_definitions.py")
        self.master_defs_file_entry.grid(row=6, column=0, padx=20, pady=(0,10), sticky="ew")
        self.master_defs_file_entry.insert(0, self.config_manager.get('Paths', 'master_definitions_file'))
        self.master_defs_file_button = ctk.CTkButton(self.tabview.tab("Image Scanning"), text="Browse", command=lambda: self._browse_file(self.master_defs_file_entry, 'Paths', 'master_definitions_file'))
        self.master_defs_file_button.grid(row=6, column=1, padx=20, pady=(0,10))


        # --- Duplicate Finder Tab ---
        self.tabview.tab("Duplicate Finder").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Duplicate Finder").grid_columnconfigure(1, weight=1) # Second column for browse buttons

        self.duplicate_button = ctk.CTkButton(self.tabview.tab("Duplicate Finder"), text="Find Duplicate Images", command=self._start_duplicate_finder_thread)
        self.duplicate_button.grid(row=0, column=0, padx=20, pady=20, columnspan=2) # Spanning two columns

        self.enable_duplicate_var = ctk.BooleanVar(value=self.config_manager.getboolean('DuplicateFinder', 'enable_duplicate_detection'))
        self.enable_duplicate_checkbox = ctk.CTkCheckBox(self.tabview.tab("Duplicate Finder"), text="Enable Duplicate Detection", variable=self.enable_duplicate_var, command=lambda: self._update_config_setting('DuplicateFinder', 'enable_duplicate_detection', self.enable_duplicate_var.get()))
        self.enable_duplicate_checkbox.grid(row=1, column=0, padx=20, pady=10, sticky="w", columnspan=2)

        self.hash_type_label = ctk.CTkLabel(self.tabview.tab("Duplicate Finder"), text="Hash Type:")
        self.hash_type_label.grid(row=2, column=0, padx=20, pady=(10,0), sticky="w")
        self.hash_type_options = ['dhash', 'ahash', 'phash', 'whash']
        self.hash_type_var = ctk.StringVar(value=self.config_manager.get('DuplicateFinder', 'hash_type'))
        self.hash_type_dropdown = ctk.CTkOptionMenu(self.tabview.tab("Duplicate Finder"), values=self.hash_type_options, variable=self.hash_type_var, command=lambda val: self._update_config_setting('DuplicateFinder', 'hash_type', val))
        self.hash_type_dropdown.grid(row=3, column=0, padx=20, pady=(0,10), sticky="ew", columnspan=2)

        self.hash_threshold_label = ctk.CTkLabel(self.tabview.tab("Duplicate Finder"), text="Hash Threshold (0-255, lower is stricter):") # Clarified range
        self.hash_threshold_label.grid(row=4, column=0, padx=20, pady=(10,0), sticky="w", columnspan=2)
        self.hash_threshold_entry = ctk.CTkEntry(self.tabview.tab("Duplicate Finder"), width=100)
        self.hash_threshold_entry.grid(row=5, column=0, padx=20, pady=(0,10), sticky="w", columnspan=2)
        self.hash_threshold_entry.insert(0, str(self.config_manager.getint('DuplicateFinder', 'hash_threshold')))

        self.rebuild_cache_var = ctk.BooleanVar(value=self.config_manager.getboolean('DuplicateFinder', 'rebuild_hash_cache'))
        self.rebuild_cache_checkbox = ctk.CTkCheckBox(self.tabview.tab("Duplicate Finder"), text="Rebuild Hash Cache", variable=self.rebuild_cache_var, command=lambda: self._update_config_setting('DuplicateFinder', 'rebuild_hash_cache', self.rebuild_cache_var.get()))
        self.rebuild_cache_checkbox.grid(row=6, column=0, padx=20, pady=10, sticky="w", columnspan=2)

        self.hashes_cache_file_label = ctk.CTkLabel(self.tabview.tab("Duplicate Finder"), text="Hashes Cache File:")
        self.hashes_cache_file_label.grid(row=7, column=0, padx=20, pady=(10,0), sticky="w")
        self.hashes_cache_file_entry = ctk.CTkEntry(self.tabview.tab("Duplicate Finder"), width=250, placeholder_text="Path to hashes.txt")
        self.hashes_cache_file_entry.grid(row=8, column=0, padx=20, pady=(0,10), sticky="ew")
        self.hashes_cache_file_entry.insert(0, self.config_manager.get('Paths', 'image_hashes_cache_file'))
        self.hashes_cache_file_button = ctk.CTkButton(self.tabview.tab("Duplicate Finder"), text="Browse", command=lambda: self._browse_file(self.hashes_cache_file_entry, 'Paths', 'image_hashes_cache_file'))
        self.hashes_cache_file_button.grid(row=8, column=1, padx=20, pady=(0,10))

        self.duplicate_report_file_label = ctk.CTkLabel(self.tabview.tab("Duplicate Finder"), text="Duplicate Report File:")
        self.duplicate_report_file_label.grid(row=9, column=0, padx=20, pady=(10,0), sticky="w")
        self.duplicate_report_file_entry = ctk.CTkEntry(self.tabview.tab("Duplicate Finder"), width=250, placeholder_text="Path to duplicate_images.txt")
        self.duplicate_report_file_entry.grid(row=10, column=0, padx=20, pady=(0,10), sticky="ew")
        self.duplicate_report_file_entry.insert(0, self.config_manager.get('Paths', 'duplicate_report_file'))
        self.duplicate_report_file_button = ctk.CTkButton(self.tabview.tab("Duplicate Finder"), text="Browse", command=lambda: self._browse_file(self.duplicate_report_file_entry, 'Paths', 'duplicate_report_file'))
        self.duplicate_report_file_button.grid(row=10, column=1, padx=20, pady=(0,10))

        # --- Duplicate Action Settings ---
        self.enable_duplicate_actions_var = ctk.BooleanVar(value=self.config_manager.getboolean('DuplicateFinder', 'enable_duplicate_actions'))
        self.enable_duplicate_actions_checkbox = ctk.CTkCheckBox(self.tabview.tab("Duplicate Finder"), text="Enable Automatic Duplicate Actions (Move/Copy)", variable=self.enable_duplicate_actions_var, command=lambda: self._update_config_setting('DuplicateFinder', 'enable_duplicate_actions', self.enable_duplicate_actions_var.get()))
        self.enable_duplicate_actions_checkbox.grid(row=11, column=0, padx=20, pady=(10,5), sticky="w", columnspan=2)

        self.duplicate_action_type_label = ctk.CTkLabel(self.tabview.tab("Duplicate Finder"), text="Action for Duplicates:")
        self.duplicate_action_type_label.grid(row=12, column=0, padx=20, pady=(5,0), sticky="w")
        self.duplicate_action_type_options = ['none', 'move', 'copy']
        self.duplicate_action_type_var = ctk.StringVar(value=self.config_manager.get('DuplicateFinder', 'duplicate_action_type'))
        self.duplicate_action_type_dropdown = ctk.CTkOptionMenu(self.tabview.tab("Duplicate Finder"), values=self.duplicate_action_type_options, variable=self.duplicate_action_type_var, command=lambda val: self._update_config_setting('DuplicateFinder', 'duplicate_action_type', val))
        self.duplicate_action_type_dropdown.grid(row=13, column=0, padx=20, pady=(0,10), sticky="ew", columnspan=2)

        self.duplicate_action_dir_label = ctk.CTkLabel(self.tabview.tab("Duplicate Finder"), text="Duplicate Action Directory:")
        self.duplicate_action_dir_label.grid(row=14, column=0, padx=20, pady=(10,0), sticky="w")
        self.duplicate_action_dir_entry = ctk.CTkEntry(self.tabview.tab("Duplicate Finder"), width=250, placeholder_text="Select folder for moved/copied duplicates")
        self.duplicate_action_dir_entry.grid(row=15, column=0, padx=20, pady=(0,10), sticky="ew")
        self.duplicate_action_dir_entry.insert(0, self.config_manager.get('Paths', 'duplicate_action_directory'))
        self.duplicate_action_dir_button = ctk.CTkButton(self.tabview.tab("Duplicate Finder"), text="Browse", command=lambda: self._browse_directory(self.duplicate_action_dir_entry, 'Paths', 'duplicate_action_directory'))
        self.duplicate_action_dir_button.grid(row=15, column=1, padx=20, pady=(0,10))

        # --- Delete Button (Separate for Safety) ---
        self.delete_duplicates_button = ctk.CTkButton(self.tabview.tab("Duplicate Finder"), text="DELETE ALL FLAGGED DUPLICATES (IRREVERSIBLE)", fg_color="red", hover_color="darkred", command=self._start_duplicate_deletion_thread)
        self.delete_duplicates_button.grid(row=16, column=0, padx=20, pady=20, columnspan=2)


        # --- Tools & Settings Tab (for editing target_resolution_X_Y) ---
        self.tabview.tab("Tools & Settings").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Tools & Settings").grid_rowconfigure(1, weight=1) # Scrollable frame

        self.save_settings_button = ctk.CTkButton(self.tabview.tab("Tools & Settings"), text="Save All Current Settings", command=self._save_all_settings)
        self.save_settings_button.grid(row=0, column=0, padx=20, pady=10)

        # Add search bar for Aspect Ratio Targets
        self.ar_search_var = ctk.StringVar()
        self.ar_search_entry = ctk.CTkEntry(self.tabview.tab("Tools & Settings"), width=300, placeholder_text="Search aspect ratio...", textvariable=self.ar_search_var)
        self.ar_search_entry.grid(row=1, column=0, padx=20, pady=(0, 5), sticky="ew")
        self.ar_search_var.trace_add('write', lambda *args: self._populate_ar_settings(self.ar_search_var.get()))

        self.scrollable_frame = ctk.CTkScrollableFrame(self.tabview.tab("Tools & Settings"), label_text="Aspect Ratio Targets")
        self.scrollable_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self._ar_option_menus = {} # To store references to CTkOptionMenu widgets

        self._populate_ar_settings() # Populate the scrollable frame with AR settings

        # Enable mouse wheel scrolling for the Aspect Ratio Targets scrollable frame
        def _on_mousewheel(event):
            # For Windows and MacOS
            self.scrollable_frame._parent_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        def _on_mousewheel_linux(event):
            # For Linux (event.num 4=up, 5=down)
            if event.num == 4:
                self.scrollable_frame._parent_canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.scrollable_frame._parent_canvas.yview_scroll(1, "units")
        # Bind mouse wheel events
        self.scrollable_frame._parent_canvas.bind_all("<MouseWheel>", _on_mousewheel)
        self.scrollable_frame._parent_canvas.bind_all("<Button-4>", _on_mousewheel_linux)
        self.scrollable_frame._parent_canvas.bind_all("<Button-5>", _on_mousewheel_linux)

        # --- About Tab ---
        self.tabview.tab("About").grid_columnconfigure(0, weight=1)
        self.tabview.tab("About").grid_rowconfigure(0, weight=1)
        self.about_textbox = ctk.CTkTextbox(self.tabview.tab("About"), wrap="word", corner_radius=10, activate_scrollbars=True)
        self.about_textbox.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.about_textbox.insert("end", self.ABOUT_TEXT)
        self.about_textbox.configure(state="disabled")

        # --- License Tab ---
        self.tabview.tab("License").grid_columnconfigure(0, weight=1)
        self.tabview.tab("License").grid_rowconfigure(0, weight=1)
        self.license_textbox = ctk.CTkTextbox(self.tabview.tab("License"), wrap="word", corner_radius=10, activate_scrollbars=True)
        self.license_textbox.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.license_textbox.insert("end", self.GPL_LICENSE_TEXT)
        self.license_textbox.configure(state="disabled")


    def _load_gpl_license_text(self) -> str:
        """Loads the GPL license text from the LICENSE file."""
        # Prioritize finding LICENSE relative to the current script or main.py
        # assuming it's in the project root.
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.join(script_dir, '..') # Assumes gui is in project_root/gui
        license_file_path = os.path.join(project_root, 'LICENSE')

        # Fallback if the direct path doesn't work (unlikely if structure is standard)
        if not os.path.exists(license_file_path):
            # Removed self._log_message call here
            return "License file (LICENSE) not found. Please ensure it's in the project root directory.\n\n" \
                   "This software is licensed under the GNU General Public License v3.0.\n" \
                   "A copy of the license is available at https://www.gnu.org/licenses/gpl-3.0.html"

        try:
            with open(license_file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            # Removed self._log_message call here
            return f"Error loading license text: {e}"


    def _browse_directory(self, entry_widget: ctk.CTkEntry, config_section: str, config_option: str):
        directory = filedialog.askdirectory()
        if directory:
            entry_widget.delete(0, ctk.END)
            entry_widget.insert(0, directory)
            self._update_config_setting(config_section, config_option, directory)

    def _browse_file(self, entry_widget: ctk.CTkEntry, config_section: str, config_option: str):
        file_path = filedialog.askopenfilename()
        if file_path:
            entry_widget.delete(0, ctk.END)
            entry_widget.insert(0, file_path)
            self._update_config_setting(config_section, config_option, file_path)

    def _toggle_custom_resolution_fields(self):
        is_checked = self.override_custom_var.get()
        state = "normal" if is_checked else "disabled"
        self.custom_width_entry.configure(state=state)
        self.custom_height_entry.configure(state=state)
        self.custom_width_label.configure(state=state)
        self.custom_height_label.configure(state=state)
        # Update config immediately
        self._update_config_setting('ImageSettings', 'override_to_custom_resolution', is_checked)
        # Also, grey out / enable fallback goal if override is toggled
        self.fallback_goal_dropdown.configure(state="disabled" if is_checked else "normal")
        self.fallback_goal_label.configure(state="disabled" if is_checked else "normal")


    def _update_config_setting(self, section: str, option: str, value: Any):
        """Updates a single setting in the ConfigManager and saves."""
        try:
            self.config_manager.set(section, option, str(value))
            self._log_message(f"Config updated: [{section}]{option} = {value}")
        except Exception as e:
            messagebox.showerror("Config Error", f"Failed to save setting {option}: {e}")
            self._log_message(f"ERROR: Failed to save config setting {option}: {e}")

    def _save_all_settings(self):
        """Saves all settings from the GUI fields back to the config."""
        try:
            # Paths
            self._update_config_setting('Paths', 'input_directory', self.input_dir_entry.get())
            self._update_config_setting('Paths', 'output_directory', self.output_dir_entry.get())
            self._update_config_setting('Paths', 'scanner_output_directory', self.scanner_output_dir_entry.get())
            self._update_config_setting('Paths', 'exclusion_reference_file', self.exclusion_file_entry.get())
            self._update_config_setting('Paths', 'master_definitions_file', self.master_defs_file_entry.get())
            self._update_config_setting('Paths', 'image_hashes_cache_file', self.hashes_cache_file_entry.get())
            self._update_config_setting('Paths', 'duplicate_report_file', self.duplicate_report_file_entry.get())
            self._update_config_setting('Paths', 'duplicate_action_directory', self.duplicate_action_dir_entry.get())

            # ImageSettings
            self._update_config_setting('ImageSettings', 'override_to_custom_resolution', self.override_custom_var.get())
            self._update_config_setting('ImageSettings', 'custom_width', self.custom_width_entry.get())
            self._update_config_setting('ImageSettings', 'custom_height', self.custom_height_entry.get())
            self._update_config_setting('ImageSettings', 'output_extension', self.output_ext_var.get())
            self._update_config_setting('ImageSettings', 'fallback_resolution_goal', self.fallback_goal_var.get())

            # Renaming
            self._update_config_setting('Renaming', 'enable_random_rename', self.rename_var.get())

            # Scanner
            self._update_config_setting('Scanner', 'enable_exclusion_reference', self.exclusion_var.get())
            self._update_config_setting('Scanner', 'merge_to_master_definitions', self.merge_master_var.get())

            # DuplicateFinder
            self._update_config_setting('DuplicateFinder', 'enable_duplicate_detection', self.enable_duplicate_var.get())
            self._update_config_setting('DuplicateFinder', 'hash_type', self.hash_type_var.get())
            self._update_config_setting('DuplicateFinder', 'hash_threshold', self.hash_threshold_entry.get())
            self._update_config_setting('DuplicateFinder', 'rebuild_hash_cache', self.rebuild_cache_var.get())
            self._update_config_setting('DuplicateFinder', 'duplicate_action_type', self.duplicate_action_type_var.get())
            self._update_config_setting('DuplicateFinder', 'enable_duplicate_actions', self.enable_duplicate_actions_var.get())


            # Aspect Ratio Specific Targets
            for ar_str, var in self._ar_option_menus.items():
                config_key = f"target_resolution_{ar_str.replace(':', '_').replace('.', '_')}"
                self._update_config_setting('ImageSettings', config_key, var.get())

            messagebox.showinfo("Settings Saved", "All settings have been saved to config.ini.")
            self._log_message("All GUI settings saved to config.ini.")
        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving settings: {e}")
            self._log_message(f"ERROR: An error occurred during saving: {e}")


    def _populate_ar_settings(self, filter_text: str = ""):
        """Populates the scrollable frame with Aspect Ratio Target settings, filtered by search."""
        # Clear existing widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self._ar_option_menus = {} # Reset storage

        # Dynamically import COMMON_RESOLUTIONS_DEFINITIONS here
        resolution_definitions_path = "" # Initialize here to prevent unbound variable warning
        try:
            resolution_definitions_path = self.config_manager.get('Paths', 'master_definitions_file')
            CurrentResolutionDefs = {} # Initialize as empty

            if os.path.exists(resolution_definitions_path):
                spec = importlib.util.spec_from_file_location("resolution_definitions", resolution_definitions_path)
                if spec and spec.loader:
                    resolution_definitions_module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(resolution_definitions_module)
                    CurrentResolutionDefs = resolution_definitions_module.COMMON_RESOLUTIONS_DEFINITIONS
                else:
                    self._log_message(f"ERROR: Could not load module spec or loader for {resolution_definitions_path}.")
            else:
                self._log_message(f"WARNING: Resolution definitions file not found at {resolution_definitions_path}. Aspect Ratio Targets dropdowns might be empty.")

        except Exception as e:
            self._log_message(f"ERROR: Failed to dynamically import COMMON_RESOLUTIONS_DEFINITIONS for GUI from {resolution_definitions_path}: {e}. AR settings dropdowns might be empty.")
            CurrentResolutionDefs = {} # Fallback to empty dict

        sorted_ar_keys = sorted(CurrentResolutionDefs.keys(),
                                key=lambda x: (float(x.split(':')[0]) / float(x.split(':')[1])
                                               if float(x.split(':')[1]) != 0 else float('inf')))

        # Filter aspect ratios by search text
        if filter_text:
            sorted_ar_keys = [ar for ar in sorted_ar_keys if filter_text.lower() in ar.lower()]

        row_num = 0
        for ar_str in sorted_ar_keys:
            levels = CurrentResolutionDefs.get(ar_str, {})
            if not levels:
                continue

            config_key_lookup = f"target_resolution_{ar_str.replace(':', '_').replace('.', '_')}"
            current_value = self.config_manager.get('ImageSettings', config_key_lookup, fallback="")

            if current_value not in levels:
                if levels:
                    current_value = list(levels.keys())[0]
                else:
                    current_value = "N/A"


            label = ctk.CTkLabel(self.scrollable_frame, text=f"Target {ar_str}:")
            label.grid(row=row_num, column=0, padx=5, pady=2, sticky="w")

            option_values = list(levels.keys()) if levels else ["No Options"]
            var = ctk.StringVar(value=current_value)

            dropdown = ctk.CTkOptionMenu(self.scrollable_frame, values=option_values, variable=var,
                                        command=lambda val, ar=ar_str: self._update_config_setting('ImageSettings', f"target_resolution_{ar.replace(':', '_').replace('.', '_')}", val))
            dropdown.grid(row=row_num, column=1, padx=5, pady=2, sticky="ew")

            # Debug: Log the available options for each aspect ratio
            # self._log_message(f"Aspect Ratio {ar_str} options: {option_values}")

            self._ar_option_menus[ar_str] = var

            row_num += 1


    def _log_message(self, message: str):
        """Appends a message to the console output textbox."""
        self.console_output.configure(state="normal")
        self.console_output.insert("end", message + "\n")
        self.console_output.see("end")
        self.console_output.configure(state="disabled")

    def _set_all_buttons_state(self, state: str):
        """Helper to set the state of main operation buttons."""
        self.process_button.configure(state=state)
        self.scan_button.configure(state=state)
        self.duplicate_button.configure(state=state)
        self.delete_duplicates_button.configure(state=state)

    def _start_image_processing_thread(self):
        """Starts image processing in a separate thread to keep GUI responsive."""
        self._log_message("Starting image processing...")
        self._save_all_settings()

        latest_config_manager = ConfigManager()
        processor = ImageProcessor(latest_config_manager)

        self._set_all_buttons_state("disabled")

        threading.Thread(target=self._run_processing_task, args=(processor,)).start()

    def _run_processing_task(self, processor: ImageProcessor):
        """Task to run image processing."""
        try:
            processed_count = processor.process_images()
            self.after(0, lambda: messagebox.showinfo("Processing Complete", f"Successfully processed {processed_count} images."))
            self._log_message(f"Image processing finished. Processed {processed_count} images.")
        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Processing Error", f"An error occurred during image processing: {e}"))
            self._log_message(f"ERROR during image processing: {e}")
        finally:
            self.after(0, lambda: self._set_all_buttons_state("normal"))

    def _start_image_scanning_thread(self):
        """Starts image scanning in a separate thread to keep GUI responsive."""
        self._log_message("Starting image scanning and report generation...")
        self._save_all_settings()

        latest_config_manager = ConfigManager()
        scanner = ImageScanner(latest_config_manager)

        self._set_all_buttons_state("disabled")

        threading.Thread(target=self._run_scanning_task, args=(scanner,)).start()

    def _run_scanning_task(self, scanner: ImageScanner):
        """Task to run image scanning."""
        try:
            scanner.scan_images()
            self.after(0, lambda: messagebox.showinfo("Scanning Complete", "Image scanning and report generation finished."))
            self._log_message("Image scanning and report generation finished.")

            if scanner.merge_to_master_definitions:
                self.after(0, self._populate_ar_settings)
                self._log_message("Aspect Ratio Targets in GUI refreshed from updated master definitions file.")

        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Scanning Error", f"An error occurred during image scanning: {e}"))
            self._log_message(f"ERROR during image scanning: {e}")
        finally:
            self.after(0, lambda: self._set_all_buttons_state("normal"))

    def _start_duplicate_finder_thread(self):
        """Starts duplicate image finding in a separate thread, with optional action."""
        self._log_message("Starting image processing...")
        self._save_all_settings()

        latest_config_manager = ConfigManager()
        finder = DuplicateFinder(latest_config_manager)

        self._set_all_buttons_state("disabled")

        if not latest_config_manager.getboolean('DuplicateFinder', 'enable_duplicate_detection'):
            self.after(0, lambda: messagebox.showwarning("Feature Disabled", "Duplicate Detection is disabled in config. Please enable it to run."))
            self._log_message("Duplicate Detection skipped: Feature is disabled in config.")
            self.after(0, lambda: self._set_all_buttons_state("normal"))
            return

        threading.Thread(target=self._run_duplicate_finder_task, args=(finder,)).start()

    def _run_duplicate_finder_task(self, finder: DuplicateFinder):
        """Task to run duplicate image finding and optionally perform actions."""
        try:
            duplicates_found = finder.find_duplicates()
            self.after(0, lambda: self._log_message(f"Found {len(duplicates_found)} duplicate/near-duplicate image pairs. Report saved to {os.path.abspath(finder.duplicate_report_file)}"))

            # Store found duplicates for potential later deletion
            self._found_duplicate_pairs = duplicates_found

            # Perform action (move/copy) if enabled and configured
            if finder.enable_duplicate_actions and finder.duplicate_action_type != 'none':
                action_type = finder.duplicate_action_type
                action_count = finder.perform_duplicate_action(duplicates_found, action_type)
                self.after(0, lambda: messagebox.showinfo("Duplicate Action Complete",
                                                          f"Finished finding duplicates. Also, {action_count} files were {action_type}d to {os.path.abspath(finder.duplicate_action_directory)}. Report saved to {os.path.abspath(finder.duplicate_report_file)}"))
                self._log_message(f"Duplicate action '{action_type}' performed on {action_count} files.")
            else:
                self.after(0, lambda: messagebox.showinfo("Duplicate Detection Complete", f"Found {len(duplicates_found)} duplicate/near-duplicate image pairs. Report saved to {os.path.abspath(finder.duplicate_report_file)}"))

        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Duplicate Detection Error", f"An error occurred during duplicate detection: {e}"))
            self._log_message(f"ERROR during duplicate detection: {e}")
        finally:
            self.after(0, lambda: self._set_all_buttons_state("normal"))

    def _start_duplicate_deletion_thread(self):
        """Initiates the deletion process for detected duplicates after confirmation."""
        if not self._found_duplicate_pairs:
            messagebox.showwarning("No Duplicates to Delete", "Please run 'Find Duplicate Images' first to identify duplicates.")
            self._log_message("Deletion skipped: No duplicates found from last scan.")
            return

        # Prepare a list of files to delete (all second files from the pairs)
        files_to_delete = [pair[1] for pair in self._found_duplicate_pairs]
        if not files_to_delete:
            messagebox.showwarning("No Duplicates to Delete", "No duplicate files were identified for deletion from the last scan.")
            self._log_message("Deletion skipped: No duplicate files identified for deletion.")
            return

        # Show a confirmation dialog
        confirm = messagebox.askyesno(
            "Confirm Permanent Deletion",
            f"You are about to PERMANENTLY DELETE {len(files_to_delete)} duplicate image files from your input directory.\n\n"
            "THIS ACTION IS IRREVERSIBLE!\n\n"
            "Do you wish to proceed?"
        )

        if confirm:
            self._log_message("Starting permanent deletion of duplicates...")
            self._set_all_buttons_state("disabled")
            latest_config_manager = ConfigManager() # Get latest config
            finder = DuplicateFinder(latest_config_manager) # Initialize finder with potentially updated paths
            threading.Thread(target=self._run_duplicate_deletion_task, args=(finder, files_to_delete)).start()
        else:
            self._log_message("Deletion cancelled by user.")

    def _run_duplicate_deletion_task(self, finder: DuplicateFinder, files_to_delete: List[str]):
        """Task to perform actual deletion of duplicate files."""
        try:
            deleted_count = finder.delete_duplicates(files_to_delete)
            self.after(0, lambda: messagebox.showinfo("Deletion Complete", f"Successfully DELETED {deleted_count} duplicate files."))
            self._log_message(f"Permanent deletion finished. DELETED {deleted_count} files.")
            # Clear the stored duplicates after deletion to prevent accidental re-deletion
            self._found_duplicate_pairs = []
        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Deletion Error", f"An error occurred during deletion: {e}"))
            self._log_message(f"ERROR during deletion: {e}")
        finally:
            self.after(0, lambda: self._set_all_buttons_state("normal"))
