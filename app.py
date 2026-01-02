import gradio as gr
from transformers import pipeline
import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from audio2hero import generate_midi
from audio_converter import prepare_audio_file
try:
    import spaces
except ImportError:
    # spaces is optional for local use
    class GPU:
        def __init__(self, func):
            self.func = func
        def __call__(self, *args, **kwargs):
            return self.func(*args, **kwargs)
    spaces = type('spaces', (), {'GPU': GPU})()


def process_audio_with_conversion(audio_file):
    """
    Process audio file with automatic format conversion and error handling
    
    Args:
        audio_file: Path to uploaded audio file (tuple from Gradio: (file_path, sample_rate))
        
    Returns:
        Tuple of (zip_path, error_message)
    """
    if audio_file is None:
        return None, "Please upload an audio file."
    
    # Gradio Audio returns a tuple (file_path, sample_rate) or just file_path
    if isinstance(audio_file, tuple):
        audio_file_path = audio_file[0]
    else:
        audio_file_path = audio_file
    
    converted_file = None
    try:
        # Prepare audio file (convert to MP3 if necessary)
        processed_file, was_converted, temp_file = prepare_audio_file(audio_file_path)
        converted_file = processed_file if was_converted else None
        
        # Generate MIDI chart
        # Use converted file for audio processing, but pass original for post-processing
        zip_path = generate_midi(processed_file, original_file_path=audio_file_path)
        
        # Return the ZIP file for download
        return zip_path, None
        
    except FileNotFoundError as e:
        error_msg = f"File not found: {str(e)}"
        print(f"Error: {error_msg}")
        return None, error_msg
    except RuntimeError as e:
        error_msg = f"Processing error: {str(e)}"
        print(f"Error: {error_msg}")
        return None, error_msg
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(f"Error: {error_msg}")
        return None, error_msg
    finally:
        # Cleanup converted file if it was temporary
        if converted_file and os.path.exists(converted_file) and converted_file != audio_file_path:
            try:
                os.remove(converted_file)
            except:
                pass


# Create Gradio interface with error handling
with gr.Blocks(title="Audio2Hero - AI Chart Generator") as gradio_app:
    gr.Markdown("""
    # 🎸 Audio2Hero AI Charter Assistant for CloneHero
    
    Generate medium difficulty Clone Hero charts from any audio file!
    
    **Features:**
    - ✅ Supports multiple audio formats (MP3, WAV, M4A, FLAC, etc.) - automatically converts if needed
    - ✅ Direct ZIP file download after conversion
    - ✅ User-friendly error messages
    - ⏱️ Processing takes 30-60 seconds per song
    
    **Tips:**
    - Name your file as `Artist - Song Name` for best metadata extraction
    - The output ZIP contains: MIDI chart, song.ogg, and song.ini
    - Ready to use in Clone Hero or edit in Moonscraper
    """)
    
    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                label="Upload Audio File (MP3, WAV, M4A, FLAC, etc.)",
                type="filepath",
                sources=["upload"]
            )
            process_btn = gr.Button("Generate Chart", variant="primary", size="lg")
        
        with gr.Column():
            zip_output = gr.File(
                label="Download ZIP File",
                file_count="single",
                visible=True
            )
            error_output = gr.Textbox(
                label="Status",
                placeholder="Ready to process...",
                interactive=False,
                visible=True
            )
    
    # Process button click handler
    def process_file(audio):
        if audio is None:
            return None, "❌ Please upload an audio file first."
        
        zip_file, error = process_audio_with_conversion(audio)
        
        if error:
            return None, f"❌ {error}"
        elif zip_file:
            return zip_file, "✅ Chart generated successfully! Click the download button above."
        else:
            return None, "⚠️ Processing completed but no file was generated."
    
    process_btn.click(
        fn=process_file,
        inputs=[audio_input],
        outputs=[zip_output, error_output],
        show_progress=True
    )
    
    gr.Markdown("""
    ### 📝 Notes
    - First run will download the AI model (~500MB-1GB) - this only happens once
    - Processing time varies based on song length and server performance
    - Generated charts are medium difficulty only
    - Charts may sometimes follow other instruments (drums, bass, vocals) in addition to guitar
    """)

if __name__ == "__main__":
    # Allow server name and port to be configured via environment variables
    server_name = os.getenv("GRADIO_SERVER_NAME", "127.0.0.1")
    server_port = int(os.getenv("GRADIO_SERVER_PORT", 7860))
    gradio_app.launch(server_name=server_name, server_port=server_port, share=False)