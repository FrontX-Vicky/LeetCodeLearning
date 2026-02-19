# Day 19: Trie (Prefix Tree)

**Date**: January 19, 2026  
**Focus**: Trie data structure for efficient string operations  
**Difficulty**: Medium  

---

## 📚 Problems to Solve

### Problem 1: Implement Trie (Prefix Tree)
**LeetCode**: [#208 - Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/)

Implement a trie with `insert`, `search`, and `startsWith` operations.

**Example**:
```python
trie = Trie()
trie.insert("apple")
trie.search("apple")   # returns True
trie.search("app")     # returns False
trie.startsWith("app") # returns True
trie.insert("app")
trie.search("app")     # returns True
```

**Constraints**:
- 1 ≤ word.length, prefix.length ≤ 2000
- word and prefix consist only of lowercase English letters
- At most 3×10⁴ calls will be made to insert, search, and startsWith

**Key Insights**:
- Each node has 26 children (for 'a'-'z')
- Use a boolean flag to mark end of word
- Insert: O(m) where m = word length
- Search: O(m)
- StartsWith: O(m)

---

### Problem 2: Design Add and Search Words Data Structure
**LeetCode**: [#211 - Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/)

Design a data structure that supports adding words and searching with wildcards (`.` matches any letter).

**Example**:
```python
wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
wd.search("pad")  # False
wd.search("bad")  # True
wd.search(".ad")  # True
wd.search("b..")  # True
```

**Constraints**:
- 1 ≤ word.length ≤ 25
- word consists of lowercase English letters
- pattern consists of lowercase letters or '.'
- At most 10⁴ calls to addWord and search

**Key Insights**:
- Trie with DFS for wildcard matching
- When encountering '.', try all 26 possible children
- Backtracking required for wildcard search

---

### Problem 3: Word Search II
**LeetCode**: [#212 - Word Search II](https://leetcode.com/problems/word-search-ii/)

Find all words from a dictionary that exist in a 2D board (DFS in 4 directions).

**Example**:
```python
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
```

**Constraints**:
- m == board.length
- n == board[i].length
- 1 ≤ m, n ≤ 12
- board[i][j] is a lowercase English letter
- 1 ≤ words.length ≤ 3×10⁴
- 1 ≤ words[i].length ≤ 10

**Key Insights**:
- Build trie from all words first
- DFS on board, traverse trie simultaneously
- Prune visited cells and found words
- Much faster than checking each word individually

---

### Problem 4: Longest Common Prefix
**LeetCode**: [#14 - Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

Find the longest common prefix string amongst an array of strings.

**Example**:
```python
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
```

**Constraints**:
- 1 ≤ strs.length ≤ 200
- 0 ≤ strs[i].length ≤ 200
- strs[i] consists of only lowercase English letters

**Key Insights**:
- Horizontal scanning: Compare prefix with each string
- Vertical scanning: Compare character by character across all strings
- Trie approach: Insert all strings, find common path
- Divide and conquer: LCP(S₁...Sₙ) = LCP(LCP(S₁...Sₖ), LCP(Sₖ₊₁...Sₙ))

---

### Problem 5: Replace Words
**LeetCode**: [#648 - Replace Words](https://leetcode.com/problems/replace-words/)

Replace words in a sentence with their shortest root from a dictionary.

**Example**:
```python
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
```

**Constraints**:
- 1 ≤ dictionary.length ≤ 1000
- 1 ≤ dictionary[i].length ≤ 100
- 1 ≤ sentence.length ≤ 10⁶
- All dictionary[i] and words in sentence consist of only lowercase letters

**Key Insights**:
- Build trie from dictionary roots
- For each word in sentence, find shortest matching prefix
- Trie allows early termination when root found

---

### Problem 6: Prefix and Suffix Search
**LeetCode**: [#745 - Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)

Design a data structure to find the word with a given prefix and suffix.

**Example**:
```python
wf = WordFilter(["apple"])
wf.f("a", "e")  # returns 0 (index of "apple")
```

**Constraints**:
- 1 ≤ words.length ≤ 10⁴
- 1 ≤ words[i].length ≤ 7
- 1 ≤ prefix.length, suffix.length ≤ 7
- words[i], prefix and suffix consist of lowercase English letters only
- At most 10⁴ calls will be made to f

**Key Insights**:
- Combine prefix and suffix with special character
- Store modified words like: "e#apple", "le#apple", "ple#apple", etc.
- Search for pattern: suffix + "#" + prefix
- Optimization: Store indices in trie nodes

---

## 🎯 What is a Trie?

A **Trie** (pronounced "try") is a tree-like data structure for efficient string storage and retrieval.

### Structure:
```
Example: Insert "cat", "car", "dog"

        root
       /    \
      c      d
      |      |
      a      o
     / \     |
    t   r    g
    *   *    *
    
* = end of word marker
```

### TrieNode Class:
```python
class TrieNode:
    def __init__(self):
        self.children = {}  # or [None] * 26 for array
        self.is_end_of_word = False
```

### Core Operations:

**1. Insert a word**: O(m) - m = word length
```python
def insert(self, word: str) -> None:
    node = self.root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True
```

**2. Search for exact word**: O(m)
```python
def search(self, word: str) -> bool:
    node = self.root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end_of_word
```

**3. Check if prefix exists**: O(m)
```python
def startsWith(self, prefix: str) -> bool:
    node = self.root
    for char in prefix:
        if char not in node.children:
            return False
        node = node.children[char]
    return True
```

---

## 🔑 Key Concepts

### When to Use a Trie?

✅ **Use Trie when:**
- Prefix-based searches (autocomplete, search suggestions)
- Dictionary/spell checker applications
- IP routing (longest prefix match)
- Word games (Boggle, Scrabble validation)
- String matching with multiple patterns

❌ **Don't use Trie when:**
- Single word lookups (hash map is better)
- No common prefixes between strings
- Memory is extremely limited (tries use more space)
- Need range queries or sorting (use BST instead)

### Trie vs Hash Map

| Feature | Trie | Hash Map |
|---------|------|----------|
| **Exact search** | O(m) | O(m) average |
| **Prefix search** | O(m) | O(n×m) - check all |
| **Space** | O(ALPHABET_SIZE × N × M) | O(N×M) |
| **Ordered traversal** | ✅ Yes | ❌ No |
| **Best for** | Prefix queries | Exact lookups |

### Implementation Choices

**1. Array vs HashMap for children**
```python
# Array: Fixed size (26 for lowercase letters)
children = [None] * 26
index = ord(char) - ord('a')

# HashMap: Dynamic, supports any characters
children = {}
```

**Array**: Faster access O(1), more space  
**HashMap**: Flexible, less space if sparse

**2. Recursive vs Iterative**
```python
# Iterative: More efficient, no stack overflow
def insert_iterative(self, word):
    node = self.root
    for char in word:
        # ...

# Recursive: More elegant for DFS operations
def search_recursive(self, node, word, idx):
    if idx == len(word):
        return node.is_end_of_word
    # ...
```

---

## 💡 Common Patterns

### Pattern 1: Basic Trie Operations
```python
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        # Add word to trie
    
    def search(self, word):
        # Check if exact word exists
    
    def startsWith(self, prefix):
        # Check if any word has this prefix
```

### Pattern 2: Trie with DFS (Wildcard Search)
```python
def search_with_wildcard(self, word):
    def dfs(node, index):
        if index == len(word):
            return node.is_end_of_word
        
        char = word[index]
        if char == '.':
            # Try all possible children
            for child in node.children.values():
                if dfs(child, index + 1):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return dfs(node.children[char], index + 1)
    
    return dfs(self.root, 0)
```

### Pattern 3: Trie + Board DFS (Word Search)
```python
def findWords(self, board, words):
    # Build trie from words
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    # DFS on board with trie traversal
    def dfs(r, c, node, path):
        # Simultaneously traverse board and trie
        char = board[r][c]
        if char not in node.children:
            return
        
        next_node = node.children[char]
        path += char
        
        if next_node.is_end_of_word:
            result.add(path)
        
        # Mark visited and explore neighbors
        board[r][c] = '#'
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            dfs(r+dr, c+dc, next_node, path)
        board[r][c] = char  # Restore
```

### Pattern 4: Finding Shortest Prefix (Replace Words)
```python
def findRoot(self, word):
    node = self.root
    prefix = ""
    
    for char in word:
        if char not in node.children:
            return word  # No root found, return original
        
        prefix += char
        node = node.children[char]
        
        if node.is_end_of_word:
            return prefix  # Found root, return early
    
    return word  # No root found
```

---

## 🎓 Learning Objectives

By the end of Day 19, you should be able to:

1. ✅ Implement a Trie from scratch with insert/search/prefix operations
2. ✅ Use DFS with trie for wildcard pattern matching
3. ✅ Combine trie with board DFS for efficient multi-word search
4. ✅ Optimize string operations using trie (replace words, longest prefix)
5. ✅ Choose between array vs hashmap representation
6. ✅ Understand space-time tradeoffs of tries vs other data structures
7. ✅ Apply tries to real-world problems (autocomplete, spell check)

---

## 📖 Resources

- **Visualizations**:
  - [VisuAlgo - Trie](https://visualgo.net/en/trie)
  - [Trie Animation](https://www.cs.usfca.edu/~galles/visualization/Trie.html)

- **Reading**:
  - [Trie - Wikipedia](https://en.wikipedia.org/wiki/Trie)
  - [Trie Implementation Guide](https://albertauyeung.github.io/2020/06/15/python-trie.html)

- **Practice**:
  - LeetCode Trie Tag: https://leetcode.com/tag/trie/

---

## ✅ Success Criteria

- [ ] Implement TrieNode and Trie classes
- [ ] Solve all 6 problems
- [ ] Understand when to use tries vs hashmaps
- [ ] Master trie + DFS pattern
- [ ] Handle wildcard searches efficiently
- [ ] Optimize memory usage (prune trie when needed)
- [ ] Pass all test cases

---

**Time Estimate**: 3-4 hours  
**Difficulty**: Medium to Hard  
**Key Takeaway**: Tries excel at prefix-based operations that would be inefficient with other data structures.

**Next**: Day 20 - Union Find (Disjoint Set)
