from __future__ import annotations

from collections.abc import Callable
from typing import Any


class ValueAlreadyInBinaryTreeError(Exception):
    """Custom exception raised when value is already present in the binary tree."""
    pass

class BinaryTree:
    """
    A tree data sctructure in which each node has at most 2 children.

    Methods
    -------
    - insert(item)
        Adds the item to the tree.

        Raises `ValueAlreadyInBinaryTreeError` if the value is already in the tree.

    - delete(item)
        Removes the item from the tree.

    - exists(item) -> bool
        Checks if the item is in the tree and returns a boolean.
    
    - get_min -> Any
        Returns the item with the smallest value.

    - get_max -> Any
        Returns the item with the highest value.

    - get_height -> int
        Returns the height of the tree.

    - preorder -> list
        Returns a list of items using preorder traversal.

    - inorder -> list
        Returns a list of items using inorder traversal.

    - postorder -> list
        Returns a list of items using postorder traversal.

    Raises
    ------
    - ValueAlreadyInBinaryTreeError
        If an item with a value already presented in the tree is being added.
    """

    def __init__(self, key_func : Callable = lambda x: x):
        self._root : _BTNode = _BTNode()
        self._key_func = key_func

    def __repr__(self) -> str:
        return self._root.repr_tree("", 0)


    def insert(self, item : Any):
        """
        Adds the item to the tree.

        Raises `ValueAlreadyInBinaryTreeError` if the value is already in the tree.
        """

        self._root.insert(item, self._key_func)

    def get_min(self) -> Any:
        """Returns the item with the smallest value."""

        return self._root.get_min()
    
    def get_max(self) -> Any:
        """Returns the item with the highest value."""

        return self._root.get_max()
    
    def delete(self, item : Any):
        """Removes the item from the tree."""

        self._root = self._root.delete(item, self._key_func) # pyright: ignore[reportAttributeAccessIssue]

    def preorder(self) -> list:
        """Returns a list of items using preorder traversal."""

        return self._root.preorder([])

    def inorder(self) -> list:
        """Returns a list of items using inorder traversal."""

        return self._root.inorder([])

    def postorder(self) -> list:
        """Returns a list of items using postorder traversal."""

        return self._root.postorder([])
    
    def exists(self, item : Any) -> bool:
        """Checks if the item is in the tree and returns a boolean."""

        return self._root.exists(item, self._key_func)
    
    def get_height(self) -> int:
        """Returns the height of the tree."""

        return self._root.get_height()


class _BTNode:
    """Internal class for the binary tree."""

    def __init__(self, item : Any = None):
        self.left : _BTNode | None = None
        self.right : _BTNode | None = None
        self.item = item

    def repr_tree(self, repr_str : str, height : int) -> str:
        if self.right != None:
            repr_str = self.right.repr_tree(repr_str, height+1)
        repr_str = repr_str + (height * "    " + f"> {self.item}\n")
        if self.left != None:
            repr_str = self.left.repr_tree(repr_str, height+1)

        return repr_str

    def insert(self, item : Any, key : Callable):
        if self.item == None:
            self.item = item
            return

        if key(item) == key(self.item):
            raise ValueAlreadyInBinaryTreeError(
                f"{item} already present in the binary tree."
            )
        
        if key(item) < key(self.item):
            if self.left == None:
                self.left = _BTNode(item)
            else:
                self.left.insert(item, key)
        
        else:
            if self.right == None:
                self.right = _BTNode(item)
            else:
                self.right.insert(item, key)

    def get_min(self) -> Any:
        if self.left == None:
            return self.item
        return self.left.get_min()

    def get_max(self) -> Any:
        if self.right == None:
            return self.item
        return self.right.get_max()
    
    def delete(self, item, key : Callable) -> _BTNode | None:
        if self.item == None:
            return None

        if key(item) < key(self.item):
            self.left = self.left.delete(item, key) # pyright: ignore[reportOptionalMemberAccess]
            return self
        if key(item) > key(self.item):
            self.right = self.right.delete(item, key) # pyright: ignore[reportOptionalMemberAccess]
            return self

        if self.left == None:
            return self.right
        if self.right == None:
            return self.left

        self.item = self.right.get_min()
        self.right = self.right.delete(self.item, key)
        return self # Check whatever the fuck is happening here after getting some sleep
    
    def preorder(self, visited : list) -> list:
        visited.append(self.item)
        if self.left != None:
            visited = self.left.preorder(visited)
        if self.right != None:
            visited = self.right.preorder(visited)
        return visited
    
    def inorder(self, visited : list) -> list:
        if self.left != None:
            visited = self.left.inorder(visited)
        visited.append(self.item)
        if self.right != None:
            visited = self.right.inorder(visited)
        return visited
    
    def postorder(self, visited : list) -> list:
        if self.left != None:
            visited = self.left.postorder(visited)
        if self.right != None:
            visited = self.right.postorder(visited)
        visited.append(self.item)
        return visited
    
    def exists(self, item, key : Callable) -> bool:
        if key(item) == key(self.item):
            return True
        elif self.left != None and key(item) < key(self.item):
            return self.left.exists(item, key)
        elif self.right != None and key(item) > key(self.item):
            return self.right.exists(item, key)
        return False
    
    def get_height(self) -> int:
        if self.item == None:
            return 0
        left = 1 if self.left == None else self.left.get_height() + 1
        right = 1 if self.right == None else self.right.get_height() + 1
        return max(left, right)