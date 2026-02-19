# Solutions.py - Reference Implementations with Visualizations
# Trie (Prefix Tree) Problems

from typing import List, Optional


# ============================================================
# TRIE NODE IMPLEMENTATION
# ============================================================

class TrieNode:
    """Basic trie node with children dictionary and end flag"""
    def __init__(self):
        self.children = {}  # Map char -> TrieNode
        self.is_end_of_word = False


# ============================================================
# PROBLEM 1: IMPLEMENT TRIE
# ============================================================

class Trie:
    """
    Standard Trie Implementation
    
    Visualization after inserting "cat", "car", "dog":
    
            root
           /    \
          c      d
          |      |
          a      o
         / \     |
        t   r    g
        *   *    *
    
    * = is_end_of_word = True
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Insert word into trie
        
        Example: insert("cat")
        root -> c -> a -> t (mark as end)
        
        Time: O(m) where m = word length
        Space: O(m) in worst case (no shared prefixes)
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """
        Search for exact word
        
        Example: search("cat")
        - Traverse root -> c -> a -> t
        - Check if t.is_end_of_word == True
        
        Time: O(m)
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        """
        Check if any word starts with prefix
        
        Example: startsWith("ca")
        - Traverse root -> c -> a
        - Return True (path exists)
        - Don't check is_end_of_word!
        
        Time: O(m)
        """
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True


# ============================================================
# PROBLEM 2: ADD AND SEARCH WORDS WITH WILDCARDS
# ============================================================

class WordDictionary:
    """
    Trie with DFS for wildcard search
    
    Wildcard '.' matches any character
    Requires DFS to try all possibilities
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        """Same as trie insert"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """
        DFS search with wildcard support
        
        Example: search(".ad") in trie with "bad", "dad", "mad"
        
        DFS at position 0 ('.'):
          Try all children: b, d, m
          For each, continue DFS at position 1 ('a')
        
        Time: O(M) best case, O(26^M) worst case (all wildcards)
        """
        def dfs(node: TrieNode, index: int) -> bool:
            # Base case: reached end of word
            if index == len(word):
                return node.is_end_of_word
            
            char = word[index]
            
            if char == '.':
                # Wildcard: try all possible children
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                # Regular character: follow specific path
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)
        
        return dfs(self.root, 0)


# ============================================================
# PROBLEM 3: WORD SEARCH II
# ============================================================

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Trie + Board DFS combination
    
    Algorithm:
    1. Build trie from all words
    2. For each cell in board:
       - Start DFS if cell matches trie root child
       - Traverse board and trie simultaneously
       - Mark cells as visited during DFS
       - Add word to result when found
    
    Optimization: Remove word from trie after finding it
    
    Time: O(M*N*4^L) where L = max word length
    Space: O(K) where K = total characters in all words
    """
    
    # Build trie from words
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word  # Store word at end node
    
    rows, cols = len(board), len(board[0])
    result = set()
    
    def dfs(r: int, c: int, node: TrieNode) -> None:
        # Out of bounds or already visited
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            board[r][c] == '#'):
            return
        
        char = board[r][c]
        
        # No matching path in trie
        if char not in node.children:
            return
        
        next_node = node.children[char]
        
        # Found a word!
        if next_node.is_end_of_word:
            result.add(next_node.word)
            # Optimization: prevent duplicate finds
            next_node.is_end_of_word = False
        
        # Mark as visited
        board[r][c] = '#'
        
        # Explore 4 directions
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            dfs(r + dr, c + dc, next_node)
        
        # Restore cell
        board[r][c] = char
    
    # Start DFS from each cell
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    
    return list(result)


# ============================================================
# PROBLEM 4: LONGEST COMMON PREFIX
# ============================================================

def longestCommonPrefix_horizontal(strs: List[str]) -> str:
    """
    Horizontal scanning approach
    
    Algorithm:
    1. Start with first string as prefix
    2. For each subsequent string:
       - Shorten prefix until it matches
    
    Time: O(S) where S = sum of all characters
    Space: O(1)
    """
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        # Shorten prefix until it matches start of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix


def longestCommonPrefix_vertical(strs: List[str]) -> str:
    """
    Vertical scanning approach
    
    Algorithm:
    1. Compare character by character across all strings
    2. Stop when mismatch found
    
    Time: O(S)
    Space: O(1)
    """
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]
        
        # Check if all strings have same char at position i
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    
    return strs[0]


