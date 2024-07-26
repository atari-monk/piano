import pygame
import numpy as np
from scipy.io.wavfile import write
import os
import sys

# Initialize pygame
pygame.init()

# Function to generate a sine wave for a given frequency
def generate_sine_wave(freq, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave.astype(np.int16)

# Define frequencies for the notes (C4 to C5)
frequencies = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'C5': 523.25
}

# Generate and save the sound files if not already present
os.makedirs('generated_sounds', exist_ok=True)
for note, freq in frequencies.items():
    filename = f'generated_sounds/{note}.wav'
    if not os.path.exists(filename):
        wave = generate_sine_wave(freq, 1.0)  # 1 second duration
        write(filename, 44100, wave)

# Define key mappings
key_map = {
    pygame.K_a: "C4.wav",
    pygame.K_s: "D4.wav",
    pygame.K_d: "E4.wav",
    pygame.K_f: "F4.wav",
    pygame.K_g: "G4.wav",
    pygame.K_h: "A4.wav",
    pygame.K_j: "B4.wav",
    pygame.K_k: "C5.wav"
}

# Load sounds
sounds = {key: pygame.mixer.Sound(f'generated_sounds/{file}') for key, file in key_map.items()}

# Set up the display
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Virtual Piano")

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in sounds:
                    sounds[event.key].play()
            elif event.type == pygame.KEYUP:
                if event.key in sounds:
                    sounds[event.key].stop()

        # Clear the screen
        screen.fill((255, 255, 255))
        
        # Display instructions
        font = pygame.font.Font(None, 36)
        instructions = [
            "Press keys A, S, D, F, G, H, J, K to play notes",
            "Twinkle Twinkle Little Star:",
            "A A G G H H G",
            "F F D D S S A",
            "G G F F D D S",
            "G G F F D D S",
            "A A G G H H G",
            "F F D D S S A"
        ]
        
        y = 50
        for line in instructions:
            text = font.render(line, True, (0, 0, 0))
            screen.blit(text, (20, y))
            y += 40
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
