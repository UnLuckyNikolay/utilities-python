import unittest
from data_structures.stack import Stack, StackIsEmptyError, StackIsFullError


class Node:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"Node({self.val})"

    def __eq__(self, node):
        return self.val == node.val

class TestDataStructures(unittest.TestCase):
    # Stack
    def test__data_structures__stack__push(self):
        stack = Stack()
        stack.push(Node(1))
        stack.push(Node(2))
        stack.push(Node(3))
        self.assertEqual(repr(stack), "Stack[Node(1), Node(2), Node(3)]")

    def test__data_structures__stack__pop(self):
        stack = Stack()
        stack.push(Node(1))
        item = stack.pop()
        self.assertEqual(item, Node(1))
        self.assertEqual(repr(stack), "Stack[]")

    def test__data_structures__stack__peek(self):
        stack = Stack()
        stack.push(Node(1))
        item = stack.peek()
        self.assertEqual(item, Node(1))
        self.assertEqual(repr(stack), "Stack[Node(1)]")

    def test__data_structures__stack__push_on_full__exception(self):
        stack = Stack(max_size=1)
        stack.push(Node(1))
        with self.assertRaises(StackIsFullError):
            stack.push(Node(2))

    def test__data_structures__stack__pop_on_empty__exception(self):
        stack = Stack(raise_errors_on_empty_op=True)
        with self.assertRaises(StackIsEmptyError):
            stack.pop()

    def test__data_structures__stack__peek_on_empty__exception(self):
        stack = Stack(raise_errors_on_empty_op=True)
        with self.assertRaises(StackIsEmptyError):
            stack.peek()

    def test__data_structures__stack__pop_on_empty(self):
        stack = Stack()
        item = stack.pop()
        self.assertEqual(item, None)

    def test__data_structures__stack__peek_on_empty(self):
        stack = Stack()
        item = stack.peek()
        self.assertEqual(item, None)

    def test__data_structures__stack__is_empty(self):
        stack = Stack()
        check = stack.is_empty()
        self.assertEqual(check, True)
        stack.push(Node(1))
        check = stack.is_empty()
        self.assertEqual(check, False)

    def test__data_structures__stack__is_full(self):
        stack = Stack(max_size=1)
        check = stack.is_full()
        self.assertEqual(check, False)
        stack.push(Node(1))
        check = stack.is_full()
        self.assertEqual(check, True)