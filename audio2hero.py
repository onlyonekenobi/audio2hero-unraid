import sys
import os
import librosa
from transformers import Pop2PianoForConditionalGeneration, Pop2PianoProcessor, Pop2PianoTokenizer
import torch
from post_processor import post_process
import tempfile
import shutil
import traceback

def generate_midi(song_path, output_dir=None, original_file_path=None):
  """
  Generate MIDI chart from audio file with error handling
  
  Args:
    song_path: Path to input audio file
    output_dir: Output directory for generated files
    
  Returns:
    Path to generated ZIP file, or raises exception with user-friendly message
  """
  converted_file = None
  temp_dir = None
  
  try:
    if output_dir is None:
      # Use environment variable if set (for Docker), otherwise default
      output_dir = os.getenv("OUTPUT_DIR", "./outputs")
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    print("Loading Model...")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using {device}")
    
    try:
      model = Pop2PianoForConditionalGeneration.from_pretrained("Tim-gubski/Audio2Hero").to(device)
      model.eval()
      processor = Pop2PianoProcessor.from_pretrained("sweetcocoa/pop2piano")
      tokenizer = Pop2PianoTokenizer.from_pretrained("sweetcocoa/pop2piano")
    except Exception as e:
      raise RuntimeError(f"Failed to load AI model. Please check your internet connection and try again. Error: {str(e)}")

    print("Processing Song...")
    
    # Load audio file
    try:
      audio, sr = librosa.load(song_path, sr=44100)
      if len(audio) == 0:
        raise ValueError("Audio file appears to be empty or corrupted")
    except Exception as e:
      raise RuntimeError(f"Failed to load audio file. Please ensure the file is a valid audio format. Error: {str(e)}")
    
    try:
      inputs = processor(audio=audio, sampling_rate=sr, return_tensors="pt")
    except Exception as e:
      raise RuntimeError(f"Failed to process audio. The file may be corrupted or in an unsupported format. Error: {str(e)}")

    # generate model output
    print("Generating output...")
    try:
      model.generation_config.output_logits = True
      model.generation_config.return_dict_in_generate = True
      model_output = model.generate(inputs["input_features"].to(device))
    except Exception as e:
      raise RuntimeError(f"Failed to generate chart. This may be due to insufficient memory or a model error. Error: {str(e)}")

    try:
      tokenizer_output = processor.batch_decode(
              token_ids=model_output.sequences.cpu(),
              feature_extractor_output=inputs
          )
    except Exception as e:
      raise RuntimeError(f"Failed to decode model output. Error: {str(e)}")

    # save to temp file
    temp_dir = tempfile.TemporaryDirectory()
    try:
      tokenizer_output["pretty_midi_objects"][0].write(f"{temp_dir.name}/temp.mid")
    except Exception as e:
      raise RuntimeError(f"Failed to create MIDI file. Error: {str(e)}")

    print("Post Processing...")
    try:
      # Use original file path for post-processing (for metadata extraction)
      # but use processed file path if original not provided
      file_for_postprocess = original_file_path if original_file_path else song_path
      post_process(file_for_postprocess, f"{temp_dir.name}/temp.mid", output_dir)
    except Exception as e:
      raise RuntimeError(f"Failed during post-processing. Error: {str(e)}")
    
    # zip folder
    song_name = song_path.split("/")[-1]
    song_name = ".".join(song_name.split(".")[0:-1])
    
    # Clean up song name (remove any path separators that might cause issues)
    song_name = song_name.replace("/", "_").replace("\\", "_")
    
    try:
      zip_path = f"{output_dir}/{song_name}.zip"
      shutil.make_archive(f"{output_dir}/{song_name}", 'zip', f"{output_dir}/{song_name}")
      
      if not os.path.exists(zip_path):
        raise FileNotFoundError("ZIP file was not created successfully")
    except Exception as e:
      raise RuntimeError(f"Failed to create ZIP file. Error: {str(e)}")

    if temp_dir:
      temp_dir.cleanup()
    
    print("Done.")
    return zip_path
    
  except RuntimeError:
    # Re-raise RuntimeErrors (these are user-friendly)
    raise
  except Exception as e:
    # Convert unexpected errors to user-friendly messages
    error_details = traceback.format_exc()
    print(f"Unexpected error: {error_details}")
    raise RuntimeError(f"An unexpected error occurred during processing: {str(e)}. Please try again or check the file format.")
  finally:
    # Cleanup converted file if it was created
    if converted_file and os.path.exists(converted_file) and converted_file != song_path:
      try:
        os.remove(converted_file)
      except:
        pass


if __name__=="__main__":
  args = sys.argv[1:]
  song_path = args[0]
  output_dir = args[1]
  generate_midi(song_path, output_dir)

  
