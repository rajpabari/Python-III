def helloWorld():
    print("Hello World")


def hello(name):
    print("Hello", name)


def multiply(a, b):
    return (a * b)


def printRepeated(phrase, count):
    for i in range(count):
        print(phrase)


def getSquare(x):
    return x ** 2


def getCentrifugal(m, v, r):
    return round(m * v ** 2 / float(r), 3)


def printList(arr):
    for i in arr:
        print(i)


def main():
    helloWorld()
    hello("Bob")
    print(multiply(10, 20))
    printRepeated("Hello", 5)
    print(getSquare(10))
    print(getCentrifugal(10, 2, 3))
    printList([1, 2, 3, 4, 5])


if __name__ == "__main__":
    main()
