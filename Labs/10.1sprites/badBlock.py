from block import Block
from random import randint


class BadBlock(Block):
    def update(self):
        self.rect.y += 1
        if self.rect.y >= 380:
            self.rect.y = 0
