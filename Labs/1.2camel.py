# Raj Pabari Python III

from random import randint


def welcome():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.")


def options():
    print("\nA) Drink from canteen")
    print("B) Ahead moderate speed")
    print("C) Ahead full speed")
    print("D) Stop for the night")
    print("E) Status check")
    print("Q) Quit")


def status(mile, drink, native):
    print("Miles traveled:", mile)
    print("Drinks in canteen:", drink)
    print("The natives are", mile-native, "miles behind you")


def main():
    welcome()

    done = False
    miles = thirst = tired = 0
    natives = -20
    drinks = 3

    while not done:
        options()
        choice = input("Your choice? ").casefold()
        if (choice == "q"):
            done = True
            continue
        elif (choice == "e"):
            status(miles, drinks, natives)
            continue
        elif (choice == "d"):
            tired = 0
            print("The camel is happy!")
            natives += randint(7, 14)
        elif (choice == "c"):
            thirst += 1
            traveled = randint(10, 20)
            miles += traveled
            print("You traveled", traveled, "miles")
            tired += randint(1, 3)
            natives += randint(7, 14)
        elif (choice == "b"):
            thirst += 1
            traveled = randint(5, 12)
            miles += traveled
            print("You traveled", traveled, "miles")
            tired += 1
            natives += randint(7, 14)
        elif (choice == "a"):
            if (drinks <= 0):
                print("No drinks left, choose a different option")
                continue
            else:
                thirst = 0
                drinks -= 1
        else:
            print("Invalid choice, choose a different option")
            continue
        if (thirst > 6):
            print("You died of thirst!")
            done = True
            continue
        if (thirst > 4):
            print("You are thirsty")
        if (tired > 8):
            print("Your camel is dead!")
            done = True
            continue
        if (tired > 5):
            print("Your camel is getting tired")
        if (natives >= miles):
            print("You have been caught by the natives")
            done = True
            continue
        if (miles - natives < 15):
            print("The natives are getting close!")
        if (miles >= 200):
            print("You traveled over 200 miles and won!")
            done = True
            continue
        if (randint(1, 20) == 5):
            print("You found an oasis!")
            drinks = 3
            thirst = 0
            tired = 0


if __name__ == "__main__":
    main()
