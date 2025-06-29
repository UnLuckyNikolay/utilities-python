import unittest
from .bubble_sort import bubble_sort


class Node():
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"Node({self.val})"
    
    def __eq__(self, node):
        return self.val == node.val

class TestSorting(unittest.TestCase):
    def test__bubble_sort__numbers(self):
        nums = [1, 3, 2, 8, 13, 5, -400]
        nums = bubble_sort(nums)
        self.assertEqual(nums, [-400, 1, 2, 3, 5, 8, 13])

    def test__bubble_sort__nodes(self):
        nodes = [Node(549), Node(69), Node(-1), Node(9001), Node(221)]
        nodes = bubble_sort(nodes, key=lambda node: node.val)
        self.assertEqual(nodes, [Node(-1), Node(69), Node(221), Node(549), Node(9001)])

    
if __name__ == "__main__":
    unittest.main()