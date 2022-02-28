
class Dog:
    def __init__(self) -> None:
        self.age = 0
        self.weight = 0
        self.name = ""


class Animal:
    def __init__(self) -> None:
        self.name = ""
        print("An animal has been born")

    def eat(self):
        print("Munch Munch")

    def makeNoise(self):
        print("Grrr says", self.name)


def main():
    dog = Dog()
    dog.age = 10
    dog.weight = 100
    dog.name = "Fido"

    animal = Animal()


if __name__ == "__main__":
    main()
