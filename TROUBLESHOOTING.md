# Audio2Hero Troubleshooting Guide

## Common Errors and Solutions

### Error: "cannot find sync word" / "invalid data found when processing input"

**Cause:** The audio file format is not being detected correctly, or the file is corrupted/incompatible.

**Solutions:**

1. **Check your audio file format:**
   - Supported formats: MP3, WAV, FLAC, M4A, AAC, OGG
   - Try converting your file to MP3 or WAV first

2. **Convert your audio file:**
   ```bash
   # In WSL, if you have ffmpeg installed:
   ffmpeg -i "input_file.m4a" -acodec libmp3lame "output.mp3"
   ```

3. **Check file integrity:**
   - Make sure the file isn't corrupted
   - Try playing it in a media player first
   - Re-download or re-export the file if needed

4. **File naming:**
   - Make sure the filename doesn't have special characters that cause issues
   - Try renaming to something simple like "song.mp3"

### Error: "FileNotFoundError: ffprobe"

**Solution:** Install FFmpeg in WSL:
```bash
sudo apt update
sudo apt install -y ffmpeg
```

### Error: "ImportError: essentia"

**Solution:** Make sure you're running in WSL and have installed all dependencies:
```bash
cd /mnt/c/Users/Luke/Documents/Cursor/audio2hero
source venv/bin/activate
pip install -r requirements.txt
```

### Error: Model download fails

**Solution:**
- Check internet connection
- Ensure you have enough disk space (model is several GB)
- The download will resume if interrupted

### Audio file format issues

**Best practices:**
- Use **MP3** or **WAV** format for best compatibility
- Ensure the file is not DRM-protected
- File should be a standard audio file (not a video file with audio track)

**To convert audio files:**
```bash
# Convert to MP3 (in WSL)
ffmpeg -i input.m4a -acodec libmp3lame -ab 192k output.mp3

# Convert to WAV
ffmpeg -i input.mp3 output.wav
```

## Getting Help

If you encounter other errors:
1. Save the error output to a file: `python app.py > error.txt 2>&1`
2. Check the error message for specific module or file issues
3. Make sure all dependencies are installed: `pip list`

