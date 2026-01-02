import gradio as gr
from transformers import pipeline
import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from audio2hero import generate_midi
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



gradio_app = gr.Interface(
    spaces.GPU(generate_midi),
    inputs=gr.Audio(label="Input Audio", type="filepath"),
    outputs=gr.File(label="Output MIDI Zip File"),
    title="Audio2Hero AI Charter Assistant for CloneHero",
    description="""Audio2Hero will generate a medium difficulty Clone Hero chart from any audio file. This can be a helping starting point to create your own charts, or you can play them as is! 
                  Make sure to rename your audio file to 'Artist - Song Name' for the autocharter to correctly
                  generate the song.ini file. The output will be a zip file containing the MIDI file, song.ogg 
                  and song.ini file. The auto charter can take upto 45 seconds to generate so please be patient. Hope you enjoy!""",
)

if __name__ == "__main__":
    # Allow server name and port to be configured via environment variables
    server_name = os.getenv("GRADIO_SERVER_NAME", "127.0.0.1")
    server_port = int(os.getenv("GRADIO_SERVER_PORT", 7860))
    gradio_app.launch(server_name=server_name, server_port=server_port, share=False)