# Day 15: Binary Search Trees (BST)

## Overview
Master Binary Search Tree operations and properties. BST is a powerful data structure that maintains sorted order and enables O(log n) operations for search, insert, and delete (in balanced trees).

## What is a Binary Search Tree?

A **Binary Search Tree** is a binary tree with a special property:
- **Left subtree** contains nodes with values **less than** the parent
- **Right subtree** contains nodes with values **greater than** the parent
- This property holds **recursively** for every node

```
Valid BST:           Invalid BST:
      5                   5
     / \                 / \
    3   7               3   7
   / \   \             / \   \
  2   4   8           2   6   8  ← 6 should be in left subtree!
```

## Why BST is Powerful

1. **Inorder traversal gives sorted order**
   ```
   Tree: 5, 3, 7, 2, 4, 8
   Inorder: [2, 3, 4, 5, 7, 8]  ← Sorted!
   ```

2. **Efficient search** (like binary search in array)
   - Compare with root
   - Go left if smaller, right if larger
   - O(log n) average case, O(n) worst case (skewed tree)

3. **Dynamic structure** (unlike sorted array)
   - Can insert/delete without shifting elements
   - Maintains sorted order automatically

## Problems to Solve

### Problem 1: Search in BST
Given a BST and a target value, return the node with that value, or None if not found.

**Example:**
```
Tree:     4
         / \
        2   7
       / \
      1   3

search(root, 2) → Node(2)
search(root, 5) → None
```

**Approach:**
- Compare target with current node
- If equal → found!
- If target < node.val → search left subtree
- If target > node.val → search right subtree

### Problem 2: Insert into BST
Insert a value into a BST while maintaining BST properties.

**Example:**
```
Tree:     4          Insert 5:      4
         / \                       / \
        2   7                     2   7
       / \          →            / \   \
      1   3                     1   3   5
```

**Approach:**
- Find correct position (like search)
- When you reach None, insert there
- Return the modified tree

### Problem 3: Validate BST
Check if a binary tree is a valid BST.

**Example:**
```
Valid:              Invalid:
      5                   5
     / \                 / \
    3   7               3   7
   / \                 / \
  2   4               2   6  ← 6 > 5, should be in right subtree!
```

**Tricky case:**
```
      10
     /  \
    5   15
       /  \
      6   20   ← Looks valid locally, but 6 < 10!
```

**Approach:**
- Can't just check node.left < node < node.right
- Need to track valid **range** for each node
- Left child must be in range (min, node.val)
- Right child must be in range (node.val, max)

### Problem 4: Find Minimum in BST
Find the node with minimum value in a BST.

**Example:**
```
Tree:     4
         / \
        2   7
       / \
      1   3

Minimum: 1 (leftmost node)
```

**Key Insight:** Minimum is always the **leftmost** node!

### Problem 5: Find Maximum in BST
Find the node with maximum value in a BST.

**Example:**
```
Tree:     4
         / \
        2   7
       / \   \
      1   3   8

Maximum: 8 (rightmost node)
```

**Key Insight:** Maximum is always the **rightmost** node!

### Problem 6: Kth Smallest Element in BST
Find the kth smallest element in a BST (1-indexed).

**Example:**
```
Tree:     5
         / \
        3   7
       / \
      2   4

k=1 → 2 (smallest)
k=2 → 3
k=3 → 4
k=4 → 5
```

**Key Insight:** Inorder traversal gives sorted order!
- Do inorder traversal
- Count as you go
- Return when count reaches k

## Complexity Analysis

| Operation | Average | Worst Case | Space |
|-----------|---------|------------|-------|
| Search | O(log n) | O(n) | O(h) recursive, O(1) iterative |
| Insert | O(log n) | O(n) | O(h) recursive, O(1) iterative |
| Find Min/Max | O(log n) | O(n) | O(1) iterative |
| Validate | O(n) | O(n) | O(h) |
| Kth Smallest | O(n) | O(n) | O(h) |

**Note:** h = height of tree
- Balanced tree: h = log n
- Skewed tree: h = n

## Common Patterns

1. **Recursive BST Template:**
   ```python
   def operation(node, target):
       if not node:
           return base_case
       
       if target < node.val:
           return operation(node.left, target)
       elif target > node.val:
           return operation(node.right, target)
       else:
           return node  # Found!
   ```

2. **Range Validation:**
   ```python
   def is_valid(node, min_val, max_val):
       if not node:
           return True
       
       if not (min_val < node.val < max_val):
           return False
       
       return (is_valid(node.left, min_val, node.val) and
               is_valid(node.right, node.val, max_val))
   ```

3. **Inorder with Counter:**
   ```python
   def kth_smallest(node, k):
       result = []
       
       def inorder(node):
           if not node:
               return
           inorder(node.left)
           result.append(node.val)
           inorder(node.right)
       
       inorder(node)
       return result[k-1]
   ```

## Key Takeaways

1. **BST Property:** Left < Root < Right (recursively)
2. **Inorder = Sorted:** Always remember this!
3. **Search is guided:** Compare and eliminate half the tree
4. **Min/Max is easy:** Leftmost/rightmost node
5. **Validation needs ranges:** Can't just check local relationships
6. **Height matters:** Balanced tree = O(log n), skewed = O(n)

## Real-World Applications

- **Databases:** B-trees (generalized BST) for indexing
- **File systems:** Directory structures
- **Memory management:** Allocation algorithms
- **Symbol tables:** Compiler implementation
- **Auto-complete:** Sorted suggestions
- **Range queries:** Finding elements in a range

## Related LeetCode Problems

- [LeetCode #700: Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)
- [LeetCode #701: Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
- [LeetCode #98: Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [LeetCode #230: Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## Tips

- Draw the tree! Visualizing helps immensely
- Remember: inorder traversal = sorted order
- For validation, think about ranges, not just local comparisons
- BST operations follow a pattern - learn it once, apply everywhere
- Practice both recursive and iterative approaches
