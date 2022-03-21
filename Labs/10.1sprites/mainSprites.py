# Raj Pabari Python III

import pygame
from random import randint
from goodBlock import GoodBlock
from badBlock import BadBlock

SCREEN_SIZE = (700, 400)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SPEED = 2
# source: https://www.pngfind.com/download/bomhbm_mario-coin-png-mario-coin-pixel-art-transparent/
COIN_LOCATION = "./Labs/8.1sprites/mario-coin.png"
# source: https://mario.wiki.gallery/images/thumb/e/ee/Spike_ball_PMTOK_sprite.png/120px-Spike_ball_PMTOK_sprite.png
SPIKE_LOCATION = "./Labs/8.1sprites/spike-ball.png"
# source: python arcade games tutorial
GOOD_LOCATION = "./Labs/8.1sprites/good_block.wav"
# source: python arcade games tutorial
BAD_LOCATION = "./Labs/8.1sprites/bad_block.wav"
# source: python arcade games tutorial
BUMP_LOCATION = "./Labs/8.1sprites/bump.wav"


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        # create and remove background
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, BLUE, [0, 0, 15, 15])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = [0, 0]

    def changeSpeed(self, shift):
        self.speed[0] = shift[0]
        self.speed[1] = shift[1]

    def update(self) -> bool:
        moved = True
        if self.rect.x + self.speed[0] < 0:
            self.rect.x = 0
            moved = False
        elif self.rect.x + self.speed[0] > SCREEN_SIZE[0]-15:
            self.rect.x = SCREEN_SIZE[0]-15
            moved = False
        else:
            self.rect.x += self.speed[0]

        if self.rect.y + self.speed[1] < 0:
            self.rect.y = 0
            moved = False
        elif self.rect.y + self.speed[1] > SCREEN_SIZE[1]-15:
            self.rect.y = SCREEN_SIZE[1]-15
            moved = False
        else:
            self.rect.y += self.speed[1]

        return moved


def main():
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)

    goodBlockList = pygame.sprite.Group()
    badBlockList = pygame.sprite.Group()
    allSpritesList = pygame.sprite.Group()

    for i in range(50):
        block = GoodBlock(COIN_LOCATION)
        block.rect.x = randint(0, SCREEN_SIZE[0]-20)
        block.rect.y = randint(0, SCREEN_SIZE[1]-20)

        goodBlockList.add(block)
        allSpritesList.add(block)

    for i in range(50):
        block = BadBlock(SPIKE_LOCATION)
        block.rect.x = randint(0, SCREEN_SIZE[0]-20)
        block.rect.y = randint(0, SCREEN_SIZE[1]-20)

        badBlockList.add(block)
        allSpritesList.add(block)

    player = Player(20, 15)
    allSpritesList.add(player)

    goodCollision = pygame.mixer.Sound(GOOD_LOCATION)
    badCollision = pygame.mixer.Sound(BAD_LOCATION)
    wallCollision = pygame.mixer.Sound(BUMP_LOCATION)

    score = 0

    FONT = pygame.font.SysFont("Calibri", 25, True, False)

    done = False
    shift = [0, 0]
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    shift[0] = -1*SPEED
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    shift[0] = SPEED
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    shift[1] = SPEED
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    shift[1] = -1*SPEED
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    shift[0] = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_w:
                    shift[1] = 0

        player.changeSpeed(shift)

        screen.fill(WHITE)

        blocksHitList = pygame.sprite.spritecollide(
            player, goodBlockList, True)

        for block in blocksHitList:
            score += 1
            goodCollision.play()

        blocksHitList = pygame.sprite.spritecollide(player, badBlockList, True)

        for block in blocksHitList:
            score -= 1
            badCollision.play()

        if not player.update():
            if not pygame.mixer.get_busy():
                wallCollision.play()

        allSpritesList.update()
        allSpritesList.draw(screen)

        text = FONT.render("Your score: "+str(score), True, BLUE)
        screen.blit(text, [0, 350])

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
