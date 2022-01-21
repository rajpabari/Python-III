# Raj Pabari Python 3
from random import randrange


def main():
    print("In this game you will have 5 tries to guess the value of a randomly generated number between 0 and 50")
    ans = randrange(51)

    for i in range(5):
        guess = int(input("What's your guess? "))
        if (guess == ans):
            print("Congrats, you won!")
            return
        elif (guess > ans):
            print("Too high")
        else:
            print("Too low")

    print("Sorry, you lost! The correct number was", ans)


if __name__ == "__main__":
    main()
