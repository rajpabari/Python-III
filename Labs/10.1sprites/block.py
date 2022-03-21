import pygame

BLACK = (0, 0, 0)


class Block(pygame.sprite.Sprite):
    def __init__(self, filename) -> None:
        super().__init__()

        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
