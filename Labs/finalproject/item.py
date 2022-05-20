from room import Room


class Item:
    # Name: String key representing the room
    # Adj: Adjacent rooms that are accessible from this room
    def __init__(self, name="", room=None):
        self._name = name
        self._room = room

    def getRoom(self):
        return self._room

    def setRoom(self, room):
        self._room = room

    def getName(self):
        return self._name

    def __eq__(self, __o: object) -> bool:
        if __o.getName() == self._name and __o.getRoom() == self._room:
            return True
        else:
            return False

    def __str__(self) -> str:
        return "Item " + self._name + " in " + self._room.getName()

    def __repr__(self) -> str:
        return self.__str__()
