from math import pi, cos, sin
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

    shiftX = 0
    right = True
    shiftY = 0
    down = True
    speed = 1

    shiftTheta = 0.0
    shiftMag = 50.0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)

        pygame.draw.rect(screen, BLACK, [75+shiftX, 75+shiftY, 250, 150], 0)

        pygame.draw.polygon(
            screen, RED, [[75+shiftX, 75+shiftY], [((75+325) / 2)+shiftX, 20+shiftY], [325+shiftX, 75+shiftY]], 0)

        for i in range(10, 250, 30):
            pygame.draw.rect(
                screen, BLUE, [75 + i + shiftX, 100 + shiftY, 20, 20], 0)
            pygame.draw.line(
                screen, BLACK, [85 + i + shiftX, 102.5 + shiftY], [85+i+shiftX, 117.5+shiftY], 2)
            pygame.draw.line(
                screen, BLACK, [77.5 + i+shiftX, 110+shiftY], [92.5+i+shiftX, 110+shiftY], 2)

        pygame.draw.rect(screen, BLUE, [100+shiftX, 150+shiftY, 30, 60], 0)
        pygame.draw.arc(
            screen, RED, [100+shiftX, 135+shiftY, 30, 30], 0, pi, 5)

        pygame.draw.circle(
            screen, GREEN, [200+shiftMag*cos(shiftTheta), 250+shiftMag*sin(shiftTheta)], 20, 0)

        if (20+shiftY) <= 0:
            down = True
        elif (225+shiftY) >= 500:
            down = False
        if down:
            shiftY += speed
        elif not down:
            shiftY -= speed

        if (75+shiftX) <= 0:
            right = True
        elif (325+shiftX) >= 400:
            right = False
        if right:
            shiftX += speed
        elif not right:
            shiftX -= speed

        shiftTheta += 0.05 * float(speed)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
