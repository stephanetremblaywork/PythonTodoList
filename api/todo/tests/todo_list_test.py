from unittest import TestCase
from api.todo.todo_item import TodoItem

from api.todo.todo_list import TodoList

class TodoListTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self) -> None:
        todoList = TodoList()
        self.assertEqual(len(todoList._todoList), 0)

        todoItem0 = TodoItem(True, "todoItem0")
        todoItem1 = TodoItem(False, "todoItem1")
        todoItem2 = TodoItem(True, "todoItem2")
        todoListItems = [todoItem0, todoItem1, todoItem2]
        todoList = TodoList(todoListItems)
        self.assertListEqual(todoList._todoList, todoListItems)

        with self.assertRaises(TypeError):
            todoList = TodoList(1024)

    def test_getAllItems(self) -> None:
        todoListItems = []
        todoList = TodoList()
        self.assertListEqual(todoList.getAllItems(), todoListItems)

        todoItem0 = TodoItem(True, "todoItem0")
        todoItem1 = TodoItem(False, "todoItem1")
        todoItem2 = TodoItem(True, "todoItem2")
        todoListItems += [todoItem0, todoItem1, todoItem2]
        todoList = TodoList(todoListItems)
        self.assertListEqual(todoList.getAllItems(), todoListItems)

    def test_getNotDoneItems(self) -> None:
        todoItemList = []
        todoList = TodoList()
        self.assertListEqual(todoList.getNotDoneItems(), todoItemList)

        todoItem0 = TodoItem(True, "todoItem0")
        todoItem1 = TodoItem(False, "todoItem1")
        todoItem2 = TodoItem(True, "todoItem2")
        todoItem3 = TodoItem(True, "todoItem3")
        todoItem4 = TodoItem(False, "todoItem4")
        todoItemList += [todoItem0, todoItem1, todoItem2, todoItem3, todoItem4]
        todoItemsNotDoneList = [todoItem1, todoItem4]
        todoList = TodoList(todoItemList)
        self.assertListEqual(todoList.getNotDoneItems(), todoItemsNotDoneList)

    def test_getDoneItems(self) -> None:
        todoItemList = []
        todoList = TodoList()
        self.assertListEqual(todoList.getDoneItems(), todoItemList)

        todoItem0 = TodoItem(True, "todoItem0")
        todoItem1 = TodoItem(False, "todoItem1")
        todoItem2 = TodoItem(True, "todoItem2")
        todoItem3 = TodoItem(True, "todoItem3")
        todoItem4 = TodoItem(False, "todoItem4")
        todoItemList += [todoItem0, todoItem1, todoItem2, todoItem3, todoItem4]
        todoItemsDoneList = [todoItem0, todoItem2, todoItem3]
        todoList = TodoList(todoItemList)
        self.assertListEqual(todoList.getDoneItems(), todoItemsDoneList)

    def test_getItemAtPosition(self) -> None:
        todoItemList = []
        todoList = TodoList()
        with self.assertRaises(IndexError):
            todoList.getItemAtPosition(0)

        with self.assertRaises(TypeError):
            todoList.getItemAtPosition(3.1416)

        todoItem0 = TodoItem(True, "todoItem0")
        todoItem1 = TodoItem(False, "todoItem1")
        todoItem2 = TodoItem(True, "todoItem2")
        todoItem3 = TodoItem(True, "todoItem3")
        todoItem4 = TodoItem(False, "todoItem4")
        todoItemList += [todoItem0, todoItem1, todoItem2, todoItem3, todoItem4]
        todoList = TodoList(todoItemList)
        self.assertEqual(todoList.getItemAtPosition(2), todoItem2)

    def test_addTodoItem(self) -> None:
        todoItem0 = TodoItem(True, "todoItem0")
        todoItem1 = TodoItem(False, "todoItem1")
        todoItem2 = TodoItem(True, "todoItem2")
        todoItem3 = TodoItem(True, "todoItem3")
        todoItem4 = TodoItem(False, "todoItem4")
        todoItemList = [todoItem0, todoItem1, todoItem2, todoItem3, todoItem4]
        newTodoItem = TodoItem(True, "newTodoItem")
        todoList = TodoList(todoItemList)
        assert (len(todoList._todoList) == 5)
        todoList.addTodoItem(newTodoItem)
        self.assertEquals(todoList._todoList[5], newTodoItem)

    def test_moveItem(self) -> None:
        todoItem0 = TodoItem(True, "todoItem0")
        todoItem1 = TodoItem(False, "todoItem1")
        todoItem2 = TodoItem(True, "todoItem2")
        todoItem3 = TodoItem(True, "todoItem3")
        todoItem4 = TodoItem(False, "todoItem4")
        todoItemListBefore = [todoItem0, todoItem1, todoItem2, todoItem3, todoItem4]
        todoItemListAfter = [todoItem0, todoItem1, todoItem3, todoItem2, todoItem4]
        todoList = TodoList(todoItemListBefore)
        todoList.moveItem(3,2)
        self.assertListEqual(todoList._todoList, todoItemListAfter)
        