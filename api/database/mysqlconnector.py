import mysql.connector
from api.database.dbinterface import DBInterface
from api.todo.todo_list import TodoList

class MySQLConnector(DBInterface, object):
    def __new__(cls, connectionPoolConfig):
        if (not hasattr(cls, instance)):
            cls.instance = super(MySQLConnector, cls).__new__(cls, connectionPoolConfig)
        
        cls.instance._setConnectionPoolConfig(connectionPoolConfig)
        return cls.instance

    def __init__(self, connectionPoolConfig):
        self._connectionPool = None
        self._connection = None
        self._poolName = "MySQLConnectionPool"
        self._poolSize = 3
        self._initializeConnectionPool()

    def _dbConnect(self) -> None:
        self._connection = self._connectionPool.get_connection()
    
    def _dbDisconnect(self) -> None:
        self._connection.close()

    def _setConnectionPoolConfig(self, connectionPoolConfig) -> None:
        if (isinstance(connectionPoolConfig, dict)):
            self._connectionPool.set_config(**self._connectionProperties)
        else:
            raise TypeError("Wrong type. Expecting 'dict' object.")

    def _initializeConnectionPool(self, connectionPoolConfig) -> None:
        if (self._connectionPool is not None):
            self._connectionPool

        self._connectionPool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name = self._poolName,
            pool_size = self._poolSize
        )

        self._setConnectionPoolConfig(connectionPoolConfig)

    def loadTodoList(self, name) -> TodoList:
        self._dbConnect()
        # Do stuff
        self._dbDisconnect()

    def saveTodoList(self, todoList) -> None:
        self._dbConnect()
        # Do stuff
        self._dbDisconnect()