# MP3 & M4A Metadata Updater

A Python-based tool with GUI for bulk-editing metadata tags for MP3 and M4A audio files, specifically designed for Stop'n'Time jazz recordings.

## Features

- **Cross-Platform Support**: Works on both Windows (PC) and macOS
- **Batch Processing**: Automatically updates multiple audio files at once
- **Supported Formats**: MP3 (`.mp3`) and M4A (`.m4a`) files
- **Automatic Metadata Extraction**: Parses filenames in format `SongTitle_YYYY-MMDD.mp3`
- **User-Friendly GUI**: Simple interface built with `tkinter`

## Metadata Fields

The tool automatically updates the following metadata:

- **Title**: Extracted from filename (e.g., `FavoriteThings_2024-1122`)
- **Artist**: Set to "Stop'n'Time"
- **Album**: Formatted date (e.g., "22 Nov 2024")
- **Year**: Extracted from filename
- **Genre**: Set to "Jazz"

## Versions

This repository contains two versions:

- **`gui_mp3_m4a_metadata_updater.py`** - Original PC/Windows version
- **`gui_mp3_m4a_metadata_updater_mac.py`** - macOS-optimized version with:
  - Native macOS UI styling
  - Improved window layout and spacing
  - Better visual feedback with status symbols
  - Mac-friendly fonts (Helvetica, Monaco)

## Installation

### Prerequisites

- Python 3.8 or higher
- `mutagen` library

### Setup

1. **Clone the repository**:
   ```bash
   git clone git@github.com:julspetersburg/mp3updater.git
   cd mp3updater
   ```

2. **Install dependencies**:
   ```bash
   # Windows/Linux
   pip install mutagen
   
   # macOS
   pip3 install mutagen
   ```

## Usage

### Running the Application

**On Windows:**
```bash
python gui_mp3_m4a_metadata_updater.py
```

**On macOS:**
```bash
python3 gui_mp3_m4a_metadata_updater_mac.py
```

### Using the GUI

1. Click **"Select Directory"**
2. Choose a folder containing your MP3/M4A files
3. The tool will process all compatible files automatically
4. Check the log window for results

### File Naming Convention

Files must follow this naming pattern:
```
SongTitle_YYYY-MMDD.mp3
```

**Examples:**
- `FavoriteThings_2024-1122.mp3`
- `TakeFive_2024-0315.m4a`

## Building Executables

The repository includes `.spec` files for building standalone executables with PyInstaller:

```bash
pyinstaller gui_mp3_m4a_metadata_updater.spec
```

Executables will be created in the `dist/` folder.

## Project Structure

```
mp3updater/
├── gui_mp3_m4a_metadata_updater.py       # Windows/PC version
├── gui_mp3_m4a_metadata_updater_mac.py   # macOS version
├── gui_mp3_m4a_metadata_updater.spec     # PyInstaller spec file
├── build/                                 # Build artifacts
├── dist/                                  # Compiled executables
└── README.md                              # This file
```

## Technologies Used

- **Python 3.8+**
- **mutagen** - Audio metadata manipulation
- **tkinter** - Cross-platform GUI framework
- **PyInstaller** - Executable packaging

## Development

Developed using PyCharm IDE.

## License

This project is for personal/organizational use for Stop'n'Time jazz recordings.

## Author

Julia (julspetersburg)

## Contributing

This is a personal project for specific use cases. Feel free to fork and adapt for your needs!