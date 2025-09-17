# Utilities for Python

A library of various functions and data structures created to be used as a pip package. Includes a number of unit tests and documentation.

## Contents

* `shuffle.py`

    function `shuffle(iterable) -> list`

	Shuffles a copy of the iterable in place and returns it as a list.  
	Uses [Fisher–Yates shuffle](https://en.wikipedia.org/wiki/Fisher–Yates_shuffle) to achieve time complexity of O(n).

* `sorting/`
	* `bubble_sort.py`

		function `bubble_sort(iterable, key=lambda x: x, reverse=False) -> list`

		Sorts a copy of the iterable in place and returns as a list.

	* `insertion_sort.py`

		function `insertion_sort(iterable, key=lambda x: x, reverse=False) -> list`

		Sorts a copy of the iterable in place and returns it as a list.

	* `merge_sort.py`

		function `merge_sort(iterable, key=lambda x: x, reverse=False) -> list`

		Sorts the iterable by splitting into smaller and smaller iterables before merging back. Then returns it as a list.

	* `quick_sort.py`

		function `quick_sort(iterable, key=lambda x: x, reverse=False, shuffling=True) -> list`

		Sorts a shuffled (can be turned off) copy of the iterable in place and returns it as a list.

	* `selection_sort.py`

		function `selection_sort(iterable, key=lambda x: x, reverse=False) -> list`

		Sorts a copy of the iterable in place and returns it as a list.

* `data_structures/`
	* `stack.py`

		`Stack(max_size=None, raise_errors_on_empty_op=False)`

		Abstract data structure. Last in, first out.  
    	Complexity of all methods - O(1).
		
		Implemented methods:

		* `.push(item)`
		* `.pop() -> Any | None`
		* `.peek() -> Any | None`
		* `.size() -> int`
		* `.is_empty() -> bool`
		* `.is_full() -> bool`

	* `queue.py`

		`Queue(max_size=None, raise_errors_on_empty_op=False)`
	
    	Abstract data structure. First in, first out.
    	Complexity of `pop` - O(n), the rest - O(1).
		
		Implemented methods:

		* `.push(item)`
		* `.pop() -> Any | None`
		* `.peek() -> Any | None`
		* `.size() -> int`
		* `.is_empty() -> bool`
		* `.is_full() -> bool`

	* `linked_list.py`

		`LinkedList(max_size=None, raise_errors_on_empty_op=False)`
	
    	Collection of nodes with references to the next one.
		
		Implemented methods:

		* `.add_to_tail(item)`
		* `.add_to_head(item)`
		* `.pop_from_head() -> Any | None`
		* `.peek_from_head() -> Any | None`
		* `.size() -> int`
		* `.is_empty() -> bool`
		* `.is_full() -> bool`

	* `llqueue.py`

		`LLQueue(max_size=None, raise_errors_on_empty_op=False)`

    	Abstract data structure. First in, first out. Linked List used to store items.  
    	Complexity of all methods - O(1).
		
		Implemented methods:

		* `.push(item)`
		* `.pop() -> Any | None`
		* `.peek() -> Any | None`
		* `.size() -> int`
		* `.is_empty() -> bool`
		* `.is_full() -> bool`

	* `hashmap.py`

		`HashMap(default_size=8, maximum_size=None)`
	
    	Stores objects as pairs of keys (Hashable) and values (Any).
		
		Implemented methods:

		* `.insert(key, value)`
		* `.get(key) -> Any`
		* `.pop(key) -> Any`
		* `.get_size() -> int`

	* `binary_tree.py`

		`BinaryTree(key_func=lambda x: x)`

		A tree data structure in which each node has at most 2 children.

		Implemented methods:

		* `.insert(item)`
		* `.delete(item)`
		* `.exists(item) -> bool`
		* `.get_min() -> Any`
		* `.get_max() -> Any`
		* `.get_height() -> int`
		* `.preorder() -> list`
		* `.inorder() -> list`
		* `.postorder() -> list`

	* `red_black_tree.py`

		`RedBlackTree(key_func=lambda x: x)`

		A binary tree data structure with automatic balancing.

		Implemented methods:

		* `.insert(item)`
		* `.exists(value) -> bool`
		* `.get_min() -> Any`
		* `.get_max() -> Any`
		* `.get_height() -> int`
		* `.get_size() -> int`
		* `.preorder() -> list`
		* `.inorder() -> list`
		* `.postorder() -> list`

	* `trie.py`

		`Trie()`

		A search tree used to store strings.

		Implemented methods:

		* `.add(word)`
		* `.exists(word) -> bool`
		* `.get_words_with_prefix(prefix) -> list`
		* `.find_matches(document, variations) -> list`
		* `.get_longest_common_prefix() -> str`
		* `.get_size() -> int`
		* `.delete(word)`

## Installation

1. Install [Python](https://www.python.org/downloads) 3.10 or higher.

2. Install using pip:

	```bash
	pip install git+https://github.com/UnLuckyNikolay/utilities-python.git
	```

3. Import the needed functions and structures:

	```python
	from utilities_python.*path* import *name*
	```

## Updating

Run the upgrade command:

```bash
pip install git+https://github.com/UnLuckyNikolay/utilities-python.git --upgrade
```

## Usage examples

* Sorting:

	Code

	```python
	from utilities_python.sorting.quick_sort import quick_sort

	def main():
		numArray = [42, 8, 16, 23, 4, 15]
		numArray = quick_sort(numArray)
		print(numArray)

	if __name__ == "__main__":
		main()
	```

	Result

	```
	[4, 8, 15, 16, 23, 42]
	```

* Queue:

	Code

	```python
	from utilities_python.data_structures.llqueue import LLQueue

	def main():
		queue = LLQueue()
		queue.push("Wake up")
		queue.push("Brush your teeth")
		queue.push("Hack the Pentagon")
		print(queue)

	if __name__ == "__main__":
		main()
	```

	Result

	```
	LLQueue[Wake up <- Brush your teeth <- Hack the Pentagon]
	```

## Unittests

Run from inside the package folder:

```bash
./test.sh
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.