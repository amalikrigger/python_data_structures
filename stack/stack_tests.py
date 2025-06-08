import unittest
from stack import Stack
from linked_list_stack import LinkedListStack

class TestStackImplementations(unittest.TestCase):

    def setUp(self):
        self.stack_classes = [Stack, LinkedListStack]

    def test_push_and_peek(self):
        for StackClass in self.stack_classes:
            stack = StackClass()
            stack.push(1)
            stack.push(2)
            stack.push(3)
            self.assertEqual(stack.peek(), 3)
            self.assertEqual(stack.size(), 3)

    def test_pop(self):
        for StackClass in self.stack_classes:
            stack = StackClass()
            stack.push(1)
            stack.push(2)
            stack.push(3)
            self.assertEqual(stack.pop(), 3)
            self.assertEqual(stack.pop(), 2)
            self.assertEqual(stack.pop(), 1)
            self.assertTrue(stack.is_empty())

    def test_peek_on_empty_raises(self):
        for StackClass in self.stack_classes:
            stack = StackClass()
            with self.assertRaises(IndexError):
                stack.peek()

    def test_pop_on_empty_raises(self):
        for StackClass in self.stack_classes:
            stack = StackClass()
            with self.assertRaises(IndexError):
                stack.pop()

    def test_is_empty_and_size(self):
        for StackClass in self.stack_classes:
            stack = StackClass()
            self.assertTrue(stack.is_empty())
            self.assertEqual(stack.size(), 0)
            stack.push(42)
            self.assertFalse(stack.is_empty())
            self.assertEqual(stack.size(), 1)

    def test_clear(self):
        for StackClass in self.stack_classes:
            stack = StackClass()
            stack.push(1)
            stack.push(2)
            stack.clear()
            self.assertTrue(stack.is_empty())
            self.assertEqual(stack.size(), 0)

    def test_to_list(self):
        for StackClass in self.stack_classes:
            stack = StackClass()
            for val in [1, 2, 3]:
                stack.push(val)
            self.assertEqual(stack.to_list(), [3, 2, 1])

    def test_bool_and_len(self):
        for StackClass in self.stack_classes:
            stack = StackClass()
            self.assertFalse(stack)
            stack.push(10)
            self.assertTrue(stack)
            self.assertEqual(len(stack), 1)

    def test_mixed_operations(self):
        for StackClass in self.stack_classes:
            stack = StackClass()
            stack.push(1)
            stack.push(2)
            stack.push(3)
            self.assertEqual(stack.pop(), 3)
            stack.push(4)
            self.assertEqual(stack.peek(), 4)
            self.assertEqual(stack.size(), 3)
            self.assertEqual(stack.to_list(), [4, 2, 1])
            stack.clear()
            self.assertTrue(stack.is_empty())

    def test_large_stack(self):
        for StackClass in self.stack_classes:
            stack = StackClass()
            for i in range(1000):
                stack.push(i)
            self.assertEqual(stack.size(), 1000)
            for i in reversed(range(1000)):
                self.assertEqual(stack.pop(), i)
            self.assertTrue(stack.is_empty())

if __name__ == '__main__':
    unittest.main()
