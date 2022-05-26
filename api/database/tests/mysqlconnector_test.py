import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from api.database.mysqlconnector import MySQLConnector
from api.database.connectionproperties import ConnectionProperties
from api.todo.todo_item import TodoItem
from api.todo.todo_list import TodoList

class MySQLConnectorTestCase(TestCase):

    def setUp(self) -> None:
        self._connectionProperties = {
            "database"  : "someDataBase",
            "user"      : "someUser",
            "password"  : "somePassword"
        }

    def tearDown(self) -> None:
        pass

    def test_new(self) -> None:
        self.fail("Not yet implemented.")

    def test_loadTodoList(self) -> None:
        self.fail("Not yet implemented.")

    def test_saveTodoList(self) -> None:
        self.fail("Not yet implemented.")

if __name__ == '__main__':
    unittest.main()