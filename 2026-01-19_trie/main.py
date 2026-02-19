# Main.py - Your Working File
# Task: Implement Trie (Prefix Tree) Data Structure
# Goal: Master efficient string storage and prefix operations

from typing import List, Optional


# ============================================================
# TRIE NODE CLASS
# ============================================================

class TrieNode:
    """
    Trie node representing a character in the tree.
    
    Attributes:
        children: Dictionary mapping characters to child nodes
        is_end_of_word: Boolean flag marking end of a valid word
    """
    def __init__(self):
        # TODO: Initialize children and end-of-word flag
        pass


# ============================================================
# PROBLEM 1: IMPLEMENT TRIE
# ============================================================

class Trie:
    """
    Trie (Prefix Tree) implementation.
    
    Operations:
    - insert(word): Add word to trie
    - search(word): Return True if exact word exists
    - startsWith(prefix): Return True if any word starts with prefix
    
    Time Complexity: O(m) for all operations, where m = word/prefix length
    Space Complexity: O(ALPHABET_SIZE * N * M) worst case
    
    Example:
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")   # True
    trie.search("app")     # False
    trie.startsWith("app") # True
    """
    
    def __init__(self):
        """Initialize trie with root node"""
        # TODO: Create root node
        pass
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        
        Algorithm:
        1. Start at root
        2. For each character:
           - If child doesn't exist, create new node
           - Move to child node
        3. Mark last node as end of word
        """
        # TODO: Implement insert
        pass
    
    def search(self, word: str) -> bool:
        """
        Search for exact word in trie.
        
        Algorithm:
        1. Traverse trie following word characters
        2. If path doesn't exist, return False
        3. If reach end, check if it's marked as word end
        """
        # TODO: Implement search
        pass
    
    def startsWith(self, prefix: str) -> bool:
        """
        Check if any word starts with given prefix.
        
        Algorithm:
        1. Traverse trie following prefix characters
        2. Return True if complete path exists
        3. Don't need to check is_end_of_word
        """
        # TODO: Implement startsWith
        pass


# ============================================================
# PROBLEM 2: DESIGN ADD AND SEARCH WORDS
# ============================================================

class WordDictionary:
    """
    Data structure supporting add and search with wildcards.
    
    Wildcard '.' matches any single character.
    
    Example:
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.search("bad")  # True
    wd.search(".ad")  # True
    wd.search("b..")  # True
    """
    
    def __init__(self):
        """Initialize with root node"""
        # TODO: Create root
        pass
    
    def addWord(self, word: str) -> None:
        """Add word to dictionary (same as trie insert)"""
        # TODO: Implement addWord
        pass
    
    def search(self, word: str) -> bool:
        """
        Search with wildcard support.
        
        Algorithm (DFS):
        1. If character is '.', try all possible children
        2. If regular character, follow that path only
        3. Use recursion/DFS for wildcard branching
        
        Time: O(M) for defined characters, O(26^M) worst case for all wildcards
        """
        # TODO: Implement wildcard search with DFS
        pass


# ============================================================
# PROBLEM 3: WORD SEARCH II
# ============================================================

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Find all words from dictionary that exist in board.
    
    Can move in 4 directions (up, down, left, right).
    Same cell cannot be used twice in one word.
    
    Example:
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]
    
    Approach: Trie + Board DFS
    1. Build trie from all words
    2. DFS on each board cell
    3. Traverse trie simultaneously with board DFS
    4. When find word, add to result
    
    Time: O(M * N * 4^L) where L = max word length
    Space: O(K) where K = total characters in all words
    """
    # TODO: Implement word search with trie
    pass


# ============================================================
# PROBLEM 4: LONGEST COMMON PREFIX
# ============================================================

def longestCommonPrefix(strs: List[str]) -> str:
    """
    Find longest common prefix among array of strings.
    
    Example:
    Input: ["flower","flow","flight"]
    Output: "fl"
    
    Input: ["dog","racecar","car"]
    Output: ""
    
    Approaches:
    1. Horizontal scanning: Compare prefix with each string
    2. Vertical scanning: Compare character by character
    3. Trie: Insert all, find common path
    4. Divide & conquer: LCP(S1...Sn) = LCP(LCP(S1...Sk), LCP(Sk+1...Sn))
    
    Time: O(S) where S = sum of all characters
    Space: O(1) for scanning, O(S) for trie
    """
    # TODO: Implement (try multiple approaches)
    pass


# ============================================================
# PROBLEM 5: REPLACE WORDS
# ============================================================

