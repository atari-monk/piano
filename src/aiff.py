import os
import numpy as np
from scipy.io import wavfile
import soundfile as sf

# Function to read AIFF file
def read_aiff(filename):
    try:
        wave, sample_rate = sf.read(filename)
        return sample_rate, wave
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None, None

# Directory containing the piano samples
sample_dir = '../audio/piano_samples'
output_dir = '../audio/piano_sounds'
os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

# Example: Playing a specific note at a specific dynamic level
note = 'C'
octave = 4
dynamic = 'mf'

filename = f'Piano.{dynamic}.{note}{octave}.aiff'
sample_path = os.path.join(sample_dir, filename)
print(f"Sample path: {os.path.abspath(sample_path)}")

if os.path.exists(sample_path):
    sample_rate, wave = read_aiff(sample_path)
    if sample_rate is not None and wave is not None:
        output_path = os.path.join(output_dir, f'{note}{octave}_{dynamic}.wav')
        try:
            if wave.ndim == 2:  # Stereo
                wavfile.write(output_path, sample_rate, (wave * 32767).astype(np.int16))
            else:  # Mono
                wavfile.write(output_path, sample_rate, (wave * 32767).astype(np.int16))
            print(f"Saved {filename} to {output_path}")
        except Exception as e:
            print(f"Error writing {output_path}: {e}")
    else:
        print("Failed to read the sample.")
else:
    print(f"Sample file not found: {sample_path}")
