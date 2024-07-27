import pygame
import sys
from recorder import Recorder

# Initialize pygame
pygame.init()

# Define key mappings
key_map = {
    pygame.K_a: "C.wav",
    pygame.K_s: "D.wav",
    pygame.K_d: "E.wav",
    pygame.K_f: "F.wav",
    pygame.K_g: "G.wav",
    pygame.K_h: "A.wav",
    pygame.K_j: "B.wav",
    pygame.K_k: "C_high.wav"
}

# Load sounds
sounds = {key: pygame.mixer.Sound(f'data/generated_sounds/{file}') for key, file in key_map.items()}

# Set up the display
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Virtual Piano")

# Initialize recorder
recorder = Recorder()

def main():
    global recorder

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in sounds:
                    sounds[event.key].play()
                    recorder.record_key_press(event.key)
                elif event.key == pygame.K_r:  # Press 'r' to start/stop recording
                    if recorder.is_recording:
                        recorder.stop_recording()
                        recorder.save_recording('data/recording.json')
                    else:
                        recorder.start_recording()
                elif event.key == pygame.K_p:  # Press 'p' to play the recording
                    if not recorder.is_recording:
                        loaded_recording = recorder.load_recording('data/recording.json')
                        recorder.play_recording(loaded_recording, sounds)
            elif event.type == pygame.KEYUP:
                if event.key in sounds:
                    sounds[event.key].stop()
                    recorder.record_key_release(event.key)

        # Clear the screen
        screen.fill((255, 255, 255))

        # Display instructions
        font = pygame.font.Font(None, 36)
        instructions = [
            "Press keys A, S, D, F, G, H, J, K to play notes C D E F G A B C_high",
            "Press 'r' to start/stop recording",
            "Press 'p' to play the recording"
        ]

        y = 50
        for line in instructions:
            text = font.render(line, True, (0, 0, 0))
            screen.blit(text, (20, y))
            y += 40

        pygame.display.flip()

if __name__ == "__main__":
    main()
