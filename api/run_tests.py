from unittest import TestSuite
from unittest import TextTestRunner
from api.todo.tests.todo_item_test import TodoItemTestCase
from api.todo.tests.todo_list_test import TodoListTestCase
from api.data.tests.mysqlconnector_test import MySQLConnectorTestCase

def getTestSuite():
    suite = TestSuite()

    todoItemTests = [ m for m in dir(TodoItemTestCase) if m.startswith('test_')]
    todoListTests = [ m for m in dir(TodoListTestCase) if m.startswith('test_')]
    mysqlConnectorTests = [ m for m in dir(MySQLConnectorTestCase) if m.startswith('test')]

    for test in todoItemTests:
        suite.addTest(TodoItemTestCase(test))

    for test in todoListTests:
        suite.addTest(TodoListTestCase(test))
        
    for test in todoListTests:
        suite.addTest(mysqlConnectorTests(test))

    return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(getTestSuite())
