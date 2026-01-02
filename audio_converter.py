"""
Audio format conversion utility for Audio2Hero
Converts various audio formats to MP3 for processing
"""
import os
import subprocess
import tempfile
from pathlib import Path


def get_audio_format(file_path):
    """Detect audio file format from extension"""
    ext = Path(file_path).suffix.lower()
    return ext[1:] if ext else None


def is_mp3(file_path):
    """Check if file is already MP3"""
    return get_audio_format(file_path) in ['mp3', 'mpeg']


def convert_to_mp3(input_path, output_path=None, quality=192):
    """
    Convert audio file to MP3 using ffmpeg
    
    Args:
        input_path: Path to input audio file
        output_path: Path for output MP3 file (optional, creates temp if not provided)
        quality: MP3 bitrate in kbps (default: 192)
    
    Returns:
        Path to converted MP3 file
    """
    if output_path is None:
        # Create temporary file
        temp_dir = tempfile.gettempdir()
        base_name = Path(input_path).stem
        output_path = os.path.join(temp_dir, f"{base_name}_converted.mp3")
    
    try:
        # Use ffmpeg to convert to MP3
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-acodec', 'libmp3lame',
            '-ab', f'{quality}k',
            '-y',  # Overwrite output file if it exists
            output_path
        ]
        
        # Run conversion (suppress output)
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        
        # Verify output file exists
        if not os.path.exists(output_path):
            raise FileNotFoundError(f"Conversion failed: output file not created")
        
        return output_path
        
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode('utf-8', errors='ignore')
        raise RuntimeError(f"FFmpeg conversion failed: {error_msg}")
    except FileNotFoundError:
        raise RuntimeError("FFmpeg not found. Please ensure FFmpeg is installed and in PATH.")


def prepare_audio_file(file_path):
    """
    Prepare audio file for processing - convert to MP3 if necessary
    
    Args:
        file_path: Path to input audio file (can be tuple from Gradio: (file_path, sample_rate))
    
    Returns:
        Tuple of (processed_file_path, was_converted, temp_file_path)
        - processed_file_path: Path to file ready for processing (MP3)
        - was_converted: Boolean indicating if conversion was performed
        - temp_file_path: Path to temporary converted file (None if not converted)
    """
    # Handle Gradio audio input (can be tuple or string)
    if isinstance(file_path, tuple):
        file_path = file_path[0]
    
    was_converted = False
    temp_file_path = None
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")
    
    # Check if already MP3
    if is_mp3(file_path):
        return file_path, False, None
    
    # Convert to MP3
    try:
        converted_path = convert_to_mp3(file_path)
        was_converted = True
        temp_file_path = converted_path
        return converted_path, True, converted_path
    except Exception as e:
        raise RuntimeError(f"Failed to convert audio file: {str(e)}")

