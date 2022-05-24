import unittest
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
        self.assertListEqual(todoList._todoList, [])
        self.assertEqual(todoList._name, "")

        name = "My Todo List"

        todoList = TodoList(name=name)
        self.assertEqual(todoList._name, name)
        self.assertListEqual(todoList._todoList, [])

        todoItem0 = TodoItem(isDone=True, description="todoItem0")
        todoItem1 = TodoItem(isDone=False, description="todoItem1")
        todoItem2 = TodoItem(isDone=True, description="todoItem2")
        todoItem3 = TodoItem(isDone=True, description="todoItem3")
        todoItem4 = TodoItem(isDone=False, description="todoItem4")
        todoItemList = [todoItem4, todoItem2, todoItem1, todoItem3, todoItem0]

        todoList = TodoList(todoList=todoItemList)
        self.assertEqual(todoList._name, "")
        self.assertListEqual(todoList._todoList, todoItemList)

        todoList = TodoList(name=name, todoList=todoItemList)
        self.assertEqual(todoList._name, name)
        self.assertListEqual(todoList._todoList, todoItemList)

        with self.assertRaises(TypeError):
            todoList = TodoList(1024)
        
        with self.assertRaises(TypeError):
            todoList = TodoList(todoItemList)

        with self.assertRaises(TypeError):
            todoList = TodoList(name=1024)

        with self.assertRaises(TypeError):
            todoList = TodoList(todoList="Hello World")

    def test_getAllItems(self) -> None:
        todoItemList = []
        todoList = TodoList()
        self.assertListEqual(todoList.getAllItems(), todoItemList)

        todoItem0 = TodoItem(isDone=True, description="todoItem0")
        todoItem1 = TodoItem(isDone=False, description="todoItem1")
        todoItem2 = TodoItem(isDone=True, description="todoItem2")
        todoItem3 = TodoItem(isDone=True, description="todoItem3")
        todoItem4 = TodoItem(isDone=False, description="todoItem4")
        todoItemList = [todoItem0, todoItem1, todoItem2, todoItem3, todoItem4]
        todoList = TodoList(todoList=todoItemList)
        self.assertListEqual(todoList.getAllItems(), todoItemList)

    def test_getNotDoneItems(self) -> None:
        todoItemList = []
        todoList = TodoList()
        self.assertListEqual(todoList.getNotDoneItems(), todoItemList)

        todoItem0 = TodoItem(isDone=True, description="todoItem0")
        todoItem1 = TodoItem(isDone=False, description="todoItem1")
        todoItem2 = TodoItem(isDone=True, description="todoItem2")
        todoItem3 = TodoItem(isDone=True, description="todoItem3")
        todoItem4 = TodoItem(isDone=False, description="todoItem4")
        todoItemList = [todoItem0, todoItem1, todoItem2, todoItem3, todoItem4]
        todoItemsNotDoneList = [todoItem1, todoItem4]
        todoList = TodoList(todoList=todoItemList)
        self.assertListEqual(todoList.getNotDoneItems(), todoItemsNotDoneList)

    def test_getDoneItems(self) -> None:
        todoItemList = []
        todoList = TodoList()
        self.assertListEqual(todoList.getDoneItems(), todoItemList)

        todoItem0 = TodoItem(isDone=True, description="todoItem0")
        todoItem1 = TodoItem(isDone=False, description="todoItem1")
        todoItem2 = TodoItem(isDone=True, description="todoItem2")
        todoItem3 = TodoItem(isDone=True, description="todoItem3")
        todoItem4 = TodoItem(isDone=False, description="todoItem4")
        todoItemList += [todoItem0, todoItem1, todoItem2, todoItem3, todoItem4]
        todoItemsDoneList = [todoItem0, todoItem2, todoItem3]
        todoList = TodoList(todoList=todoItemList)
        self.assertListEqual(todoList.getDoneItems(), todoItemsDoneList)

    def test_getItemAtPosition(self) -> None:
        todoItemList = []
        todoList = TodoList()
        with self.assertRaises(IndexError):
            todoList.getItemAtPosition(0)

        with self.assertRaises(TypeError):
            todoList.getItemAtPosition(3.1416)

        todoItem0 = TodoItem(isDone=True, description="todoItem0")
        todoItem1 = TodoItem(isDone=False, description="todoItem1")
        todoItem2 = TodoItem(isDone=True, description="todoItem2")
        todoItem3 = TodoItem(isDone=True, description="todoItem3")
        todoItem4 = TodoItem(isDone=False, description="todoItem4")
        todoItemList += [todoItem0, todoItem1, todoItem2, todoItem3, todoItem4]
        todoList = TodoList(todoList=todoItemList)
        self.assertEqual(todoList.getItemAtPosition(2), todoItem2)

    def test_addTodoItem(self) -> None:
        todoItem0 = TodoItem(isDone=True, description="todoItem0")
        todoItem1 = TodoItem(isDone=False, description="todoItem1")
        todoItem2 = TodoItem(isDone=True, description="todoItem2")
        todoItem3 = TodoItem(isDone=True, description="todoItem3")
        todoItem4 = TodoItem(isDone=False, description="todoItem4")
        todoItemList = [todoItem0, todoItem1, todoItem2, todoItem3, todoItem4]
        todoItemListLength = len(todoItemList)
        todoList = TodoList(todoList=todoItemList)
        
        newTodoItem = TodoItem(isDone=True, description="newTodoItem")
        self.assertTrue (len(todoList._todoList) == todoItemListLength)
        todoList.addTodoItem(newTodoItem)
        self.assertTrue (len(todoList._todoList) == todoItemListLength + 1)
        self.assertEquals(todoList._todoList[-1], newTodoItem)

        newTodoItem = TodoItem(isDone=True, description="Item at position 3.")
        todoList.addTodoItem(newTodoItem)
        self.assertEquals(todoList._todoList[-1], newTodoItem)

    def test_moveItem(self) -> None:
        todoItem0 = TodoItem(isDone=True, description="todoItem0")
        todoItem1 = TodoItem(isDone=False, description="todoItem1")
        todoItem2 = TodoItem(isDone=True, description="todoItem2")
        todoItem3 = TodoItem(isDone=True, description="todoItem3")
        todoItem4 = TodoItem(isDone=False, description="todoItem4")
        todoItemListBefore = [todoItem0, todoItem1, todoItem2, todoItem3, todoItem4]
        todoItemListAfter = [todoItem0, todoItem1, todoItem3, todoItem2, todoItem4]
        todoList = TodoList(todoList=todoItemListBefore)
        todoList.moveItem(3, 2)
        self.assertListEqual(todoList._todoList, todoItemListAfter)

    def test_setName(self) -> None:
        name = "My Todo List"
        todoList = TodoList()
        todoList.setName(name)
        self.assertEqual(todoList._name, name)

    def test_getName(self) -> None:
        name = "My Todo List"
        todoList = TodoList()
        todoList.setName(name)
        self.assertEqual(todoList.getName(), name)

if __name__ == '__main__':
    unittest.main()