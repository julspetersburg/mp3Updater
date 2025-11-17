import os
import sys
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from datetime import datetime
from tkinter import Tk, Label, Button, filedialog, Text, Scrollbar, END, Frame
from tkinter import ttk

# Define static metadata
PRESET_METADATA = {
    "artist": "Stop'n'Time",  # Static contributing artist
    "genre": "Jazz",  # Static genre
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
        return f"✓ Metadata updated for: {os.path.basename(file_path)}"
    except Exception as e:
        return f"✗ Failed to update metadata for {os.path.basename(file_path)}: {e}"


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
        return f"✓ Metadata updated for: {os.path.basename(file_path)}"
    except Exception as e:
        return f"✗ Failed to update metadata for {os.path.basename(file_path)}: {e}"


def bulk_update_metadata(directory, log_display):
    """
    Process all MP3 and M4A files in the given directory.
    """
    files_processed = 0
    files_skipped = 0

    log_display.insert(END, f"\n{'=' * 60}\n")
    log_display.insert(END, f"Processing directory: {directory}\n")
    log_display.insert(END, f"{'=' * 60}\n\n")

    for file in sorted(os.listdir(directory)):
        message = None
        if file.endswith(".mp3") or file.endswith(".m4a"):
            file_path = os.path.join(directory, file)
            metadata = extract_metadata_from_filename(file)
            if metadata:
                if file.endswith(".mp3"):
                    message = update_mp3_metadata(file_path, metadata)
                elif file.endswith(".m4a"):
                    message = update_m4a_metadata(file_path, metadata)
                files_processed += 1
            else:
                message = f"⊘ Skipped (invalid filename format): {file}"
                files_skipped += 1
        else:
            message = f"⊘ Skipped (unsupported format): {file}"
            files_skipped += 1

        if message:
            log_display.insert(END, message + "\n")
            log_display.see(END)
            log_display.update()

    log_display.insert(END, f"\n{'=' * 60}\n")
    log_display.insert(END, f"Complete! Processed: {files_processed} | Skipped: {files_skipped}\n")
    log_display.insert(END, f"{'=' * 60}\n\n")
    log_display.see(END)


def select_directory(log_display):
    """
    Open a dialog to select the directory.
    """
    directory = filedialog.askdirectory(title="Select Directory with MP3/M4A Files")
    if directory:
        log_display.insert(END, f"\n➤ Selected directory: {directory}\n")
        log_display.see(END)
        bulk_update_metadata(directory, log_display)


def create_gui():
    """
    Create the GUI with macOS-friendly styling.
    """
    root = Tk()
    root.title("MP3 & M4A Metadata Updater")
    root.geometry("800x600")

    # macOS-specific adjustments
    if sys.platform == "darwin":
        try:
            # Make it look more native on macOS
            root.tk.call('tk', 'scaling', 1.4)
        except:
            pass

    # Main container with padding
    main_frame = Frame(root, padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)

    # Header
    header_label = Label(main_frame, text="MP3 & M4A Metadata Updater",
                         font=("Helvetica", 18, "bold"))
    header_label.pack(pady=(0, 5))

    subtitle_label = Label(main_frame,
                           text="Updates metadata for Stop'n'Time jazz recordings",
                           font=("Helvetica", 11))
    subtitle_label.pack(pady=(0, 20))

    # Instructions
    instructions = Label(main_frame,
                         text="Select a folder containing MP3 or M4A files with names like: SongTitle_2024-1122.mp3",
                         font=("Helvetica", 11),
                         wraplength=700,
                         justify="left")
    instructions.pack(pady=(0, 15))

    # Button frame
    button_frame = Frame(main_frame)
    button_frame.pack(pady=(0, 15))

    select_btn = Button(button_frame,
                        text="Select Directory",
                        command=lambda: select_directory(log_display),
                        font=("Helvetica", 12),
                        bg="#007AFF" if sys.platform != "darwin" else "SystemButtonFace",
                        fg="white" if sys.platform != "darwin" else "black",
                        padx=20,
                        pady=8,
                        relief="flat" if sys.platform == "darwin" else "raised")
    select_btn.pack()

    # Log display frame with scrollbar
    log_frame = Frame(main_frame)
    log_frame.pack(fill="both", expand=True, pady=(0, 15))

    scrollbar = Scrollbar(log_frame)
    scrollbar.pack(side="right", fill="y")

    log_display = Text(log_frame,
                       wrap="word",
                       yscrollcommand=scrollbar.set,
                       font=("Monaco" if sys.platform == "darwin" else "Courier", 10),
                       bg="#F5F5F5",
                       relief="solid",
                       borderwidth=1)
    log_display.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=log_display.yview)

    # Initial message
    log_display.insert(END, "Welcome! Click 'Select Directory' to begin.\n")
    log_display.insert(END, f"\nPreset metadata:\n")
    log_display.insert(END, f"  Artist: {PRESET_METADATA['artist']}\n")
    log_display.insert(END, f"  Genre: {PRESET_METADATA['genre']}\n\n")

    # Quit button
    quit_btn = Button(main_frame,
                      text="Quit",
                      command=root.quit,
                      font=("Helvetica", 11),
                      padx=15,
                      pady=5)
    quit_btn.pack()

    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    # Run the GUI loop
    root.mainloop()


if __name__ == "__main__":
    create_gui()