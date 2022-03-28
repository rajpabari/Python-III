import re

ALICE_LOCATION = "./Labs/11.1searching/AliceInWonderland200.txt"
DICTIONARY_LOCATION = "./Labs/11.1searching/Dictionary.txt"


def splitLine(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    aliceText = open(ALICE_LOCATION, "r")
    dictionaryFile = open(DICTIONARY_LOCATION, "r")
    dictionary = set()
    for i in dictionaryFile:
        dictionary.add(i.strip().lower())
    lineNumber = 0
    for line in aliceText:
        lineNumber += 1
        for word in splitLine(line):
            if word.lower() not in dictionary:
                print("Line", lineNumber, "possible misspelled word:", word)

    dictionaryFile.close()
    aliceText.close()


if __name__ == "__main__":
    main()
