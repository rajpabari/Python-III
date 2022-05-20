# Raj Pabari Python III
from room import Room
from item import Item


def initRooms():
    rooms = [Room("Master Bedroom"), Room("South Hall"), Room("Dining Room"),
             Room("Guest Bedroom"), Room("North Hall"), Room(
                 "Kitchen"), Room("Balcony"),
             Room("Living Room"), Room("Garden"), Room("Garage"), Room("Inventory")]
    for index, room in enumerate(rooms):
        room.setId(index)

    rooms[0].setAdj([rooms[1], rooms[3]])
    rooms[1].setAdj([rooms[0], rooms[2], rooms[4], rooms[9]])
    rooms[2].setAdj([rooms[1], rooms[5], rooms[9]])
    rooms[3].setAdj([rooms[0], rooms[4], rooms[7], rooms[8]])
    rooms[4].setAdj([rooms[1], rooms[3], rooms[5], rooms[6]])
    rooms[5].setAdj([rooms[2], rooms[4], rooms[9]])
    rooms[6].setAdj([rooms[4], rooms[7]])
    rooms[7].setAdj([rooms[3], rooms[6], rooms[8]])
    rooms[8].setAdj([rooms[7], rooms[3]])
    rooms[9].setAdj([rooms[1], rooms[5], rooms[2]])

    rooms[-1].setId(-1)

    return rooms


def initItems(rooms):
    items = [Item("key", rooms[1]), Item("bandana", rooms[0]), Item("hat", rooms[0]),
             Item("plate", rooms[2]), Item("knife", rooms[5]),
             Item("pillow", rooms[3]), Item("napkin", rooms[2]),
             Item("binoculars", rooms[6]), Item("shears", rooms[8]),
             Item("remote", rooms[7]), Item("cushion", rooms[7]),
             Item("spoon", rooms[2]), Item("glasses", rooms[6]),
             Item("chest", rooms[9]), Item("mannequin", rooms[9])]

    return items


def lookRooms(adjacentRooms, roomName):
    print("The following rooms are adjacent to", roomName+":")
    counter = 1
    for i in adjacentRooms:
        print(str(counter) + ") " + i.getName())
        counter += 1


def lookItems(allItems, currentRoom):
    flag = False
    for item in allItems:
        if item.getRoom() == currentRoom:
            print("There is a \""+item.getName() +
                  "\" in the", currentRoom.getName()+".")
            flag = True
    if flag == False:
        print("There are no items in this room.")

    return flag


def lookInventory(inv):
    print("Your inventory contains the following items: ")
    for i in inv:
        print(str(i).strip().split()[1])


def addToInventory(item, allItems, inv, invRoom):
    for index, currentItem in enumerate(allItems):
        if item == currentItem:
            inv.append(currentItem)
            inv[-1].setRoom(invRoom)
            del allItems[index]
            return True
    return False


def dropFromInventory(userItem, allItems, inv, currentRoom):
    for index, item in enumerate(inv):
        if userItem == item.getName():
            allItems.append(item)
            allItems[-1].setRoom(currentRoom)
            del inv[index]
            return True
    return False


def help():
    print("You win if you can find the treasure, which you will discover if you are")
    print("holding the correct two items in your inventory at the same time.")
    print()
    print("You can type the following commands:")
    print("look - see items in your inventory, the items in this room, and the adjacent rooms")
    print("move - allows you to move to a different room")
    print("grab - allows you to pick up an item into your inventory (max capacity: 2 items)")
    print("drop - allows you to drop an item from your inventory")
    print("hint - gives you a series of hints but each hint costs moves")
    print("q - quit")
    print("help - displays this help menu")


def hint(inv):
    moveCount = 0
    answer = input(
        "Would you like to see hint 1 of 3 for the cost of 2 moves (y/n)? ").strip().casefold()
    if answer == "y" or answer == "yes":
        countCorrect = 0
        if len(inv) >= 1 and (inv[0].getName() == "key" or inv[0].getName() == "chest"):
            countCorrect += 1
        if len(inv) >= 2 and (inv[1].getName() == "chest" or inv[1].getName() == "chest"):
            countCorrect += 1
        print(countCorrect,
              "of the", len(inv), "items currently in your inventory are the correct items.")
        moveCount += 1
    else:
        return moveCount

    answer = input(
        "\nWould you like to see hint 2 of 3 for the cost of 2 moves (y/n)? ").strip().casefold()
    if answer == "y" or answer == "yes":
        print("One of the winning items is used inside the other. The items are usually used together.")
        moveCount += 2
    else:
        return moveCount

    answer = input(
        "\nWould you like to see hint 3 of 3 for the cost of 2 moves (y/n)? ").strip().casefold()
    if answer == "y" or answer == "yes":
        print("You will win this game if you pick up the \"key\" and the \"chest\".")
        moveCount += 2
    else:
        return moveCount
    return moveCount


