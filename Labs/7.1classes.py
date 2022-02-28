# Raj Pabari Python III

import pygame
from random import randint

SCREEN_SIZE = (400, 500)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Rectangle:
    def __init__(self, screen, pos=[0, 0], size=[10, 10], color=GREEN) -> None:
        self.screen = screen
        self.pos = pos
        self.size = size
        self.color = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color,
                         [self.pos[0], self.pos[1], self.size[0], self.size[1]], 0)

    def move(self, changeX, changeY):
        self.pos[0] += changeX
        self.pos[1] += changeY
        return self.pos

    def setPos(self, x, y):
        self.pos[0] = x
        self.pos[1] = y
        return self.pos

    def setSize(self, width, height):
        self.size[0] = width
        self.size[1] = height
        return self.size


class Ellipse(Rectangle):
    def draw(self):
        pygame.draw.ellipse(self.screen, self.color,
                            [self.pos[0], self.pos[1], self.size[0], self.size[1]], 0)


def main():
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)

    shapes = []

    for i in range(1000):
        shapes.append(Ellipse(screen,
                              [randint(0, SCREEN_SIZE[0]-50),
                               randint(0, SCREEN_SIZE[1]-50)],
                              [randint(10, 50), randint(10, 50)],
                              (randint(0, 255), randint(0, 255), randint(0, 255))))

        shapes.append(Rectangle(screen,
                                [randint(0, SCREEN_SIZE[0]-50),
                                 randint(0, SCREEN_SIZE[1]-50)],
                                [randint(10, 50), randint(10, 50)],
                                (randint(0, 255), randint(0, 255), randint(0, 255))))

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)

        for shape in shapes:
            shape.move(randint(-3, 3), randint(-3, 3))
            shape.draw()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
