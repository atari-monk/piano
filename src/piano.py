import pygame
import sys
import json

# Initialize pygame
pygame.init()

# Load configuration
with open('C:\\atari-monk\\code\\piano\\data\\piano_config.json', 'r') as f:
    config = json.load(f)

# Initialize variables
current_set = config['sets'][1]
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

def handle_key_events(event):
    """Handle key events for playing sounds."""
    if event.key in sounds:
        sounds[event.key].play()

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

        # Clear the screen
        screen.fill((255, 255, 255))

        # Display instructions
        font = pygame.font.Font(None, 36)
        lines = [instructions]

        y = 50
        for line in lines:
            text = font.render(line, True, (0, 0, 0))
            screen.blit(text, (20, y))
            y += 40

        pygame.display.flip()

if __name__ == "__main__":
    main()
