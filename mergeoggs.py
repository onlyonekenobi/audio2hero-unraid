from pydub import AudioSegment


def merge(out_dir, *files):
    if len(files)==0:
        raise ValueError("No files to merge")
    # Auto-detect format for first file
    combined = AudioSegment.from_file(files[0])
    for file in files[1:]:
        # Auto-detect format for subsequent files
        sound = AudioSegment.from_file(file)
        combined = combined.overlay(sound)
    # Export as OGG for Clone Hero compatibility
    combined.export(out_dir, format="ogg")

if __name__ == "__main__":
    merge("merged.ogg","guitar.ogg", "bass.ogg", "song.ogg")
    