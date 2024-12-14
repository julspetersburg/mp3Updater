# MP3 & M4A Metadata Updater GUI

## Project Description
The **MP3 & M4A Metadata Updater GUI** is a Python-based tool designed to streamline the process of bulk-editing metadata (tags) for MP3 and M4A files. The tool uses a graphical user interface (GUI) to make metadata updates simple and efficient for users, even without programming knowledge.

## Features
- **Batch Processing**: Automatically updates multiple MP3 and M4A files at once.
- **Supported File Formats**: `.mp3` and `.m4a`.
- **Metadata Fields**:
  - **Title**: Extracted from the file name.
  - **Contributing Artists**: Predefined as "Stop'n'Time".
  - **Album**: Automatically formatted based on the file's date (e.g., "13 Dec 2024").
  - **Year**: Extracted from the file name.
  - **Genre**: Predefined as "Jazz".
- **User-Friendly Interface**: Simple GUI built with `tkinter`.
- **Customizable**: Can be modified to suit different metadata needs.

## Technologies Used
- **Python**:
  - Core programming language.
  - Libraries: `mutagen` (for MP3/M4A metadata editing), `tkinter` (for the GUI).
- **PyCharm**: Development IDE.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher installed.
- `mutagen` library installed:

