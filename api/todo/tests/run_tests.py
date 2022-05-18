from unittest import TestSuite
from unittest import TextTestRunner
from api.todo.tests.todo_item_test import ToDoItemTestCase
from api.todo.tests.todo_list_test import ToDoListTestCase

def getTodoTestSuite():
    suite = TestSuite()
    suite.addTest(ToDoItemTestCase('Basic ToDoItem class unit tests.'))
    suite.addTest(ToDoListTestCase('Basic ToDoList class unit tests.'))
    return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(getTodoTestSuite())
