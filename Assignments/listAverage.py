
def main():
    arr = [3, 12, 3, 5, 3, 4, 6, 8, 5, 3, 5, 6, 3, 2, 4]
    sum = 0.0
    for i in arr:
        sum += i
    print(round(sum/float(len(arr)), 2))


if __name__ == "__main__":
    main()
