# Raj Pabari Python III

def main():
    print("Welcome to a five question quiz!\n")

    correct = 0.0
    questions = 5.0

    if (input("1) What is the program author's first name?\n").casefold() == "raj"):
        print("Correct")
        correct += 1.0
    else:
        print("Incorrect")

    if (input("2) What is the language this program is written in?\n").casefold() == "python"):
        print("Correct")
        correct += 1.0
    else:
        print("Incorrect")

    if (input("3) Which of these is equal to 10^2?\nA)100\nB)1000\nC)10000\n").casefold() == "a"):
        print("Correct!")
        correct += 1.0
    else:
        print("Incorrect")

    if (int(input("4) What is 5+5?\n")) == 10):
        print("Correct!")
        correct += 1.0
    else:
        print("Incorrect")

    if (int(input("5) What is 9/3?\n")) == 3):
        print("Correct!")
        correct += 1.0
    else:
        print("Incorrect")

    print("Your score is", int((correct/questions)*100.0), "%")


if __name__ == "__main__":
    main()
