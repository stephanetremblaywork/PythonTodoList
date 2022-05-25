import mysql.connector
from api.data.dbinterface import DBInterface
from api.data.connectionproperties import ConnectionProperties
from api.todo.todo_list import TodoList

class MySQLConnector(DBInterface):
    def __init__(self, connectionProperties):
        self._connection = None
        self.setConnectionProperties(connectionProperties)

    def _dbConnect(self) -> None:
        self._connection = mysql.connector.connect(
            user=self._connectionProperties.getUser(),
            password=self._connectionProperties.getPassword,
            host=self._connectionProperties.getHost(),
            database=self._connectionProperties.getDbName())
    
    def _dbDisconnect(self) -> None:
        self._connection.close()

    def setConnectionProperties(self, connectionProperties) -> None:
        if (isinstance(connectionProperties, ConnectionProperties)):
            self._connectionProperties = connectionProperties
        else:
            raise TypeError("Wrong type. Expecting ConnectionProperties object.")
    
    def loadTodoList(self, name) -> TodoList:
        self._dbConnect()
        # Do stuff
        self._dbDisconnect()

    def saveTodoList(self, todoList) -> None:
        self._dbConnect()
        # Do stuff
        self._dbDisconnect()