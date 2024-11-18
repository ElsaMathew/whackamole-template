import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        #screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
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
                    # mole_image.get_rect(center=(x, y))
                    print(event.pos[0])
                    if x // 32 * 32 == event.pos[0] // 32 * 32 and y // 32 * 32 == event.pos[1] // 32 * 32:
                        x = random.randrange(0, 609)
                        y = random.randrange(0, 481)
                        screen.blit(mole_image, mole_image.get_rect(topleft = (x, y)))

            screen.fill("light green")
            for i in range(1, 20):
                pygame.draw.line(screen, "black", (i * 32, 0), (i * 32, 512))
            for j in range(1, 16):
                pygame.draw.line(screen, "black", (0, j * 32), (640, j * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
            pygame.display.flip()
            clock.tick(60)
            # if pygame.MOUSEBUTTONDOWN:
            #     a, b = event.pos
            #     print(x)
            #     x = random.randrange(0, 609)
            #     y = random.randrange(0, 481)
            #     if x % 32 != 0:
            #         x = x // 32
            #     if y % 32 != 0:
            #         y = y // 32
            #     screen.blit(mole_image, mole_image.get_rect(topleft= (x, y)))

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
