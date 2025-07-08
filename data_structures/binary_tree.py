from collections.abc import Callable
from typing import Any


class ValueAlreadyInBinaryTreeError(Exception):
    """Custom exception raised when value is already present in the binary tree."""
    pass

class BinaryTree:
    """
    Methods
    -------
    - insert(object)
        Adds the object to the tree.

        Raises `ValueAlreadyInBinaryTreeError` if the value is already in the tree.

    - delete(object)
        Removes the object from the tree.

    - exists(object) -> bool
        Checks if the object is in the tree and returns a boolean.
    
    - get_min -> Any
        Returns the object with the smallest value.

    - get_max -> Any
        Returns the object with the highest value.

    - get_height -> int
        Returns the height of the tree.

    - preorder -> list
        Returns a list of objects using preorder traversal.

    - inorder -> list
        Returns a list of objects using inorder traversal.

    - postorder -> list
        Returns a list of objects using postorder traversal.

    Raises
    ------
    - ValueAlreadyInBinaryTreeError
        If an object with a value already presented in the tree is being added.
    """

    def __init__(self, key_func : Callable = lambda x: x):
        self._root = _BTNode()
        self._key_func = key_func

    def __repr__(self) -> str:
        return self._root.repr_tree("", 0)


    def insert(self, object : Any):
        """
        Adds the object to the tree.

        Raises `ValueAlreadyInBinaryTreeError` if the value is already in the tree.
        """

        self._root.insert(object, self._key_func)

    def get_min(self) -> Any:
        """Returns the object with the smallest value."""

        return self._root.get_min()
    
    def get_max(self) -> Any:
        """Returns the object with the highest value."""

        return self._root.get_max()
    
    def delete(self, object : Any):
        """Removes the object from the tree."""

        self._root = self._root.delete(object, self._key_func)

    def preorder(self) -> list:
        """Returns a list of objects using preorder traversal."""

        return self._root.preorder([])

    def inorder(self) -> list:
        """Returns a list of objects using inorder traversal."""

        return self._root.inorder([])

    def postorder(self) -> list:
        """Returns a list of objects using postorder traversal."""

        return self._root.postorder([])
    
    def exists(self, object : Any) -> bool:
        """Checks if the object is in the tree and returns a boolean."""

        return self._root.exists(object, self._key_func)
    
    def get_height(self) -> int:
        """Returns the height of the tree."""

        return self._root.get_height()


class _BTNode:
    """Internal class for the binary tree."""

    def __init__(self, object : Any = None):
        self.left = None
        self.right = None
        self.object = object

    def repr_tree(self, repr_str : str, height : int) -> str:
        if self.right != None:
            repr_str = self.right.repr_tree(repr_str, height+1)
        repr_str = repr_str + (height * "    " + f"> {self.object}\n")
        if self.left != None:
            repr_str = self.left.repr_tree(repr_str, height+1)

        return repr_str

    def insert(self, object : Any, key : Callable):
        if self.object == None:
            self.object = object
            return

        if key(object) == key(self.object):
            raise ValueAlreadyInBinaryTreeError(
                f"{object} already present in the binary tree."
            )
        
        if key(object) < key(self.object):
            if self.left == None:
                self.left = _BTNode(object)
            else:
                self.left.insert(object, key)
        
        else:
            if self.right == None:
                self.right = _BTNode(object)
            else:
                self.right.insert(object, key)

    def get_min(self) -> Any:
        if self.left == None:
            return self.object
        return self.left.get_min()

    def get_max(self) -> Any:
        if self.right == None:
            return self.object
        return self.right.get_max()
    
    def delete(self, object, key : Callable):
        if self.object == None:
            return None

        if key(object) < key(self.object):
            self.left = self.left.delete(object, key)
            return self
        if key(object) > key(self.object):
            self.right = self.right.delete(object, key)
            return self

        if self.left == None:
            return self.right
        if self.right == None:
            return self.left

        self.object = self.right.get_min()
        self.right = self.right.delete(self.object, key)
        return self # Check whatever the fuck is happening here after getting some sleep
    
    def preorder(self, visited : list) -> list:
        visited.append(self.object)
        if self.left != None:
            visited = self.left.preorder(visited)
        if self.right != None:
            visited = self.right.preorder(visited)
        return visited
    
    def inorder(self, visited : list) -> list:
        if self.left != None:
            visited = self.left.inorder(visited)
        visited.append(self.object)
        if self.right != None:
            visited = self.right.inorder(visited)
        return visited
    
    def postorder(self, visited : list) -> list:
        if self.left != None:
            visited = self.left.postorder(visited)
        if self.right != None:
            visited = self.right.postorder(visited)
        visited.append(self.object)
        return visited
    
    def exists(self, object, key : Callable) -> bool:
        if key(object) == key(self.object):
            return True
        elif self.left != None and key(object) < key(self.object):
            return self.left.exists(object, key)
        elif self.right != None and key(object) > key(self.object):
            return self.right.exists(object, key)
        return False
    
    def get_height(self) -> int:
        if self.object == None:
            return 0
        left = 1 if self.left == None else self.left.get_height() + 1
        right = 1 if self.right == None else self.right.get_height() + 1
        return max(left, right)