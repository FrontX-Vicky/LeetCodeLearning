# Day 16: Tree DFS & BFS (Depth-First Search & Breadth-First Search)

## Overview
Master tree traversal algorithms: DFS (recursive and iterative) and BFS (level-order). These are fundamental techniques for solving a vast array of tree problems including path finding, level-based operations, and tree analysis.

## What are DFS and BFS?

### **DFS (Depth-First Search)**
Explores as far as possible along each branch before backtracking.

**Three variants:**
- **Preorder**: Root → Left → Right
- **Inorder**: Left → Root → Right  
- **Postorder**: Left → Right → Root

**Characteristics:**
- Uses stack (explicit or recursion stack)
- Memory: O(h) where h = height
- Good for: paths, tree structure analysis

### **BFS (Breadth-First Search)**
Explores all nodes at current level before moving to next level.

**Characteristics:**
- Uses queue (FIFO)
- Memory: O(w) where w = max width
- Good for: shortest paths, level-by-level operations

---

## Visual Comparison

```
Tree:      1
          / \
         2   3
        / \
       4   5

DFS Preorder:  1 → 2 → 4 → 5 → 3  (goes deep first)
DFS Inorder:   4 → 2 → 5 → 1 → 3  (sorted for BST)
DFS Postorder: 4 → 5 → 2 → 3 → 1  (children before parent)

BFS (Level):   1 → 2 → 3 → 4 → 5  (level by level)
```

---

## Problems to Solve

### **Problem 1: Maximum Depth of Binary Tree**
Find the depth (height) of a tree.

**Example:**
```
Tree:      3
          / \
         9  20
           /  \
          15   7

Depth: 3 (levels: 3 → 20 → 15/7)
```

**Approaches:**
1. **DFS Recursive**: depth = 1 + max(left_depth, right_depth)
2. **BFS**: Count levels while traversing

### **Problem 2: Minimum Depth of Binary Tree**
Find the depth to the nearest leaf node.

**Example:**
```
Tree:      3
          / \
         9  20
           /  \
          15   7

Minimum depth: 2 (path: 3 → 9)
```

**Key difference from max depth:** Must reach a **leaf** node (no children).

### **Problem 3: Path Sum**
Check if tree has a root-to-leaf path with given sum.

**Example:**
```
Tree:      5
          / \
         4   8
        /   / \
       11  13  4
      /  \      \
     7    2      1

Target: 22
Path: 5 → 4 → 11 → 2 = 22 ✓
```

**Approach:** DFS, subtract current value, check if leaf reaches 0.

### **Problem 4: Level Order Traversal (BFS)**
Return nodes level by level.

**Example:**
```
Tree:      3
          / \
         9  20
           /  \
          15   7

Result: [[3], [9, 20], [15, 7]]
```

**Approach:** Use queue, process all nodes at current level before moving to next.

### **Problem 5: Right Side View**
Return values of nodes visible from right side.

**Example:**
```
Tree:      1
          / \
         2   3
          \   \
           5   4

Right view: [1, 3, 4]
(The rightmost node at each level)
```

**Approach:** BFS, take last node of each level.

### **Problem 6: Symmetric Tree**
Check if tree is mirror of itself.

**Example:**
```
Valid:         1          Invalid:      1
              / \                      / \
             2   2                    2   2
            / \ / \                    \   \
           3  4 4  3                    3   3
```

**Approach:** Compare left and right subtrees recursively.

---

## DFS vs BFS: When to Use

### **Use DFS when:**
- ✓ Need to explore all paths
- ✓ Tree is very wide (fewer nodes in memory)
- ✓ Looking for specific path
- ✓ Tree structure analysis
- ✓ Recursive solution is natural

### **Use BFS when:**
- ✓ Need shortest path (in terms of levels)
- ✓ Level-by-level processing needed
- ✓ Tree is very deep (BFS won't stack overflow)
- ✓ Finding nodes closest to root
- ✓ Need to process by distance from root

---

## Complexity Analysis

| Operation | DFS (Recursive) | DFS (Iterative) | BFS |
|-----------|-----------------|-----------------|-----|
| Time | O(n) | O(n) | O(n) |
| Space (avg) | O(log n) | O(log n) | O(w)* |
| Space (worst) | O(n) | O(n) | O(n) |

*w = maximum width of tree

**Key differences:**
- **DFS space**: O(height) - tall trees use more
- **BFS space**: O(width) - wide trees use more

**Perfect binary tree:**
- Height: log n
- Width at bottom: n/2
- BFS typically uses more space!

---

## Common Patterns

### **1. DFS Template (Recursive):**
```python
def dfs(node):
    if not node:
        return base_case
    
    # Process current node
    result = process(node)
    
    # Recurse on children
    left = dfs(node.left)
    right = dfs(node.right)
    
    # Combine results
    return combine(result, left, right)
```

### **2. DFS Template (Iterative with Stack):**
```python
def dfs_iterative(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        process(node)
        
        # Push right first (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### **3. BFS Template (Level Order):**
```python
def bfs(root):
    if not root:
        return []
    
    queue = [root]
    result = []
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

### **4. Path Sum Pattern:**
```python
def has_path_sum(node, target):
    if not node:
        return False
    
    # Leaf node check
    if not node.left and not node.right:
        return target == node.val
    
    # Subtract current value and recurse
    remaining = target - node.val
    return (has_path_sum(node.left, remaining) or
            has_path_sum(node.right, remaining))
```

---

## Key Takeaways

1. **DFS = Depth first**, explores branches completely
2. **BFS = Breadth first**, explores level by level
3. **DFS uses stack**, BFS uses queue
4. **Choose based on problem**: shortest path → BFS, path exploration → DFS
5. **Space tradeoff**: DFS O(h), BFS O(w)
6. **All traverse O(n)** nodes eventually
7. **BFS perfect for levels**, DFS perfect for paths

---

## Real-World Applications

### **DFS:**
- File system traversal
- Maze solving
- Dependency resolution
- Game tree exploration (chess, etc.)
- Graph cycle detection

### **BFS:**
- Social network "degrees of separation"
- Web crawlers (by distance from start page)
- GPS navigation (shortest path)
- Network broadcast
- Puzzle solving (Rubik's cube)

---

## Related LeetCode Problems

- [LeetCode #104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [LeetCode #111: Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- [LeetCode #112: Path Sum](https://leetcode.com/problems/path-sum/)
- [LeetCode #102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [LeetCode #199: Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
- [LeetCode #101: Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

---

## Tips

- **DFS is default for most tree problems** - use recursion when possible
- **BFS when you see "level"** in the problem description
- **Queue for BFS**, Stack for iterative DFS
- **Track level information** when needed (BFS)
- **Path problems** often need DFS with backtracking
- **Symmetric problems** compare two subtrees simultaneously
- Draw the execution tree to understand recursion!
