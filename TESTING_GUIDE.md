# Local Testing Guide

## Quick Start

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Open your browser:**
   - Go to: `http://127.0.0.1:7860`
   - You should see the Audio2Hero interface

## Testing Checklist

### ✅ Test 1: UI Loading
- [ ] Interface loads without errors
- [ ] Upload button is visible
- [ ] Status message shows "Ready to process..."

### ✅ Test 2: MP3 File Upload
- [ ] Upload an MP3 file
- [ ] File is accepted
- [ ] Click "Generate Chart"
- [ ] Processing starts (status updates)
- [ ] ZIP file appears for download
- [ ] Download works

### ✅ Test 3: Non-MP3 Format Conversion
- [ ] Upload a WAV file
- [ ] File is accepted
- [ ] Click "Generate Chart"
- [ ] Conversion happens automatically (check status)
- [ ] Processing completes
- [ ] ZIP file available for download

### ✅ Test 4: Error Handling - Invalid File
- [ ] Upload a non-audio file (e.g., .txt, .jpg)
- [ ] Error message appears clearly
- [ ] Error is user-friendly (not a stack trace)

### ✅ Test 5: Error Handling - Corrupted File
- [ ] Upload a corrupted audio file
- [ ] Error message appears
- [ ] Message explains what went wrong

### ✅ Test 6: Multiple Formats
Test with different formats:
- [ ] MP3 (should work directly)
- [ ] WAV (should convert)
- [ ] M4A (should convert)
- [ ] FLAC (should convert)

## Expected Behavior

### Success Flow:
1. Upload file → Status: "Ready to process..."
2. Click "Generate Chart" → Status: "Processing..."
3. Conversion (if needed) → Status updates
4. Model processing → Status updates
5. Success → Status: "✅ Chart generated successfully!"
6. ZIP file appears → Click to download

### Error Flow:
1. Upload file → Status: "Ready to process..."
2. Click "Generate Chart" → Status: "Processing..."
3. Error occurs → Status: "❌ [Clear error message]"
4. No ZIP file → User knows what went wrong

## Troubleshooting

### App won't start
- Check if port 7860 is already in use
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (3.8+ required)

### FFmpeg errors
- Ensure FFmpeg is installed and in PATH
- Test: `ffmpeg -version`

### Model loading errors
- First run downloads the model (~500MB-1GB)
- Ensure internet connection is active
- Check disk space

### Conversion errors
- Test FFmpeg directly: `ffmpeg -i test.wav test.mp3`
- Check file permissions
- Ensure file is not corrupted

## Testing on Windows

**Note:** On Windows with Python 3.12+, the full processing may fail due to `essentia` dependency. However, you can still test:
- ✅ UI functionality
- ✅ File upload
- ✅ Format conversion
- ✅ Error handling
- ❌ Full model processing (requires WSL or Docker)

For full testing, use WSL or Docker.

## Next Steps After Testing

Once local testing is complete:
1. Fix any issues found
2. Commit changes: `git add . && git commit -m "Test results and fixes"`
3. Push to GitHub: `git push`
4. Deploy to Unraid Docker

