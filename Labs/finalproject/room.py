class Room:
    # Name: String key representing the room
    # Adj: Adjacent rooms that are accessible from this room
    def __init__(self, name="", adj=[], id=-1):
        self._name = name
        self._adj = adj
        self._id = id

    def getAdj(self):
        return self._adj

    def setAdj(self, adj):
        self._adj = adj

    def getName(self):
        return self._name

    def setId(self, id):
        self._id = id

    def getId(self):
        return id

    def __str__(self) -> str:
        return "Room " + self._name + " id " + self._id

    def __repr__(self) -> str:
        return self.__str__()
