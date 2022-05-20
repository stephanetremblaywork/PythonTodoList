class TodoItem():

    def __init__(self, position = 0, isDone = False, description = "") -> None:
        if (isinstance(position, int) and isinstance(isDone, bool) and isinstance(description, str)):
            self._position = position
            self._isDone = isDone
            self._description = description
        else:
            raise TypeError("Invalid types.")
        
    def setIsDone(self, isDone) -> None:
        if (isinstance(isDone, bool)):
            self._isDone = isDone
        else:
            raise TypeError("Invalid Type")
    
    def setPosition(self, position) -> None:
        if (isinstance(position, int)):
            self._position = position
        else:
            raise TypeError("Invalid Type")
    
    def setDescription(self, description = "") -> None:
        if (isinstance(description, str)):
            self._description = description
        else:
            raise TypeError("Invalid type.")
    
    def getIsDone(self) -> bool:
        return self._isDone

    def getPosition(self) -> int:
        return self._position

    def getDescription(self) -> str:
        return self._description
