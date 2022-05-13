class ToDoItem():

    def __init__(self, isDone = False, description = "") -> None:
        if (isDone is bool and description is str):
            self.isDone = isDone
            self.description = description
        else:
            raise TypeError("Invalid types.")

    def __init__(self) -> None:
        pass

    def setDone(self) -> None:
        self.isDone = True
    
    def setNotDone(self) -> None:
        self.isDone = False

    def setDescription(self, description = "") -> None:
        if (description is str):
            self.description = description
        else:
            raise TypeError("Invalid type.")
    
    def getDone(self) -> bool:
        return self.isDone

    def getDescription(self) -> str:
        return self.description
