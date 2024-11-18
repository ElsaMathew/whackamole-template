import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x = 0
        y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if x // 32 * 32 == event.pos[0] // 32 * 32 and y // 32 * 32 == event.pos[1] // 32 * 32:
                        x = random.randrange(0, 609) // 32 * 32
                        y = random.randrange(0, 481) // 32* 32
                        screen.blit(mole_image, mole_image.get_rect(topleft = (x, y)))

            screen.fill((242, 255, 244))
            for i in range(1, 20):
                pygame.draw.line(screen, (15, 79, 21), (i * 32, 0), (i * 32, 512))
            for j in range(1, 16):
                pygame.draw.line(screen, (15, 79, 21), (0, j * 32), (640, j * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
