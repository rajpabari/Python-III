def main():
    SIZE = 5
    arr = []
    print("This program takes", SIZE, "numbers and prints them in an array")
    for i in range(SIZE):
        arr.append(int(input("Give your number (#"+str(i+1)+"): ")))
    print(arr)


if __name__ == "__main__":
    main()
