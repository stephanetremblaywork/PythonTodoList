from api.todo.todo_item import ToDoItem

class ToDoList():

    def __init__(self) -> None:
        self._toDoList = []

    def __init__(self, toDoList) -> None:
        if (toDoList is list):
            self._toDoList = toDoList
        else:
            raise TypeError("Invalid type.")

    def getAllItems(self) -> list:
        return self._toDoList

    def getNotDoneItems(self) -> list:
        return list(filter(lambda x: (x.isDone == False), self._toDoList))

    def getDoneItems(self) -> list:
        return list(filter(lambda x: (x.isDone == True), self._toDoList))

    def getItemAtPosition(self, position) -> ToDoItem:
        if (position is int):
            return self._toDoList[position]
        else:
            raise TypeError("Invalid type.")

    def addToDoItem(self, toDoItem) -> None:
        if (toDoItem is ToDoItem):
            self._toDoList.append(toDoItem)
        elif ():
            raise TypeError("Invalid type.")

    def addToDoItem(self, isDone = False, description = "") -> None:
        self._toDoList.append(ToDoItem(isDone, description))

    def moveItem(self, oldPosition, newPosition) -> None:
        self._toDoList.insert(newPosition, self._toDoList.pop(oldPosition))
    