from unittest import TestSuite
from unittest import TextTestRunner
from api.todo.tests.todo_item_test import TodoItemTestCase
from api.todo.tests.todo_list_test import TodoListTestCase

def getTodoTestSuite():
    suite = TestSuite()
    suite.addTest(TodoItemTestCase('Basic ToDoItem class unit tests.'))
    suite.addTest(TodoListTestCase('Basic ToDoList class unit tests.'))
    return suite

if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(getTodoTestSuite())
