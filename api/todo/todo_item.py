class TodoItem():

    def __init__(self, isDone = False, description = "") -> None:
        if (isinstance(isDone, bool) and isinstance(description, str)):
            self._isDone = isDone
            self._description = description
        else:
            raise TypeError("Invalid types.")

    def setIsDone(self, isDone) -> None:
        if (isinstance(isDone, bool)):
            self._isDone = isDone
        else:
            raise TypeError("Invalid Type")
    
    def setDescription(self, description = "") -> None:
        if (isinstance(description, str)):
            self._description = description
        else:
            raise TypeError("Invalid type.")
    
    def getIsDone(self) -> bool:
        return self._isDone

    def getDescription(self) -> str:
        return self._description
