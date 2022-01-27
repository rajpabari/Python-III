from math import pi
import pygame


def main():
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    size = (400, 500)
    screen = pygame.display.set_mode(size)

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)

        pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

        # draws repeated offset lines
        for i in range(0, 100, 10):
            pygame.draw.line(screen, RED, [0, 10+i], [100, 110+i], 5)

        # Top Left is (20,20), width in x direction 250 and y direction 100
        pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)
        pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

        # drawing the ellipse but only swept from some angle to some other angle
        pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, pi/2, 2)
        pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], pi/2, pi, 2)
        pygame.draw.arc(screen, RED, [20, 220, 250, 200], pi, 3 * pi/2, 2)
        pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], 3*pi / 2, 2 * pi, 2)

        # three vertices of triangle
        pygame.draw.polygon(
            screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

        font = pygame.font.SysFont("Calibri", 25, True, False)

        text = font.render("Test message", True, BLACK)
        screen.blit(text, [250, 250])

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
