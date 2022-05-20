import unittest
from unittest import TestCase
from api.todo.todo_item import TodoItem

class TodoItemTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self) -> None:
        itemDescription = "DESCRIPTION"
        itemIsDone = True

        todoItem = TodoItem()
        self.assertEqual(todoItem._position, 0)
        self.assertEqual(todoItem._description, "")
        self.assertEqual(todoItem._isDone, False)

        todoItem = TodoItem(position=2)
        self.assertEqual(todoItem._position, 2)
        self.assertEqual(todoItem._description, "")
        self.assertEqual(todoItem._isDone, False)
        
        todoItem = TodoItem(isDone=True)
        self.assertEqual(todoItem._position, 0)
        self.assertEqual(todoItem._description, "")
        self.assertEqual(todoItem._isDone, True)

        todoItem = TodoItem(description=itemDescription)
        self.assertEqual(todoItem._position, 0)
        self.assertEqual(todoItem._description, itemDescription)
        self.assertEqual(todoItem._isDone, False)

        todoItem = TodoItem(isDone=itemIsDone, description=itemDescription)
        self.assertEqual(todoItem._description, itemDescription)
        self.assertEqual(todoItem._isDone, itemIsDone)

        with self.assertRaises(TypeError):
            TodoItem(isDone="string argument")
        
        with self.assertRaises(TypeError):
            TodoItem(description=1024)

    def test_setPosition(self) -> None:
        position = 4
        todoItem = TodoItem()
        todoItem.setPosition(position)
        self.assertEqual(todoItem._position, position)

        with self.assertRaises(TypeError):
            todoItem.setPosition("Not a position")

    def test_setIsDone(self) -> None:
        isDone = True
        todoItem = TodoItem()
        todoItem.setIsDone(isDone)
        self.assertEqual(todoItem._isDone, isDone)

        isDone = False
        todoItem.setIsDone(isDone)
        self.assertEqual(todoItem._isDone, isDone)

        with self.assertRaises(TypeError):
            todoItem.setIsDone("string argument")
    
    def test_setDescription(self) -> None:
        description = "DESCRIPTION"
        todoItem = TodoItem()
        todoItem.setDescription(description)
        self.assertEqual(todoItem._description, description)

        with self.assertRaises(TypeError):
            self.test_setDescription(1024)

    def test_getPosition(self) -> None:
        position = 4
        todoItem = TodoItem()
        todoItem.setPosition(position)
        self.assertEqual(todoItem.getPosition(), position)

    def test_getIsDone(self) -> bool:
        isDone = True
        todoItem = TodoItem(isDone=isDone)
        self.assertEqual(todoItem.getIsDone(), isDone)

    def test_getDescription(self) -> str:
        description = "DESCRIPTION"
        todoItem = TodoItem(description=description)
        self.assertEqual(todoItem.getDescription(), description)

if __name__ == '__main__':
    unittest.main()