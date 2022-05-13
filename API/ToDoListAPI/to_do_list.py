from typing import List

from API.ToDoListAPI.to_do_item import ToDoItem


class ToDoList():

    def __init__(self) -> None:
        self.toDoList = List()

    def __init__(self, toDoList) -> None:
        if (toDoList is List):
            self.toDoList = toDoList
        else:
            raise TypeError("Invalid type.")

    def getAllItems(self) -> List:
        return self.toDoList

    def getNotDoneItems(self) -> List:
        return list(filter(lambda x: (x.isDone == False), self.toDoList))

    def getDoneItems(self) -> List:
        return list(filter(lambda x: (x.isDone == True), self.toDoList))

    def getItemAtPosition(self, position) -> ToDoItem:
        if (position is int):
            return self.toDoList[position]
        else:
            raise TypeError("Invalid type.")

    def addToDoItem(self, toDoItem) -> None:
        if (toDoItem is ToDoItem):
            self.toDoList.append(toDoItem)
        elif ():
            raise TypeError("Invalid type.")

    def addToDoItem(self, isDone = False, description = "") -> None:
        self.toDoList.append(ToDoItem(isDone, description))

    def moveItem(self, oldPosition, newPosition) -> None:
        self.toDoList.insert(newPosition, self.toDoList.pop(oldPosition))
    