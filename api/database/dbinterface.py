from api.todo.todo_list import TodoList

class DBInterface():

    def setConnectionProperties(self, connectionProperties) -> None:
        pass

    def loadTodoList(self, name) -> TodoList:
        pass

    def saveTodoList(self, todoList) -> None:
        pass
