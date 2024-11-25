# MP3 Metadata Updater GUI

## Project Description
The **MP3 Metadata Updater GUI** is a Python-based tool designed to streamline the process of bulk-editing metadata (tags) for MP3 files. The tool uses a graphical user interface (GUI) to make metadata updates simple and efficient for users, even without programming knowledge.

## Features
- **Batch Processing**: Automatically updates multiple MP3 files at once.
- **Metadata Fields**:
  - **Title**: Extracted from the file name.
  - **Contributing Artists**: Predefined as "Stop'n'Time".
  - **Album**: Automatically formatted based on the file's date (e.g., "22 Nov 2024").
  - **Year**: Extracted from the file name.
  - **Genre**: Predefined as "Jazz".
- **User-Friendly Interface**: Simple GUI built with `tkinter`.
- **Customizable**: Can be modified to suit different metadata needs.

## Technologies Used
- **Python**:
  - Core programming language.
  - Libraries: `mutagen` (for MP3 metadata editing), `tkinter` (for the GUI).
- **PyCharm**: Development IDE.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher installed.
- `mutagen` library installed:

## License
This project is licensed under the MIT License. 

## Acknowledgments
Thanks to the developers of the mutagen library for making metadata editing simple.
Inspired by my need for an easy-to-use MP3 metadata bulk editing tool.  
