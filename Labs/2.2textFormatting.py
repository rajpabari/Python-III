import pygame


def nums(start, stop):
    counter = 1
    temp = 0
    ans = ""
    for i in range(start, stop+1):
        temp += 1
        ans += str(i) + " "
        if (temp == counter):
            temp = 0
            counter += 1
            print(ans)
            ans = ""
    if (temp != 0):
        print(ans)


def init(size):
    ans = ""
    for i in range(size*2):
        ans += "o"
    print(ans)


def o(size):
    init(size)
    ans = ""
    if size <= 1:
        return
    if size != 2:
        for i in range(size*2):
            if (i == 0 or i == size*2-1):
                ans += "o"
            else:
                ans += " "
        for i in range(size-2):
            print(ans)
    init(size)


def genRow(start, stop):
    ans = ""
    while start <= stop:
        counter = 0
        for i in range(start, stop+1, 2):
            ans += str(i) + " "
            counter += 2
        ans = ans[:-1]
        while (counter <= stop):
            ans += " "
            counter += 1
        start += 2
        ans += "\n"
    return ans[:-1]


def square(size):
    start = 0
    if (size % 2 == 1):
        start = 1
    top = genRow(start, size*2-1)

    rows = top.split("\n")
    for row in range(len(rows)-1, -1, -1):
        rows.append(rows[row])

    ans = ""
    for row in rows:
        ans += row + " " + row[::-1] + "\n"

    print(ans[:-1])


def rect(width, height):
    pygame.init()
    size = (width, height)
    screen = pygame.display.set_mode(size)
    done = False
    clock = pygame.time.Clock()

    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(BLACK)

        for i in range(0, width, 10):
            for j in range(0, height, 10):
                pygame.draw.rect(screen, GREEN, [i, j, 7.5, 7.5], 0)

        pygame.display.flip()

    pygame.quit()


def main():
    nums(10, 54)
    print("")

    o(int(input("How many rows of Os? ")))
    print("")

    square(int(input("How big should square be (NOTE: only for i <= 5)? ")))
    print("")

    input("Ready to launch pygame window? ")
    rect(400, 500)


if __name__ == "__main__":
    main()
