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

        pygame.draw.rect(screen, BLACK, [75, 75, 250, 150], 0)

        pygame.draw.polygon(
            screen, RED, [[75, 75], [(75+325) / 2, 20], [325, 75]], 0)

        for i in range(10, 250, 30):
            pygame.draw.rect(screen, BLUE, [75 + i, 100, 20, 20], 0)
            pygame.draw.line(
                screen, BLACK, [85 + i, 102.5], [85+i, 117.5], 2)
            pygame.draw.line(screen, BLACK, [77.5 + i, 110], [92.5+i, 110], 2)

        pygame.draw.rect(screen, BLUE, [100, 150, 30, 60], 0)
        pygame.draw.arc(screen, RED, [100, 135, 30, 30], 0, pi, 5)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
