from block import Block
from random import randint


class GoodBlock(Block):
    def update(self):
        self.rect.x += randint(-3, 3)
        self.rect.y += randint(-3, 3)
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 680:
            self.rect.x = 680
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > 380:
            self.rect.y = 380
