import pygame
import sys
import json
from recorder import Recorder

# Initialize pygame
pygame.init()

# Load configuration
with open('C:\\atari-monk\\code\\piano\\data\\piano_config.json', 'r') as f:
    config = json.load(f)

# Initialize variables
current_set_index = 1
current_set = config['sets'][current_set_index]
key_map = current_set['key_map']
sound_path = current_set['path']
instructions = current_set['instructions']

# Function to load sounds based on the current key map
def load_sounds(key_map, path):
    return {getattr(pygame, key): pygame.mixer.Sound(f'{path}\\{file}') for key, file in key_map.items()}

sounds = load_sounds(key_map, sound_path)

# Set up the display
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Virtual Piano")

# Initialize recorder
recorder = Recorder()

def handle_key_events(event):
    """Handle key events for playing sounds and recording."""
    global current_set_index, sounds, current_set, key_map, sound_path, instructions  # Move this line to the top of the function
    if event.key in sounds:
        sounds[event.key].play()
        recorder.record_key_press(event.key)
    elif event.key == pygame.K_r:  # Press 'r' to start/stop recording
        if recorder.is_recording:
            recorder.stop_recording()
            recorder.save_recording('C:\\atari-monk\\code\\piano\\data\\recording.json')
        else:
            recorder.start_recording()
    elif event.key == pygame.K_p:  # Press 'p' to play the recording
        if not recorder.is_recording:
            loaded_recording = recorder.load_recording('C:\\atari-monk\\code\\piano\\data\\recording.json')
            recorder.play_recording(loaded_recording, sounds)
    elif event.key == pygame.K_n:  # Press 'n' to switch to the next set of notes
        current_set_index = (current_set_index + 1) % len(config['sets'])
        current_set = config['sets'][current_set_index]
        key_map = current_set['key_map']
        sound_path = current_set['path']
        instructions = current_set['instructions']
        sounds = load_sounds(key_map, sound_path)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                handle_key_events(event)
            elif event.type == pygame.KEYUP:
                if event.key in sounds:
                    sounds[event.key].stop()
                    recorder.record_key_release(event.key)

        # Clear the screen
        screen.fill((255, 255, 255))

        # Display instructions
        font = pygame.font.Font(None, 36)
        lines = [
            instructions,
            "Press 'r' to start/stop recording",
            "Press 'p' to play the recording",
            "Press 'n' to switch to the next set of notes"
        ]

        y = 50
        for line in lines:
            text = font.render(line, True, (0, 0, 0))
            screen.blit(text, (20, y))
            y += 40

        pygame.display.flip()

if __name__ == "__main__":
    main()
