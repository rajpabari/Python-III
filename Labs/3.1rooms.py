# Raj Pabari Python III
# Note, I approached this prompt as a graph with adjacency matrix rather than 2D list

class Room:
    # Name: String key representing the room
    # Adj: Adjacent rooms that are accessible from this room
    def __init__(self, name="", adj=[]):
        self._name = name
        self._adj = adj

    def getAdj(self):
        return self._adj

    def setAdj(self, adj):
        self._adj = adj

    def getName(self):
        return self._name


def main():
    # Create structure using given information in prompt
    rooms = [Room("Bedroom Two"), Room("South Hall"), Room("Dining Room"),
             Room("Bedroom One"), Room("North Hall"), Room("Kitchen"), Room("Balcony")]
    rooms[0].setAdj([rooms[1], rooms[3]])
    rooms[1].setAdj([rooms[0], rooms[2], rooms[4]])
    rooms[2].setAdj([rooms[1], rooms[5]])
    rooms[3].setAdj([rooms[0], rooms[4]])
    rooms[4].setAdj([rooms[1], rooms[3], rooms[5], rooms[6]])
    rooms[5].setAdj([rooms[2], rooms[4]])
    rooms[6].setAdj([rooms[4]])

    done = False
    currentRoom = rooms[0]

    while not done:
        counter = 1
        print("\nYou are currently in", currentRoom.getName())
        print("You can now travel to the following places by typing their number, or type q to quit.")
        for i in currentRoom.getAdj():
            print(str(counter) + ") " + i.getName())
            counter += 1
        choice = input("Where would you like to go? ").casefold()
        if choice == "q":
            done = True
            break
        else:
            index = int(choice) - 1
            currentRoom = currentRoom.getAdj()[index]


if __name__ == "__main__":
    main()
