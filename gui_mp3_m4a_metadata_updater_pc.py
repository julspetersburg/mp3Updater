import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from datetime import datetime
from tkinter import Tk, Label, Button, filedialog, Text, Scrollbar, END

# Define static metadata
PRESET_METADATA = {
    "artist": "Stop'n'Time",  # Static contributing artist
    "genre": "Jazz",  # Static genre 2
}


def format_date(date_str):
    """
    Convert date in 'YYYY-MMDD' format to 'DD MMM YYYY'.
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m%d")
        formatted_date = date_obj.strftime("%d %b %Y")  # '22 Nov 2024'
        year = date_obj.strftime("%Y")  # '2024'
        return formatted_date, year
    except ValueError:
        return None, None


def extract_metadata_from_filename(filename):
    """
    Extract metadata from filenames like 'FavoriteThings_2024-1122.mp3'.
    """
    try:
        name_part = os.path.splitext(filename)[0]  # Remove file extension
        title, date_str = name_part.split("_")  # Split by the underscore
        formatted_date, year = format_date(date_str)
        if formatted_date and year:
            return {"title": name_part, "album": formatted_date, "year": year}
        else:
            return None
    except ValueError:
        return None


def update_mp3_metadata(file_path, metadata):
    """
    Update MP3 metadata.
    """
    try:
        # Load MP3 file
        audio = MP3(file_path, ID3=EasyID3)

        # Apply extracted metadata
        if metadata.get("title"):
            audio["title"] = metadata["title"]
        if metadata.get("album"):
            audio["album"] = metadata["album"]
        if metadata.get("year"):
            audio["date"] = metadata["year"]

        # Apply preset metadata
        for key, value in PRESET_METADATA.items():
            audio[key] = value

        # Save changes
        audio.save()
        return f"Metadata updated for: {file_path}"
    except Exception as e:
        return f"Failed to update metadata for {file_path}: {e}"


def update_m4a_metadata(file_path, metadata):
    """
    Update M4A metadata.
    """
    try:
        # Load M4A file
        audio = MP4(file_path)

        # Apply extracted metadata
        if metadata.get("title"):
            audio["\xa9nam"] = metadata["title"]  # Title
        if metadata.get("album"):
            audio["\xa9alb"] = metadata["album"]  # Album
        if metadata.get("year"):
            audio["\xa9day"] = metadata["year"]  # Year

        # Apply preset metadata
        if "artist" in PRESET_METADATA:
            audio["\xa9ART"] = PRESET_METADATA["artist"]  # Artist
        if "genre" in PRESET_METADATA:
            audio["\xa9gen"] = PRESET_METADATA["genre"]  # Genre

        # Save changes
        audio.save()
        return f"Metadata updated for: {file_path}"
    except Exception as e:
        return f"Failed to update metadata for {file_path}: {e}"


def bulk_update_metadata(directory, log_display):
    """
    Process all MP3 and M4A files in the given directory.
    """
    for file in os.listdir(directory):
        message = None  # Initialize 'message' to avoid referencing it before assignment
        if file.endswith(".mp3") or file.endswith(".m4a"):
            file_path = os.path.join(directory, file)
            metadata = extract_metadata_from_filename(file)
            if metadata:
                if file.endswith(".mp3"):
                    message = update_mp3_metadata(file_path, metadata)
                elif file.endswith(".m4a"):
                    message = update_m4a_metadata(file_path, metadata)
            else:
                message = f"Skipped file (invalid metadata): {file}"
        else:
            message = f"Skipped file (unsupported format): {file}"

        # Log the message if set
        if message:
            log_display.insert(END, message + "\n")
def select_directory(log_display):
    """
    Open a dialog to select the directory.
    """
    directory = filedialog.askdirectory()
    if directory:
        log_display.insert(END, f"Selected directory: {directory}\n")
        bulk_update_metadata(directory, log_display)


# Create the GUI
def create_gui():
    root = Tk()
    root.title("MP3 & M4A Metadata Updater")

    # Labels
    Label(root, text="Metadata Updater", font=("Arial", 16)).pack(pady=10)
    Label(root, text="Select a directory containing MP3/M4A files:", font=("Arial", 12)).pack(pady=5)

    # Buttons
    Button(root, text="Select Directory", command=lambda: select_directory(log_display), width=20).pack(pady=10)

    # Log display with scrollbar
    log_frame = Scrollbar(root)
    log_frame.pack(side="right", fill="y")

    log_display = Text(root, wrap="word", yscrollcommand=log_frame.set, height=15, width=70)
    log_display.pack(padx=10, pady=10)
    log_frame.config(command=log_display.yview)

    Button(root, text="Quit", command=root.quit, width=10).pack(pady=10)

    # Run the GUI loop
    root.mainloop()


if __name__ == "__main__":
    create_gui()