def replaceWords(dictionary: List[str], sentence: str) -> str:
    """
    Replace words with their shortest root from dictionary.
    
    Example:
    dictionary = ["cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"
    Output: "the cat was rat by the bat"
    
    Approach: Trie for efficient prefix matching
    1. Build trie from dictionary roots
    2. For each word in sentence:
       - Traverse trie character by character
       - Return shortest root (early termination when found)
       - If no root, return original word
    
    Time: O(D + S) where D = dict chars, S = sentence chars
    Space: O(D) for trie
    """
    # TODO: Implement replace words
    pass


# ============================================================
# PROBLEM 6: PREFIX AND SUFFIX SEARCH
# ============================================================

class WordFilter:
    """
    Find word matching both prefix and suffix.
    
    Example:
    wf = WordFilter(["apple"])
    wf.f("a", "e")  # returns 0
    
    Approach: Combined trie with suffix#prefix
    - For word "apple", store:
      "e#apple", "le#apple", "ple#apple", "pple#apple", "apple#apple"
    - Search for: suffix + "#" + prefix
    - Store indices in trie nodes
    
    Time: O(NK^2) preprocessing, O(K) query where K = word length
    Space: O(NK^2)
    """
    
    def __init__(self, words: List[str]):
        """Build trie with suffix#prefix combinations"""
        # TODO: Implement initialization
        pass
    
    def f(self, prefix: str, suffix: str) -> int:
        """
        Find highest index of word matching prefix and suffix.
        
        Return -1 if no match found.
        """
        # TODO: Implement search
        pass


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_trie(node, prefix="", is_tail=True):
    """Visualize trie structure (for debugging)"""
    print(prefix + ("└── " if is_tail else "├── ") + 
          ("*" if node.is_end_of_word else "○"))
    
    children = list(node.children.items())
    for i, (char, child) in enumerate(children):
        extension = "    " if is_tail else "│   "
        print(prefix + extension + char, end="")
        print_trie(child, prefix + extension, i == len(children) - 1)


if __name__ == "__main__":
    print("=" * 60)
    print("TRIE (PREFIX TREE) - SMOKE TEST")
    print("=" * 60)
    
    # Test 1: Basic Trie Operations
    print("\n" + "-" * 60)
    print("PROBLEM 1: IMPLEMENT TRIE")
    print("-" * 60)
    trie = Trie()
    trie.insert("apple")
    print(f"Search 'apple': {trie.search('apple')}")
    print(f"Expected: True")
    print(f"Search 'app': {trie.search('app')}")
    print(f"Expected: False")
    print(f"StartsWith 'app': {trie.startsWith('app')}")
    print(f"Expected: True")
    
    # Test 2: Wildcard Search
    print("\n" + "-" * 60)
    print("PROBLEM 2: ADD AND SEARCH WORDS")
    print("-" * 60)
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(f"Search 'pad': {wd.search('pad')}")
    print(f"Expected: False")
    print(f"Search 'bad': {wd.search('bad')}")
    print(f"Expected: True")
    print(f"Search '.ad': {wd.search('.ad')}")
    print(f"Expected: True")
    
    # Test 3: Word Search II
    print("\n" + "-" * 60)
    print("PROBLEM 3: WORD SEARCH II")
    print("-" * 60)
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    result = findWords(board, words)
    print(f"Found words: {result}")
    print(f"Expected: ['eat', 'oath'] (in any order)")
    
    # Test 4: Longest Common Prefix
    print("\n" + "-" * 60)
    print("PROBLEM 4: LONGEST COMMON PREFIX")
    print("-" * 60)
    strs = ["flower","flow","flight"]
    result = longestCommonPrefix(strs)
    print(f"LCP: '{result}'")
    print(f"Expected: 'fl'")
    
    # Test 5: Replace Words
    print("\n" + "-" * 60)
    print("PROBLEM 5: REPLACE WORDS")
    print("-" * 60)
    dictionary = ["cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"
    result = replaceWords(dictionary, sentence)
    print(f"Result: {result}")
    print(f"Expected: 'the cat was rat by the bat'")
    
    # Test 6: Prefix and Suffix Search
    print("\n" + "-" * 60)
    print("PROBLEM 6: PREFIX AND SUFFIX SEARCH")
    print("-" * 60)
    wf = WordFilter(["apple"])
    result = wf.f("a", "e")
    print(f"f('a', 'e'): {result}")
    print(f"Expected: 0")
    
    print("\n" + "=" * 60)
    print("Run 'python test_cases.py' for full test suite!")
    print("=" * 60)
