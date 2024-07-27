import pygame
import sys

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
sounds = {key: pygame.mixer.Sound(f'generated_sounds/{file}') for key, file in key_map.items()}

# Set up the display
screen = pygame.display.set_mode((500, 200))
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
            "Press keys A, S, D, F, G, H, J, K",
            "to play notes C D E F G A B C_high"
        ]
        
        y = 50
        for line in instructions:
            text = font.render(line, True, (0, 0, 0))
            screen.blit(text, (20, y))
            y += 40
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
