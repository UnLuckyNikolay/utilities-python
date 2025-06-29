import unittest
from .bubble_sort import bubble_sort
from .merge_sort import merge_sort


class Node():
    # Used for testing sorting lists of classes
    def __init__(self, val, val2=None):
        self.val = val # Sorts classes using this arg
        self.val2 = val2 # Checks stability

    def __repr__(self):
        return f"Node({self.val}, {self.val2})"
    
    def __eq__(self, node):
        return (
            self.val == node.val and
            self.val2 == node.val2)

class TestSorting(unittest.TestCase):
    # Lists to use for sorting
    nums = [1, 3, 2, 8, 13, 5, -400]
    nodes = [Node(549), Node(69), Node(-1), Node(9001), Node(221)]
    nodes2 = [Node(549, 1), Node(-1), Node(69), Node(549, 2), Node(9001), Node(221), Node(549, 3)]

    # Sorted lists
    nums_sorted = [-400, 1, 2, 3, 5, 8, 13]
    nodes_sorted = [Node(-1), Node(69), Node(221), Node(549), Node(9001)]
    nodes2_sorted = [Node(-1), Node(69), Node(221), Node(549, 1), Node(549, 2), Node(549, 3), Node(9001)]

    # Reversed sorted lists
    nums_reverse = [13, 8, 5, 3, 2, 1, -400]
    nodes2_reverse = [Node(9001), Node(549, 1), Node(549, 2), Node(549, 3), Node(221), Node(69), Node(-1)]


    def test__sort__zzz__check_lists_at_the_end(self):
        # This test runs last and checks that the lists were properly copied and not modified
        self.assertEqual(self.nums, [1, 3, 2, 8, 13, 5, -400])
        self.assertEqual(self.nodes, [Node(549), Node(69), Node(-1), Node(9001), Node(221)])
        self.assertEqual(self.nodes2, [Node(549, 1), Node(-1), Node(69), Node(549, 2), Node(9001), Node(221), Node(549, 3)])

    # Bubble sort
    def test__sort__bubble__numbers(self):
        nums = self.nums.copy()
        nums = bubble_sort(nums)
        self.assertEqual(nums, self.nums_sorted)

    def test__sort__bubble__nodes(self):
        nodes = self.nodes.copy()
        nodes = bubble_sort(nodes, key=lambda node: node.val)
        self.assertEqual(nodes, self.nodes_sorted)

    def test__sort__bubble__reverse(self):
        nums = self.nums.copy()
        nums = bubble_sort(nums, reverse=True)
        self.assertEqual(nums, self.nums_reverse)

    # Merge sort
    def test__sort__merge__numbers(self):
        nums = self.nums.copy()
        nums = merge_sort(nums)
        self.assertEqual(nums, self.nums_sorted)

    def test__sort__merge__nodes(self):
        nodes = self.nodes.copy()
        nodes = merge_sort(nodes, key=lambda node: node.val)
        self.assertEqual(nodes, self.nodes_sorted)

    def test__sort__merge__numbers_reverse(self):
        nums = self.nums.copy()
        nums = merge_sort(nums, reverse=True)
        self.assertEqual(nums, self.nums_reverse)

    def test__sort__merge__stability(self):
        nodes2 = self.nodes2.copy()
        nodes2 = merge_sort(nodes2, key=lambda node: node.val)
        self.assertEqual(nodes2, self.nodes2_sorted)

    def test__sort__merge__stability_reverse(self):
        nodes2 = self.nodes2.copy()
        nodes2 = merge_sort(nodes2, key=lambda node: node.val, reverse=True)
        self.assertEqual(nodes2, self.nodes2_reverse)

    
if __name__ == "__main__":
    unittest.main()