def longestCommonPrefix_trie(strs: List[str]) -> str:
    """
    Trie approach
    
    Algorithm:
    1. Build trie from all strings
    2. Traverse from root while:
       - Only one child exists
       - Not at end of any word
    
    Time: O(S) for building + O(min_len) for traversal
    Space: O(S)
    """
    if not strs:
        return ""
    
    # Build trie
    root = TrieNode()
    for word in strs:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    # Find common prefix
    prefix = ""
    node = root
    
    while len(node.children) == 1 and not node.is_end_of_word:
        char = list(node.children.keys())[0]
        prefix += char
        node = node.children[char]
    
    return prefix


# ============================================================
# PROBLEM 5: REPLACE WORDS
# ============================================================

def replaceWords(dictionary: List[str], sentence: str) -> str:
    """
    Use trie for efficient prefix matching
    
    Algorithm:
    1. Build trie from dictionary roots
    2. For each word in sentence:
       - Traverse trie to find shortest root
       - Use root if found, else original word
    
    Time: O(D + S) where D = dict chars, S = sentence chars
    Space: O(D) for trie
    """
    
    # Build trie from dictionary
    root = TrieNode()
    for word in dictionary:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def findRoot(word: str) -> str:
        """Find shortest root for word"""
        node = root
        prefix = ""
        
        for char in word:
            if char not in node.children:
                return word  # No root found
            
            prefix += char
            node = node.children[char]
            
            if node.is_end_of_word:
                return prefix  # Found root, return early!
        
        return word  # No root found
    
    # Replace each word
    words = sentence.split()
    return " ".join(findRoot(word) for word in words)


# ============================================================
# PROBLEM 6: PREFIX AND SUFFIX SEARCH
# ============================================================

class WordFilter:
    """
    Combined prefix-suffix trie
    
    Key Idea: Store word as "suffix#prefix"
    For "apple":
      "e#apple"
      "le#apple"
      "ple#apple"
      "pple#apple"
      "apple#apple"
      "#apple" (empty suffix)
    
    Search for: suffix + "#" + prefix
    """
    
    def __init__(self, words: List[str]):
        self.trie = {}
        
        # Process each word with its index
        for index, word in enumerate(words):
            # Generate all suffix#prefix combinations
            for i in range(len(word) + 1):
                suffix = word[i:]  # Empty to full word
                key = suffix + "#" + word
                
                # Insert into trie
                node = self.trie
                for char in key:
                    if char not in node:
                        node[char] = {}
                    node = node[char]
                    # Store index at every node (higher index = later in list)
                    node['#index'] = index
    
    def f(self, prefix: str, suffix: str) -> int:
        """
        Find highest weight (index) of word with prefix and suffix
        
        Time: O(P + S) where P = prefix length, S = suffix length
        """
        search_key = suffix + "#" + prefix
        node = self.trie
        
        for char in search_key:
            if char not in node:
                return -1
            node = node[char]
        
        return node.get('#index', -1)


# ============================================================
# VISUALIZATION HELPERS
# ============================================================

def visualize_trie_insert():
    """
    Demonstrate trie insertion
    
    Insert: "cat", "car", "dog"
    
    Step 1: Insert "cat"
        root
         |
         c
         |
         a
         |
         t*
    
    Step 2: Insert "car" (shares "ca" prefix)
        root
         |
         c
         |
         a
        / \
       t*  r*
    
    Step 3: Insert "dog" (new branch)
        root
       /    \
      c      d
      |      |
      a      o
     / \     |
    t*  r*   g*
    """
    print("Trie Insertion Visualization")
    print("* = end of word marker")


def visualize_wildcard_search():
    """
    Demonstrate wildcard DFS search
    
    Trie: "bad", "dad", "mad"
        root
       / | \
      b  d  m
      |  |  |
      a  a  a
      |  |  |
      d* d* d*
    
    Search ".ad":
    - At position 0, char='.'
    - Try all 3 branches: b, d, m
    - For each, continue with 'a' at position 1
    - All succeed → return True
    """
    print("Wildcard Search DFS")
    print("'.' requires trying all possible branches")


if __name__ == "__main__":
    print("Trie - Reference Solutions")
    print("=" * 60)
    
    # Test basic trie
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    print(f"Search 'apple': {trie.search('apple')}")  # True
    print(f"Search 'app': {trie.search('app')}")      # True
    print(f"StartsWith 'app': {trie.startsWith('app')}")  # True
    print(f"Search 'appl': {trie.search('appl')}")    # False
    
    print()
    visualize_trie_insert()
    print()
    visualize_wildcard_search()
