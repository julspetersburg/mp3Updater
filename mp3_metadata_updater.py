import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from datetime import datetime

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
        print(f"Error parsing date: {date_str}")
        return None, None


def extract_metadata_from_filename(filename):
    """
    Extract metadata from filenames like 'FavoriteThings_2024-1122.mp3'.
    """
    try:
        name_part = os.path.splitext(filename)[0]  # Remove '.mp3'
        title, date_str = name_part.split("_")  # Split by the underscore
        formatted_date, year = format_date(date_str)
        if formatted_date and year:
            return {"title": name_part, "album": formatted_date, "year": year}
        else:
            return None
    except ValueError:
        print(f"Filename format not recognized: {filename}")
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
        print(f"Metadata updated for: {file_path}")
    except Exception as e:
        print(f"Failed to update metadata for {file_path}: {e}")


def bulk_update_metadata(directory):
    """
    Process all MP3 files in the given directory.
    """
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            file_path = os.path.join(directory, file)
            metadata = extract_metadata_from_filename(file)
            if metadata:
                update_mp3_metadata(file_path, metadata)


# Main function
if __name__ == "__main__":
    # Specify the directory containing MP3 files
    mp3_directory = input("Enter the path to your MP3 directory: ")
    if os.path.isdir(mp3_directory):
        bulk_update_metadata(mp3_directory)
    else:
        print("Invalid directory. Please check the path.")
