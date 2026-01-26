# Day 14: Binary Tree Basics - Tree Traversals

## LeetCode #144, #94, #145: Binary Tree Traversals

### Problem Description
Given the `root` of a binary tree, return the **preorder**, **inorder**, and **postorder** traversal of its nodes' values.

**Binary Tree Node:**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**Example:**
```
Tree:
       1
      / \
     2   3
    / \
   4   5

Preorder:  [1, 2, 4, 5, 3]  (Root → Left → Right)
Inorder:   [4, 2, 5, 1, 3]  (Left → Root → Right)
Postorder: [4, 5, 2, 3, 1]  (Left → Right → Root)
```

**Constraints:**
- The number of nodes in the tree is in the range [0, 100]
- -100 ≤ Node.val ≤ 100

---

## Three Traversal Types

### 1. Preorder Traversal (Root → Left → Right)
**Process root first, then recursively traverse subtrees**

**Recursive Strategy:**
```python
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
```

**Use Cases:**
- Creating a copy of the tree
- Prefix expression evaluation
- Serializing tree structure

**Time:** O(n), **Space:** O(h) where h = height (recursion stack)

---

### 2. Inorder Traversal (Left → Root → Right)
**Process left subtree, then root, then right subtree**

**Recursive Strategy:**
```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

**Use Cases:**
- **Binary Search Tree (BST)**: Inorder gives sorted order!
- Finding kth smallest element in BST
- Validating BST

**Time:** O(n), **Space:** O(h)

---

### 3. Postorder Traversal (Left → Right → Root)
**Process subtrees first, then root**

**Recursive Strategy:**
```python
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

**Use Cases:**
- Deleting tree (delete children before parent)
- Calculating tree height
- Postfix expression evaluation

**Time:** O(n), **Space:** O(h)

---

## Three Implementation Approaches

### Approach 1: Recursive (Most Natural)
**Direct translation of definition**

**Pros:**
- Clean, readable code
- Matches mathematical definition
- Easy to understand and implement

**Cons:**
- Stack overflow risk for very deep trees
- Harder to pause/resume traversal

**Pattern:**
```python
def traverse(root):
    if not root:
        return []
    
    # For preorder:  process root, then left, then right
    # For inorder:   process left, then root, then right
    # For postorder: process left, then right, then root
```

---

### Approach 2: Iterative with Stack
**Simulate recursion using explicit stack**

**Why use stack:**
- Recursion uses implicit call stack
- We can make it explicit with our own stack
- Gives us more control

**Preorder with stack:**
1. Push root
2. Pop node, process it, push right, push left
3. Repeat until stack empty

**Inorder with stack:**
1. Go left as far as possible, pushing nodes
2. Pop and process
3. Go right once
4. Repeat

**Postorder with stack:**
- Trickiest iterative traversal
- Need to track whether we've visited children

---

### Approach 3: Morris Traversal (Advanced - O(1) Space)
**Modify tree temporarily to avoid stack**

**Concept:**
- Use threaded binary tree concept
- Create temporary links to avoid recursion/stack
- Restore tree structure after traversal

**Pros:**
- O(1) extra space (only pointers)
- No recursion, no stack

**Cons:**
- More complex to implement
- Temporarily modifies tree (then restores)
- Not commonly asked in interviews

---

## Key Learnings

### 1. **Traversal Mnemonic**
```
PREorder:  ROOT first, then children
INorder:   LEFT first, root IN middle, right last
POSTorder: Children first, root at the POST (end)
```

### 2. **Visual Example - All Three Traversals**
```
Tree:
       1
      / \
     2   3
    / \
   4   5

Preorder (Root-Left-Right):
  Visit 1 → Visit 2 → Visit 4 → Visit 5 → Visit 3
  Result: [1, 2, 4, 5, 3]

Inorder (Left-Root-Right):
  Visit 4 → Visit 2 → Visit 5 → Visit 1 → Visit 3
  Result: [4, 2, 5, 1, 3]

Postorder (Left-Right-Root):
  Visit 4 → Visit 5 → Visit 2 → Visit 3 → Visit 1
  Result: [4, 5, 2, 3, 1]
```

### 3. **Base Case for All Recursions**
```python
if not root:
    return []  # or return, depending on implementation
```
**Critical:** Check null before accessing `root.val`, `root.left`, `root.right`!

### 4. **Iterative Stack Pattern (Preorder)**
```python
stack = [root]
result = []

while stack:
    node = stack.pop()
    result.append(node.val)
    
    # Push right first (LIFO - will process left first)
    if node.right:
        stack.append(node.right)
    if node.left:
        stack.append(node.left)
```

### 5. **Why Inorder Matters for BST**
```
Binary Search Tree:
       4
      / \
     2   6
    / \ / \
   1  3 5  7

Inorder: [1, 2, 3, 4, 5, 6, 7] ← Sorted!

This property is fundamental to BST operations!
```

---

## Common Mistakes

❌ **Forgetting null check** → NullPointerException
❌ **Wrong order in preorder** → Root must be first
❌ **Stack order confusion** → Right before left (LIFO)
❌ **Not returning result** → Function returns nothing

✅ **Always check `if not root`** before accessing
✅ **Trace small example** → 1-3 nodes
✅ **Trust recursion** → Don't overthink the entire tree

---

## Real-World Applications

1. **File system traversal** - Preorder (directory first, then contents)
2. **Expression trees** - Inorder (infix), Postorder (postfix)
3. **HTML/XML parsing** - Tree structure traversal
4. **Database indexing** - B-trees use inorder
5. **Compiler AST** - Abstract syntax tree traversal

---

## Testing Strategy

**Test Cases:**
- Empty tree (null root)
- Single node
- Only left children (skewed left)
- Only right children (skewed right)
- Complete binary tree
- Various heights (h=1, 2, 3, 4)
- Different values (negative, zero, positive)

**Verify:**
- Correct order for each traversal type
- All nodes visited exactly once
- Correct handling of null nodes

---

## Master Concept: **Tree Recursion**

**Core Principle:**
Trees are naturally recursive structures. Each subtree is itself a tree!

**Recursive Pattern:**
1. **Base case:** `if not root: return`
2. **Process:** Do something with `root.val`
3. **Recurse:** Call on `root.left` and `root.right`
4. **Combine:** Merge results (order depends on traversal type)

**Trust the Recursion:**
- Don't trace entire tree mentally
- Trust that `traverse(root.left)` works correctly
- Focus on: "What do I do at this node?"

---

## Time to Practice! 🚀

Open `main.py` and implement all three traversals (recursive + iterative). Run `python test_cases.py` to verify!
