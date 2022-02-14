# Raj Pabari Python III

from random import randint


def min3(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


def box(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*", end=" ")
        print()


def find(arr, toFind):
    for index, i in enumerate(arr):
        if i == toFind:
            print("Found", i, "at index", index)


def createList(size):
    randNums = []
    for i in range(size):
        randNums.append(randint(1, 6))
    return randNums


def countList(arr, x):
    ans = 0
    for i in arr:
        if i == x:
            ans += 1
    return ans


def averageList(arr):
    return float(sum(arr)) / float(len(arr))


def main():
    print(min3(4, 7, 5))
    print(min3(4, 5, 5))
    print(min3(4, 4, 4))
    print(min3(-2, -6, -100))
    print(min3("Z", "B", "A"))
    print()

    box(7, 5)  # Print a box 7 high, 5 across
    print()   # Blank line
    box(3, 2)  # Print a box 3 high, 2 across
    print()   # Blank line
    box(3, 10)  # Print a box 3 high, 10 across
    print()

    my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19,
               3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
    find(my_list, 12)
    find(my_list, 91)
    find(my_list, 80)
    print()

    print(createList(5))
    print()

    count = countList([1, 2, 3, 3, 3, 4, 2, 1], 3)
    print(count)
    print()

    avg = averageList([1, 2, 3])
    print(avg)
    print()

    arr = createList(10000)
    for i in range(0, 6):
        print("Number of times", i+1, "appears in list:", countList(arr, i+1))
    print("Average of the 10000 numbers:", averageList(arr))


if __name__ == "__main__":
    main()
