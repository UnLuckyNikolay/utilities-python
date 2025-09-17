# pyright: reportOptionalMemberAccess=false
# pyright: reportAttributeAccessIssue=false

from __future__ import annotations

from collections.abc import Callable
from typing import Any


class ValueAlreadyInRedBlackTreeError(Exception):
    """Custom exception raised when value is already present in the red black tree."""
    pass

class RedBlackTree:
    """
    A binary tree data structure with automatic balancing.

    Methods
    -------
    - insert(item : Any)
        Adds the item to the tree.

        Raises `ValueAlreadyInRedBlackTreeError` if the value is already in the tree.

    - get_size() -> int
        Returns the size of the tree.

    - get_height() -> int
        Returns the height of the tree.
    
    - get_min() -> Any
        Returns the item with the smallest value.

    - get_max() -> Any
        Returns the item with the highest value.

    - exists(value) -> bool
        Checks if the item is in the tree and returns a boolean.

    - preorder() -> list
        Returns a list of items using preorder traversal.

    - inorder() -> list
        Returns a list of items using inorder traversal.

    - postorder() -> list
        Returns a list of items using postorder traversal.

    Raises
    ------
    - ValueAlreadyInRedBlackTreeError
        If an item with a value already presented in the tree is being added.
    """

    def __init__(self, key_func : Callable = lambda x: x):
        self._nil = _RBTNode(None)

        self._root = self._nil
        self._key_func = key_func
        self._size = 0

    def __repr__(self) -> str:
        return self._root.repr_tree_recursive("", 0)

    
    def insert(self, item : Any):
        """
        Adds the item to the tree.

        Raises `ValueAlreadyInRedBlackTreeError` if the value is already in the tree.
        """

        new_node = _RBTNode(item)
        new_node.left, new_node.right = self._nil, self._nil
        new_node.red = True
        new_value = self._key_func(item)

        parent = None
        current = self._root
        while current != self._nil:
            parent = current
            current_value = self._key_func(current.item)

            if new_value < current_value:
                current = current.left
            elif new_value > current_value:
                current = current.right
            else:
                raise ValueAlreadyInRedBlackTreeError(
                    f"item with the value {new_value} is already present in the tree."
                )
            
        if parent == None:
            self._root = new_node
        else:
            new_node.parent = parent
            parent_value = self._key_func(parent.item)
            if new_value < parent_value:
                parent.left = new_node
            elif new_value > parent_value:
                parent.right = new_node

        self._size += 1

        self._adjust_tree(new_node)

    def get_size(self) -> int:
        """Returns the size of the tree."""

        return self._size
    
    def get_height(self) -> int:
        """Returns the height of the tree."""

        return self._root.get_height_recursive(self._nil)
    
    def get_min(self) -> Any:
        """Returns the item with the smallest value."""

        return self._root.get_min_recursive(self._nil)
    
    def get_max(self) -> Any:
        """Returns the item with the highest value."""

        return self._root.get_max_recursive(self._nil)
    
    def exists(self, target_value) -> bool:
        """Checks if the item is in the tree and returns a boolean."""

        return self._root.exists_recursive(self._nil, self._key_func, target_value)
    
    def preorder(self) -> list:
        """Returns a list of items using preorder traversal."""

        return self._root.preorder_recursive(self._nil, [])
    
    def inorder(self) -> list:
        """Returns a list of items using inorder traversal."""

        return self._root.inorder_recursive(self._nil, [])
    
    def postorder(self) -> list:
        """Returns a list of items using postorder traversal."""

        return self._root.postorder_recursive(self._nil, [])
    

    def _adjust_tree(self, new_node):
        current = new_node
        while current != self._root and current.parent.red == True:
            parent = current.parent
            grandparent = parent.parent
            uncle = grandparent.left if parent == grandparent.right else grandparent.right
        
            if uncle.red == True:
                uncle.red = False
                parent.red = False
                grandparent.red = True
                current = grandparent
            
            elif parent == grandparent.right:
                if current == parent.left:
                    current = parent
                    self._rotate_right(current)
                    parent = current.parent
                parent.red = False
                grandparent.red = True
                self._rotate_left(grandparent)
                    
            elif parent == grandparent.left:
                if current == parent.right:
                    current = parent
                    self._rotate_left(current)
                    parent = current.parent
                parent.red = False
                grandparent.red = True
                self._rotate_right(grandparent)
                    
        self._root.red = False

    def _rotate_left(self, pivot_parent : _RBTNode):
        if pivot_parent == self._nil or pivot_parent.right == self._nil:
            return # Add error?
        
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot_parent.right != self._nil:
            pivot_parent.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if self._root == pivot_parent:
            self._root = pivot
        elif pivot_parent.parent.left == pivot_parent:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot
        
    def _rotate_right(self, pivot_parent : _RBTNode):
        if pivot_parent == self._nil or pivot_parent.left == self._nil:
            return # Add error?
        
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot_parent.left != self._nil:
            pivot_parent.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if self._root == pivot_parent:
            self._root = pivot
        elif pivot_parent.parent.left == pivot_parent:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot
        

