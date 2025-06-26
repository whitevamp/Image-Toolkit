Image Toolkit
🚀 Overview

Image Toolkit is a versatile Python-based application designed to help you efficiently manage and organize your digital image collection with a user-friendly graphical interface. It's built to streamline common image-related tasks, from resizing and format conversion to advanced duplicate detection and cleanup.
✨ Key Features

    Image Processing:

        Batch resize images to custom dimensions or predefined aspect ratios (e.g., 16:9, 4:3, 1:1, etc.).

        Convert images to various output formats (JPG, PNG, WebP, BMP, TIFF).

        Option to randomly rename processed images for better organization.

    Image Scanning:

        Scan your input directories to generate detailed reports on image dimensions.

        Identify and report unique image resolutions.

        Option to merge newly found aspect ratios into a master definition file for future processing.

        Exclude specific image dimensions from scans based on a reference file.

    Duplicate Finder (Perceptual Hashing):

        Advanced Duplicate Detection: Identifies duplicate and near-duplicate images based on their visual content using various perceptual hashing algorithms (aHash, pHash, dHash, wHash).

        Configurable Thresholds: Adjust the sensitivity of duplicate detection using a Hamming distance threshold.

        Intelligent Caching: Caches image hashes to speed up subsequent scans, only reprocessing new or modified files.

        Automated Actions: Configurable options to automatically move or copy detected duplicate images to a specified archive directory.

        Permanent Deletion: A dedicated, irreversible delete option for flagged duplicates, with a prominent warning.

    User-Friendly GUI: Powered by CustomTkinter for a modern and intuitive desktop application experience.

    Configurable Settings: All paths and operational parameters are managed via a config.ini file, easily editable through the GUI.

📦 Installation

To get started with Image Toolkit, follow these steps:

    Clone the repository:

    git clone https://github.com/[YourGitHubUsername]/Image-Toolkit.git
    cd Image-Toolkit

    (Replace [YourGitHubUsername] with your actual GitHub username.)

    Create a virtual environment (recommended):

    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate

    Install dependencies:

    pip install -r requirements.txt

    (You will need to create requirements.txt if you haven't already. It should contain customtkinter, Pillow, imagehash.)
    A basic requirements.txt would look like this:

    customtkinter
    Pillow
    imagehash

🚀 Usage

    Run the application:

    python main.py

    Configure Paths and Settings:

        Upon first run, config.ini and necessary directories (input_images, output_processed_images, scan_reports, image_cache, duplicate_actions_archive) will be created.

        Adjust input/output directories and other settings directly within the GUI's various tabs or by editing config.ini manually.

        For duplicate detection, explore the "Duplicate Finder" tab to set hash type, threshold, and enable automatic actions.

    Perform Operations:

        Use the "Image Processing" tab to resize and convert your images.

        Use the "Image Scanning" tab to analyze your library and generate reports.

        Use the "Duplicate Finder" tab to find duplicates and manage them (move, copy, or delete).

📜 License

This project is licensed under the GNU General Public License v3.0 (GPLv3).

You are free to use, modify, and distribute this software under the terms of the GPLv3. Any derivative works or distributions must also be licensed under the GPLv3.

A copy of the full license text is included in the LICENSE file in this repository and is also accessible within the application's "License" tab.
🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

    Fork the repository.

    Create a new branch (git checkout -b feature/your-feature-name).

    Make your changes.

    Commit your changes (git commit -m 'Add new feature').

    Push to the branch (git push origin feature/your-feature-name).

    Open a Pull Request.

📧 Contact

For any questions or feedback, you can reach the author:

Author: whitevamp
GitHub: https://github.com/whitevamp
