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
sample_dir = 'C:\\atari-monk\\code\\piano\\audio\\piano_samples'
output_dir = 'C:\\atari-monk\\code\\piano\\audio\\piano_sounds'
os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

# List of sample files
sample_files = [
    'Piano.mf.A4.aiff',
    'Piano.mf.B4.aiff',
    'Piano.mf.C4.aiff',
    'Piano.mf.C5.aiff',
    'Piano.mf.D4.aiff',
    'Piano.mf.E4.aiff',
    'Piano.mf.F4.aiff',
    'Piano.mf.G4.aiff'
]

# Process each sample file
for filename in sample_files:
    sample_path = os.path.join(sample_dir, filename)
    print(f"Processing {filename}")

    if os.path.exists(sample_path):
        sample_rate, wave = read_aiff(sample_path)
        if sample_rate is not None and wave is not None:
            note_dynamic = filename.split('.')[2] + '_' + filename.split('.')[1]  # Extract note and dynamic level
            output_path = os.path.join(output_dir, f'{note_dynamic}.wav')
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
