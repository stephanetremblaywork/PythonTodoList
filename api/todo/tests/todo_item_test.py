from unittest import TestCase

from api.todo.todo_item import ToDoItem

class ToDoItemTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self) -> None:
        itemDescription = "DESCRIPTION"
        itemIsDone = True

        todoItem = ToDoItem()
        self.assertEqual(todoItem._description, "")
        self.assertEqual(todoItem._isDone, False)

        todoItem = ToDoItem(isDone=True)
        self.assertEqual(todoItem._description, "")
        self.assertEqual(todoItem._isDone, True)

        todoItem = ToDoItem(description=itemDescription)
        self.assertEqual(todoItem._description, itemDescription)
        self.assertEqual(todoItem._isDone, False)

        todoItem = ToDoItem(isDone=itemIsDone, description=itemDescription)
        self.assertEqual(todoItem._description, itemDescription)
        self.assertEqual(todoItem._isDone, itemIsDone)

        with self.assertRaises(TypeError):
            ToDoItem(isDone="string argument")
        
        with self.assertRaises(TypeError):
            ToDoItem(description=1024)
    
    def test_setIsDone(self) -> None:
        isDone = True
        todoItem = ToDoItem()
        todoItem.setIsDone(isDone)
        self.assertEqual(todoItem._isDone, isDone)

        isDone = False
        todoItem.setIsDone(isDone)
        self.assertEqual(todoItem._isDone, isDone)

        with self.assertRaises(TypeError):
            todoItem.setIsDone("string argument")
    
    def test_setDescription(self) -> None:
        description = "DESCRIPTION"
        todoItem = ToDoItem()
        todoItem.setDescription(description)
        self.assertEqual(todoItem._description, description)

        with self.assertRaises(TypeError):
            self.test_setDescription(1024)
    
    def test_getIsDone(self) -> bool:
        isDone = True
        todoItem = ToDoItem(isDone=isDone)
        self.assertEqual(todoItem.getIsDone(), isDone)

    def test_getDescription(self) -> str:
        description = "DESCRIPTION"
        todoItem = ToDoItem(description=description)
        self.assertEqual(todoItem.getDescription(), description)