def win(inv):
    if len(inv) != 2:
        return False
    if (inv[0].getName() == "key" or inv[1].getName() == "key"):
        if (inv[0].getName() == "chest" or inv[1].getName() == "chest"):
            return True
    return False


def main():
    # Create structure using given information in prompt
    rooms = initRooms()
    items = initItems(rooms)

    done = False
    currentRoom = rooms[0]

    inventory = []

    actionCount = 0
    loseCount = 50

    print("\nWelcome to Raj's text adventure game!")
    print("You can hold up to two items in your inventory at any given time.")
    print("You win if you can find the treasure, which you will discover if you are")
    print("holding the correct two items in your inventory at the same time.")
    print("But, time is tight! You lose if you use",
          loseCount, "moves without finding the treasure.")
    print()

    while not done:

        if win(inventory) == False and actionCount < loseCount:
            print("\nYou are currently in", currentRoom.getName())
            print("You have", loseCount-actionCount, "moves remaining.")
            choice = input(
                "What would you like to do? Type \"help\" for options or \"q\" to quit.\n").strip().casefold()
        print()

        if win(inventory) == True or actionCount >= loseCount or choice == "q" or choice == "quit":
            done = True
            break
        elif choice == "look":
            lookInventory(inventory)
            print()
            lookItems(items, currentRoom)
            print()
            lookRooms(currentRoom.getAdj(), currentRoom.getName())
        elif choice == "move":
            lookRooms(currentRoom.getAdj(), currentRoom.getName())
            print(
                "You can travel to any of the places above by typing their number.")
            roomChoice = input(
                "Where would you like to go? ").strip().casefold()
            try:
                index = int(roomChoice) - 1
                if (index+1) > len(currentRoom.getAdj()) or index < 0:
                    raise IndexError
                else:
                    currentRoom = currentRoom.getAdj()[index]
            except:
                print("Invalid room number, please try again.")
                actionCount -= 1

        elif choice == "grab":
            if len(inventory) >= 2:
                print(
                    "Your inventory is full! Please drop an item before picking up another item.")
                actionCount -= 1
            elif lookItems(items, currentRoom) == True:
                userItem = input(
                    "Type the name of the item you would like to grab: ").strip().casefold()
                if addToInventory(
                        Item(userItem, currentRoom), items, inventory, rooms[-1]) == True:
                    print("Successfully added", userItem, "to inventory.")
                else:
                    print("Could not find", userItem,
                          "in this room. Please try again.")
                    actionCount -= 1
        elif choice == "drop":
            if len(inventory) <= 0:
                print("You are not currently holding any items.")
                actionCount -= 1
            else:
                lookInventory(inventory)
                userItem = input(
                    "Type the name of the item you would like to drop: ").strip().casefold()
                if dropFromInventory(
                        userItem, items, inventory, currentRoom) == True:
                    print("Successfully dropped", userItem, "from inventory.")
                else:
                    print("Could not drop", userItem,
                          "from inventory. Please try again.")
                    actionCount -= 1
        elif choice == "hint":
            moveCount = hint(inventory)
            print("Those", int((moveCount+1)/2), "hints cost you",
                  moveCount+1, "moves in total.")
            actionCount += moveCount
        elif choice == "help":
            actionCount -= 1
            help()
        else:
            actionCount -= 1
            print("Sorry, I don't recognize that command.\n")
            help()
        actionCount += 1

    if win(inventory) == True:
        print()
        print("Congratulations! You used the key to unlock the chest and discovered the treasure.")
        print("You won in", actionCount,
              "moves. The best possible score is 4 moves.")
    else:
        print()
        print("You lost! You took", actionCount,
              "of", loseCount, "moves and did not find the treasure.")


if __name__ == "__main__":
    main()
