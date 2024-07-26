import numpy as np
from scipy.io.wavfile import write
import os

# Function to generate a sine wave for a given frequency
def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave.astype(np.int16)

# Define frequencies for the notes (C4 to C5)
frequencies = {
    'C': 261.63,  # C4
    'D': 293.66,  # D4
    'E': 329.63,  # E4
    'F': 349.23,  # F4
    'G': 392.00,  # G4
    'A': 440.00,  # A4
    'B': 493.88,  # B4
    'C_high': 523.25  # C5
}

# Generate and save the sound files if not already present
os.makedirs('generated_sounds', exist_ok=True)
for note, freq in frequencies.items():
    filename = f'generated_sounds/{note}.wav'
    if not os.path.exists(filename):
        wave = generate_sine_wave(freq, 1.0)  # 1 second duration
        write(filename, 44100, wave)

print("Sound files generated and saved in 'generated_sounds' directory.")
