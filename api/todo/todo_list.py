from api.todo.todo_item import TodoItem

class TodoList():

    def __init__(self, name = "", todoList = []) -> None:
        if (isinstance(name, str) and isinstance(todoList, list)):
            self._name = name
            self._todoList = todoList
        else:
            raise TypeError("Invalid type.")

    def setName(self, name) -> None:
        if (isinstance(name, str)):
            self._name = name
        else:
            raise TypeError("Invalid type.")

    def getName(self) -> str:
        return self._name

    def getAllItems(self) -> list:
        return self._todoList

    def getNotDoneItems(self) -> list:
        if (len(self._todoList) == 0):
            return []

        return list(filter(lambda x: (x.getIsDone() == False), self._todoList))

    def getDoneItems(self) -> list:
        if (len(self._todoList) == 0):
            return []

        return list(filter(lambda x: (x.getIsDone() == True), self._todoList))

    def getItemAtPosition(self, position) -> TodoItem:
        if (isinstance(position,int)):
            if (len(self._todoList) == 0):
                raise IndexError("Index out of range")

            return self._todoList[position]
        else:
            raise TypeError("Invalid type.")

    def addTodoItem(self, toDoItem = TodoItem(False, "")) -> None:
        if (isinstance(toDoItem, TodoItem)):
            self._todoList.append(toDoItem)
        elif ():
            raise TypeError("Invalid type.")

    def moveItem(self, oldPosition, newPosition) -> None:
        if (isinstance(oldPosition, int) and isinstance(newPosition, int)):
            self._todoList.insert(newPosition, self._todoList.pop(oldPosition))
        else:
            raise TypeError("Invalid types.")
