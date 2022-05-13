class ToDoItem():

    def __init__(self, isDone = False, description = "") -> None:
        if (isDone is bool and description is str):
            self._isDone = isDone
            self._description = description
        else:
            raise TypeError("Invalid types.")

    def setDone(self) -> None:
        self._isDone = True
    
    def setNotDone(self) -> None:
        self._isDone = False

    def setDescription(self, description = "") -> None:
        if (description is str):
            self._description = description
        else:
            raise TypeError("Invalid type.")
    
    def getDone(self) -> bool:
        return self._isDone

    def getDescription(self) -> str:
        return self._description