class _RBTNode:
    """Internal class for the red black tree."""

    def __init__(self, item : Any, parent : _RBTNode = None): # pyright: ignore[reportArgumentType]
        self.left :_RBTNode = None
        self.right :_RBTNode = None
        self.parent = parent
        self.red = False
        self.item = item
    
    def repr_tree_recursive(self, repr_str : str, height : int) -> str:
        if self.item != None:
            if self.right.item != None:
                repr_str = self.right.repr_tree_recursive(repr_str, height+1)
            color = "R" if self.red == True else "B"
            repr_str = repr_str + (height * "    " + f"{color}> {self.item}\n")
            if self.left.item != None:
                repr_str = self.left.repr_tree_recursive(repr_str, height+1)

        return repr_str
    
    def get_height_recursive(self, nil_node : _RBTNode) -> int:
        if self == nil_node:
            return 0
        left = 1 if self.left == nil_node else self.left.get_height_recursive(nil_node) + 1
        right = 1 if self.right == nil_node else self.right.get_height_recursive(nil_node) + 1
        return max(left, right)
    
    def get_min_recursive(self, nil_node : _RBTNode) -> Any:
        if self == nil_node:
            return None
        if self.left == nil_node:
            return self.item
        return self.left.get_min_recursive(nil_node)
    
    def get_max_recursive(self, nil_node : _RBTNode) -> Any:
        if self == nil_node:
            return None
        if self.right == nil_node:
            return self.item
        return self.right.get_max_recursive(nil_node)
    
    def exists_recursive(self, nil_node : _RBTNode, key_func : Callable, target_value) -> bool:
        current_value = key_func(self.item)
        if target_value == current_value:
            return True
        elif self.left != nil_node and target_value < current_value:
            return self.left.exists_recursive(nil_node, key_func, target_value)
        elif self.right != nil_node and target_value > current_value:
            return self.right.exists_recursive(nil_node, key_func, target_value)
        return False
    
    def preorder_recursive(self, nil_node : _RBTNode, visited : list) -> list:
        visited.append(self.item)
        if self.left != nil_node:
            visited = self.left.preorder_recursive(nil_node, visited)
        if self.right != nil_node:
            visited = self.right.preorder_recursive(nil_node, visited)
        return visited
    
    def inorder_recursive(self, nil_node : _RBTNode, visited : list) -> list:
        if self.left != nil_node:
            visited = self.left.inorder_recursive(nil_node, visited)
        visited.append(self.item)
        if self.right != nil_node:
            visited = self.right.inorder_recursive(nil_node, visited)
        return visited
    
    def postorder_recursive(self, nil_node : _RBTNode, visited : list) -> list:
        if self.left != nil_node:
            visited = self.left.postorder_recursive(nil_node, visited)
        if self.right != nil_node:
            visited = self.right.postorder_recursive(nil_node, visited)
        visited.append(self.item)
        return visited
    