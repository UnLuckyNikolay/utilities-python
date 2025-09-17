import json


class Trie:
    """
    Search tree used to store strings.

    Methods
    -------
    - add(word)
        Adds the word to the trie.

    - exists(word) -> bool
        Checks if the word is in the trie.

    - get_words_with_prefix(prefix) -> list
        Returns a list of words that start with the prefix.

    - find_matches(document, variations) -> set
        Returns a set of matches in the documents.

        If `variations` (dict) are provided, chars stored as keys will be checked as chars stored as values.
    
    - get_longest_common_prefix -> str
        Returns the longest common prefix.

    - get_size -> int
        Returns the amount of words stored in the trie.

    - delete(word)
        Removes the word from the trie.
    """
    
    def __init__(self):
        self._root = {}
        self._end_symbol = '*'
        self._size = 0

    def __repr__(self):
        return json.dumps(self._root, indent=4, sort_keys=True)


    def add(self, word : str):
        """Adds the word to the trie."""

        current_level = self._root

        for char in word:
            if char not in current_level:
                current_level[char] = {}
            current_level = current_level[char]

        current_level[self._end_symbol] = True
        self._size += 1

    def exists(self, word : str) -> bool:
        """Checks if the word is in the trie."""

        current_level = self._root

        for char in word:
            if char not in current_level:
                return False
            current_level = current_level[char]

        return self._end_symbol in current_level
            
    def get_words_with_prefix(self, prefix : str) -> list:
        """Returns a list of words that start with the prefix."""
        
        words = []
        current_level = self._root

        for char in prefix:
            if char in current_level:
                current_level = current_level[char]
            else:
                return words

        return self._search_level(current_level, prefix, words)
    
    def find_matches(self, document : str, variations : dict = None) -> set: # pyright: ignore[reportArgumentType]
        """
        Returns a set of matches in the documents.

        If `variations` (dict) are provided, chars stored as keys will be checked as chars stored as values.
        """

        matches = set()

        for outer_i in range(len(document)):
            current_level = self._root

            for i in range(outer_i, len(document)):
                char = document[i]
                if variations != None and char in variations:
                    char = variations[char]
                if char not in current_level:
                    break
                current_level = current_level[char]
                if self._end_symbol in current_level:
                    matches.add(document[outer_i : i + 1])

        return matches
    
    def get_longest_common_prefix(self) -> str:
        """Returns the longest common prefix."""

        current = self._root
        prefix = ""

        while True:
            children = list(current.keys())
            if self._end_symbol in children or len(children) != 1:
                break
            prefix += children[0]
            current = current[children[0]]

        return prefix
    
    def get_size(self) -> int:
        """Returns the amount of words stored in the trie."""

        return self._size
    
    def delete(self, word : str):
        """Removes the word from the trie."""

        current_level = self._root
        levels = [self._root]

        for char in word:
            if char not in current_level:
                raise ValueError(f"{word} is not present in the trie.")
            current_level = current_level[char]
            levels.append(current_level)

        if self._end_symbol in current_level:
            current_level.pop(self._end_symbol)
            self._size -= 1

            if len(current_level) == 0:
                levels.pop()
                for i in range(1, len(word)+1):
                    current_level = levels.pop()
                    if self._end_symbol not in current_level and len(current_level) == 1:
                        current_level.pop(word[-i])
                    else:
                        current_level.pop(word[-i])
                        return

        else:
            raise ValueError(f"{word} is not present in the trie.")


    def _search_level(self, current_level : dict, current_prefix : str, words : list) -> list:
        """Inner function used in `get_words_with_prefix`"""

        for key in sorted(current_level):
            if key == self._end_symbol:
                words.append(current_prefix)
            else:
                words = self._search_level(current_level[key], current_prefix+key, words)
        return words