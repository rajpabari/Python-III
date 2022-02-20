from math import pi, cos, sin
import pygame

# source: https://pngtree.com/freebackground/blue-earth-outer-space-background_1011332.html
BG_LOCATION = "./Labs/6.1bitmapping/space-background.jpg"
# source: http://clipart-library.com/clipart/BcarpLEKi.htm
SMILEY_LOCATION = "./Labs/6.1bitmapping/smileyFace.png"
# source: https://www.youtube.com/watch?v=attUrDwfdr8
VICTORY_LOCATION = "./Labs/6.1bitmapping/yaySound.mp3"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SIZE = (800, 800)


def drawHouse(screen, xPos, yPos):
    # returns bounds of door of house

    pygame.draw.rect(screen, BLACK, [xPos, yPos, 250, 150], 0)

    pygame.draw.polygon(
        screen, RED, [[xPos, yPos], [125 + xPos, yPos - 55], [xPos + 250, yPos]], 0)

    for i in range(10, 250, 30):
        pygame.draw.rect(screen, BLUE, [xPos + i, yPos + 10, 20, 20], 0)
        pygame.draw.line(
            screen, BLACK, [xPos + 10 + i, yPos + 12.5], [xPos + 10 + i, yPos + 27.5], 2)
        pygame.draw.line(
            screen, BLACK, [xPos + 2.5 + i, yPos + 20], [xPos + 17.5 + i, yPos + 20], 2)

    pygame.draw.rect(screen, BLUE, [xPos + 25, yPos + 60, 30, 60], 0)
    pygame.draw.arc(screen, RED, [xPos + 25, yPos + 45, 30, 30], 0, pi, 5)

    return [(xPos+25, yPos+60), (xPos+55, yPos+120)]


def main():

    pygame.init()

    screen = pygame.display.set_mode(SIZE)
    bgImage = pygame.image.load(BG_LOCATION).convert()
    smileyImage = pygame.image.load(SMILEY_LOCATION).convert()
    smileyImage.set_colorkey(BLACK)

    font = pygame.font.SysFont('Calibri', 25, True, False)
    regularText = font.render(
        "Get the smiley face in the door to win", True, BLACK)
    victoryText = font.render("You won!", True, BLACK)
    victorySound = pygame.mixer.Sound(VICTORY_LOCATION)

    done = False
    clock = pygame.time.Clock()

    smileyPos = [SIZE[0]/2, SIZE[1]/2]
    smileyShift = [0, 0]
    victory = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    smileyShift[0] = -1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    smileyShift[0] = 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    smileyShift[1] = 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    smileyShift[1] = -1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    smileyShift[0] = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_w:
                    smileyShift[1] = 0

        screen.blit(bgImage, [0, 0])
        victoryZone = drawHouse(screen, 100, 400)
        for i in range(len(smileyPos)):
            smileyPos[i] += smileyShift[i]

        screen.blit(smileyImage, smileyPos)

        if smileyPos[0] >= victoryZone[0][0] and smileyPos[0]+25 <= victoryZone[1][0]:
            if smileyPos[1] >= victoryZone[0][1] and smileyPos[1]+25 <= victoryZone[1][1]:
                victory = True
            else:
                victory = False
        else:
            victory = False

        if victory:
            screen.blit(victoryText, [100, 600])
            if not pygame.mixer.get_busy():
                victorySound.set_volume(100)
                victorySound.play()
        else:
            victorySound.set_volume(0)
            screen.blit(regularText, [100, 600])
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
