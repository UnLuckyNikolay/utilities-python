import unittest
from data_structures.stack import Stack, StackIsEmptyError, StackIsFullError
from data_structures.queue import Queue, QueueIsEmptyError, QueueIsFullError
from data_structures.linked_list import LinkedList, LListIsEmptyError, LListIsFullError
from data_structures.llqueue import LLQueue, LLQueueIsEmptyError, LLQueueIsFullError
from data_structures.binary_tree import BinaryTree, ValueAlreadyInBinaryTreeError


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
        self.assertEqual(repr(stack), "Stack[Node(3), Node(2), Node(1)]")

    def test__data_structures__stack__pop(self):
        stack = Stack()
        stack.push(Node(1))
        stack.push(Node(2))
        stack.push(Node(3))
        item = stack.pop()
        self.assertEqual(item, Node(3))
        self.assertEqual(repr(stack), "Stack[Node(2), Node(1)]")

    def test__data_structures__stack__peek(self):
        stack = Stack()
        stack.push(Node(1))
        stack.push(Node(2))
        stack.push(Node(3))
        item = stack.peek()
        self.assertEqual(item, Node(3))
        self.assertEqual(repr(stack), "Stack[Node(3), Node(2), Node(1)]")

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
        
    # Queue
    def test__data_structures__queue__push(self):
        queue = Queue()
        queue.push(Node(1))
        queue.push(Node(2))
        queue.push(Node(3))
        self.assertEqual(repr(queue), "Queue[Node(1), Node(2), Node(3)]")

    def test__data_structures__queue__pop(self):
        queue = Queue()
        queue.push(Node(1))
        queue.push(Node(2))
        queue.push(Node(3))
        item = queue.pop()
        self.assertEqual(item, Node(1))
        self.assertEqual(repr(queue), "Queue[Node(2), Node(3)]")

    def test__data_structures__queue__peek(self):
        queue = Queue()
        queue.push(Node(1))
        queue.push(Node(2))
        queue.push(Node(3))
        item = queue.peek()
        self.assertEqual(item, Node(1))
        self.assertEqual(repr(queue), "Queue[Node(1), Node(2), Node(3)]")

    def test__data_structures__queue__push_on_full__exception(self):
        queue = Queue(max_size=1)
        queue.push(Node(1))
        with self.assertRaises(QueueIsFullError):
            queue.push(Node(2))

    def test__data_structures__queue__pop_on_empty__exception(self):
        queue = Queue(raise_errors_on_empty_op=True)
        with self.assertRaises(QueueIsEmptyError):
            queue.pop()

    def test__data_structures__queue__peek_on_empty__exception(self):
        queue = Queue(raise_errors_on_empty_op=True)
        with self.assertRaises(QueueIsEmptyError):
            queue.peek()

    def test__data_structures__queue__pop_on_empty(self):
        queue = Queue()
        item = queue.pop()
        self.assertEqual(item, None)

    def test__data_structures__queue__peek_on_empty(self):
        queue = Queue()
        item = queue.peek()
        self.assertEqual(item, None)

    def test__data_structures__queue__is_empty(self):
        queue = Queue()
        check = queue.is_empty()
        self.assertEqual(check, True)
        queue.push(Node(1))
        check = queue.is_empty()
        self.assertEqual(check, False)

    def test__data_structures__queue__is_full(self):
        queue = Queue(max_size=1)
        check = queue.is_full()
        self.assertEqual(check, False)
        queue.push(Node(1))
        check = queue.is_full()
        self.assertEqual(check, True)
        
    # Linked List
    def test__data_structures__llist__push_to_tail(self):
        llist = LinkedList()
        llist.add_to_tail(1)
        llist.add_to_tail("two")
        llist.add_to_tail(3)
        self.assertEqual(repr(llist), "[1 -> two -> 3]")

    def test__data_structures__llist__push_to_head(self):
        llist = LinkedList()
        llist.add_to_head(3)
        llist.add_to_head("two")
        llist.add_to_head(1)
        self.assertEqual(repr(llist), "[1 -> two -> 3]")

    def test__data_structures__llist__pop(self):
        llist = LinkedList()
        llist.add_to_head(3)
        llist.add_to_head("two")
        llist.add_to_head(1)
        item = llist.pop_from_head()
        self.assertEqual(item, 1)
        self.assertEqual(repr(llist), "[two -> 3]")

    def test__data_structures__llist__peek(self):
        llist = LinkedList()
        llist.add_to_head(3)
        llist.add_to_head("two")
        llist.add_to_head(1)
        item = llist.peek_from_head()
        self.assertEqual(item, 1)
        self.assertEqual(repr(llist), "[1 -> two -> 3]")

    def test__data_structures__llist__add_to_full__exception(self):
        llist = LinkedList(max_size=1)
        llist.add_to_head(1)
        with self.assertRaises(LListIsFullError):
            llist.add_to_head(2)
        with self.assertRaises(LListIsFullError):
            llist.add_to_tail(3)

    def test__data_structures__llist__pop_on_empty__exception(self):
        llist = LinkedList(raise_errors_on_empty_op=True)
        with self.assertRaises(LListIsEmptyError):
            llist.pop_from_head()

    def test__data_structures__llist__peek_on_empty__exception(self):
        llist = LinkedList(raise_errors_on_empty_op=True)
        with self.assertRaises(LListIsEmptyError):
            llist.peek_from_head()

    def test__data_structures__llist__pop_on_empty(self):
        llist = LinkedList()
        item = llist.pop_from_head()
        self.assertEqual(item, None)

    def test__data_structures__llist__peek_on_empty(self):
        llist = LinkedList()
        item = llist.peek_from_head()
        self.assertEqual(item, None)

    def test__data_structures__llist__is_empty(self):
        llist = LinkedList()
        check = llist.is_empty()
        self.assertEqual(check, True)
        llist.add_to_head(1)
        check = llist.is_empty()
        self.assertEqual(check, False)

    def test__data_structures__llist__is_full(self):
        llist = LinkedList(max_size=1)
        check = llist.is_full()
        self.assertEqual(check, False)
        llist.add_to_head(1)
        check = llist.is_full()
        self.assertEqual(check, True)

    # LLQueue
    def test__data_structures__llqueue__push(self):
        llist = LLQueue()
        llist.push(1)
        llist.push("two")
        llist.push(3)
        self.assertEqual(repr(llist), "LLQueue[1 <- two <- 3]")

    def test__data_structures__llqueue__pop(self):
        llist = LLQueue()
        llist.push(1)
        llist.push("two")
        llist.push(3)
        item = llist.pop()
        self.assertEqual(item, 1)
        self.assertEqual(repr(llist), "LLQueue[two <- 3]")

    def test__data_structures__llqueue__peek(self):
        llist = LLQueue()
        llist.push(1)
        llist.push("two")
        llist.push(3)
        item = llist.peek()
        self.assertEqual(item, 1)
        self.assertEqual(repr(llist), "LLQueue[1 <- two <- 3]")

    def test__data_structures__llqueue__add_to_full__exception(self):
        llist = LLQueue(max_size=1)
        llist.push(1)
        with self.assertRaises(LLQueueIsFullError):
            llist.push(2)
        with self.assertRaises(LLQueueIsFullError):
            llist.push(3)

    def test__data_structures__llqueue__pop_on_empty__exception(self):
        llist = LLQueue(raise_errors_on_empty_op=True)
        with self.assertRaises(LLQueueIsEmptyError):
            llist.pop()

    def test__data_structures__llqueue__peek_on_empty__exception(self):
        llist = LLQueue(raise_errors_on_empty_op=True)
        with self.assertRaises(LLQueueIsEmptyError):
            llist.peek()

    def test__data_structures__llqueue__pop_on_empty(self):
        llist = LLQueue()
        item = llist.pop()
        self.assertEqual(item, None)

    def test__data_structures__llqueue__peek_on_empty(self):
        llist = LLQueue()
        item = llist.peek()
        self.assertEqual(item, None)

    def test__data_structures__llqueue__is_empty(self):
        llist = LLQueue()
        check = llist.is_empty()
        self.assertEqual(check, True)
        llist.push(1)
        check = llist.is_empty()
        self.assertEqual(check, False)

    def test__data_structures__llqueue__is_full(self):
        llist = LLQueue(max_size=1)
        check = llist.is_full()
        self.assertEqual(check, False)
        llist.push(1)
        check = llist.is_full()
        self.assertEqual(check, True)

    # Binary Tree
    def test__data_structures__binary_tree__inorder(self):
        bt = BinaryTree()
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bt.insert(i)
        self.assertEqual(bt.inorder(), [1, 2, 3, 4, 5, 6, 7])

    def test__data_structures__binary_tree__preorder(self):
        bt = BinaryTree()
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bt.insert(i)
        self.assertEqual(bt.preorder(), [4, 2, 1, 3, 6, 5, 7])

    def test__data_structures__binary_tree__postorder(self):
        bt = BinaryTree()
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bt.insert(i)
        self.assertEqual(bt.postorder(), [1, 3, 2, 5, 7, 6, 4])

    def test__data_structures__binary_tree__exists(self):
        bt = BinaryTree()
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bt.insert(i)
        self.assertEqual(bt.exists(3), True)
        self.assertEqual(bt.exists(12), False)

    def test__data_structures__binary_tree__get_height(self):
        bt = BinaryTree()
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bt.insert(i)
        self.assertEqual(bt.get_height(), 3)

    def test__data_structures__binary_tree__get_min(self):
        bt = BinaryTree()
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bt.insert(i)
        self.assertEqual(bt.get_min(), 1)

    def test__data_structures__binary_tree__get_max(self):
        bt = BinaryTree()
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bt.insert(i)
        self.assertEqual(bt.get_max(), 7)

    def test__data_structures__binary_tree__delete(self):
        bt = BinaryTree()
        for i in [4, 2, 1, 3, 6, 5, 7]:
            bt.insert(i)
        bt.delete(5)
        self.assertEqual(bt.inorder(), [1, 2, 3, 4, 6, 7])

        #self.assertEqual(rbt.inorder(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        #self.assertEqual(rbt.preorder(), [4, 2, 1, 3, 6, 5, 8, 7, 9, 10])
        #self.assertEqual(rbt.postorder(), [1, 3, 2, 5, 7, 10, 9, 8, 6, 4])
        #nums = [10, 6, 3, 4, 8, 7, 9, 1, 5, 2]