# Solutions.py - Reference Implementations
# Day 16: Tree DFS & BFS

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM 1: MAXIMUM DEPTH OF BINARY TREE
# ============================================================

def max_depth_recursive(root):
    """
    Find maximum depth of binary tree (DFS recursive).
    
    VISUALIZATION:
    
           3
          / \
         9  20
           /  \
          15   7
    
    EXECUTION TRACE:
    
    max_depth(3):
      ├─ max_depth(9):
      │    ├─ max_depth(None) → 0
      │    ├─ max_depth(None) → 0
      │    └─ return 1 + max(0, 0) = 1
      │
      ├─ max_depth(20):
      │    ├─ max_depth(15):
      │    │    ├─ max_depth(None) → 0
      │    │    ├─ max_depth(None) → 0
      │    │    └─ return 1 + max(0, 0) = 1
      │    │
      │    ├─ max_depth(7):
      │    │    ├─ max_depth(None) → 0
      │    │    ├─ max_depth(None) → 0
      │    │    └─ return 1 + max(0, 0) = 1
      │    │
      │    └─ return 1 + max(1, 1) = 2
      │
      └─ return 1 + max(1, 2) = 3
    
    PATTERN: depth = 1 + max(left_depth, right_depth)
    
    Time: O(n) - visit each node once
    Space: O(h) - recursion stack height
    """
    if not root:
        return 0
    
    left_depth = max_depth_recursive(root.left)
    right_depth = max_depth_recursive(root.right)
    
    return 1 + max(left_depth, right_depth)


def max_depth_bfs(root):
    """
    Find maximum depth of binary tree (BFS iterative).
    
    VISUALIZATION:
    
           3
          / \
         9  20
           /  \
          15   7
    
    EXECUTION TRACE:
    
    Level 0: queue = [3]           depth = 1
    Process: 3 → add 9, 20
    
    Level 1: queue = [9, 20]       depth = 2
    Process: 9 (no children)
    Process: 20 → add 15, 7
    
    Level 2: queue = [15, 7]       depth = 3
    Process: 15, 7 (no children)
    
    Level 3: queue = []            done!
    
    Return: depth = 3
    
    KEY TECHNIQUE: Count levels in BFS
    
    Time: O(n) - visit each node once
    Space: O(w) - queue holds one level at a time
           where w = max width of tree
    """
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0
    
    while queue:
        # Process entire current level
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        depth += 1
    
    return depth


# ============================================================
# PROBLEM 2: MINIMUM DEPTH OF BINARY TREE
# ============================================================

def min_depth_recursive(root):
    """
    Find minimum depth to nearest leaf node (DFS recursive).
    
    VISUALIZATION:
    
           3
          / \
         9  20
           /  \
          15   7
    
    EXECUTION TRACE:
    
    min_depth(3):
      ├─ min_depth(9):           ← LEAF!
      │    ├─ left = None, right = None
      │    └─ return 1
      │
      ├─ min_depth(20):          ← NOT A LEAF
      │    ├─ min_depth(15):      ← LEAF!
      │    │    └─ return 1
      │    │
      │    ├─ min_depth(7):       ← LEAF!
      │    │    └─ return 1
      │    │
      │    └─ return 1 + min(1, 1) = 2
      │
      └─ return 1 + min(1, 2) = 2
    
    TRICKY CASE:
    
           1
          /
         2
    
    min_depth(1):
      ├─ left = min_depth(2) = 1
      ├─ right = min_depth(None) = 0  ← WRONG!
      │  We can't count this path because 1 is NOT a leaf!
      │
      └─ Must ignore the None side and take the other path
         return 1 + left_depth = 2
    
    RULE: If one child is None, take the other child's path.
          Only use min() when both children exist.
    
    Time: O(n)
    Space: O(h)
    """
    if not root:
        return 0
    
    # Base case: leaf node
    if not root.left and not root.right:
        return 1
    
    # If one child is None, must take the other path
    if not root.left:
        return 1 + min_depth_recursive(root.right)
    if not root.right:
        return 1 + min_depth_recursive(root.left)
    
    # Both children exist: take minimum
    left_depth = min_depth_recursive(root.left)
    right_depth = min_depth_recursive(root.right)
    
    return 1 + min(left_depth, right_depth)


def min_depth_bfs(root):
    """
    Find minimum depth to nearest leaf node (BFS iterative).
    
    VISUALIZATION:
    
           3
          / \
         9  20
           /  \
          15   7
    
    EXECUTION TRACE:
    
    Level 1: queue = [3]           depth = 1
    Process: 3 (has children) → add 9, 20
    
    Level 2: queue = [9, 20]       depth = 2
    Process: 9 → NO CHILDREN! → LEAF FOUND! → return 2
    
    BFS finds shortest path automatically!
    No need to traverse entire tree.
    
    WHY BFS IS BETTER FOR MIN DEPTH:
    - DFS must explore all branches to find minimum
    - BFS stops at first leaf (closest to root)
    
    Time: O(n) worst case, but often stops early
    Space: O(w) for queue
    """
    if not root:
        return 0
    
    queue = deque([(root, 1)])  # (node, depth)
    
    while queue:
        node, depth = queue.popleft()
        
        # Check if leaf node
        if not node.left and not node.right:
            return depth  # First leaf we find is minimum!
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return 0


# ============================================================
# PROBLEM 3: PATH SUM
# ============================================================

def has_path_sum(root, target_sum):
    """
    Check if tree has root-to-leaf path with given sum.
    
    VISUALIZATION:
    
           5
          / \
         4   8
        /   / \
       11  13  4
      /  \      \
     7    2      1
    
    Target: 22
    
    EXECUTION TRACE:
    
    has_path_sum(5, 22):           remaining = 22 - 5 = 17
      │
      ├─ has_path_sum(4, 17):      remaining = 17 - 4 = 13
      │    │
      │    └─ has_path_sum(11, 13): remaining = 13 - 11 = 2
      │         │
      │         ├─ has_path_sum(7, 2):  remaining = 2 - 7 = -5
      │         │    └─ LEAF with val 7 ≠ 2 → False
      │         │
      │         └─ has_path_sum(2, 2):  remaining = 2 - 2 = 0
      │              └─ LEAF with val 2 = 2 → True! ✓
      │
      └─ Return True (found valid path: 5→4→11→2)
    
    PATTERN:
    1. Subtract current value from target
    2. If leaf and remaining = 0 → found path!
    3. Otherwise, check left or right subtree
    
    Time: O(n) - may need to check all paths
    Space: O(h) - recursion stack
    """
    if not root:
        return False
    
    # Check if leaf node with target sum
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Subtract current value and check children
    remaining = target_sum - root.val
    
    return (has_path_sum(root.left, remaining) or 
            has_path_sum(root.right, remaining))


# ============================================================
# PROBLEM 4: LEVEL ORDER TRAVERSAL (BFS)
# ============================================================

def level_order(root):
    """
    Return level-order traversal as list of lists.
    
    VISUALIZATION:
    
           3
          / \
         9  20
           /  \
          15   7
    
    EXECUTION TRACE:
    
    Level 0: queue = [3]
             level_size = 1
             current_level = []
             Process: 3 → current_level = [3]
                      Add: 9, 20 to queue
             result = [[3]]
    
    Level 1: queue = [9, 20]
             level_size = 2
             current_level = []
             Process: 9 → current_level = [9]
             Process: 20 → current_level = [9, 20]
                      Add: 15, 7 to queue
             result = [[3], [9, 20]]
    
    Level 2: queue = [15, 7]
             level_size = 2
             current_level = []
             Process: 15 → current_level = [15]
             Process: 7 → current_level = [15, 7]
             result = [[3], [9, 20], [15, 7]]
    
    Level 3: queue = []
             Done!
    
    KEY TECHNIQUE: Track level_size = len(queue) before processing.
                   This tells us how many nodes are at current level.
    
    Time: O(n)
    Space: O(w) for queue
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  # Nodes at current level
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result


# ============================================================
# PROBLEM 5: RIGHT SIDE VIEW
# ============================================================

def right_side_view(root):
    """
    Return values visible from right side of tree.
    
    VISUALIZATION:
    
           1          ← visible: 1
          / \
         2   3        ← visible: 3 (rightmost)
          \   \
           5   4      ← visible: 4 (rightmost)
    
    From right side, you see: [1, 3, 4]
    
    EXECUTION TRACE:
    
    Level 0: queue = [1]
             Process: 1
             Rightmost: 1 ✓
             result = [1]
    
    Level 1: queue = [2, 3]
             Process: 2, 3
             Rightmost: 3 ✓
             result = [1, 3]
    
    Level 2: queue = [5, 4]
             Process: 5, 4
             Rightmost: 4 ✓
             result = [1, 3, 4]
    
    PATTERN: Last node processed at each level = rightmost node
    
    ALTERNATIVE: DFS traversing right side first
    
    def right_side_view_dfs(root):
        result = []
        
        def dfs(node, depth):
            if not node:
                return
            
            # First time we see this depth = rightmost at this level
            if depth == len(result):
                result.append(node.val)
            
            # Traverse right first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return result
    
    Time: O(n)
    Space: O(w) for BFS, O(h) for DFS
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # Last node at this level = rightmost
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result


# ============================================================
# PROBLEM 6: SYMMETRIC TREE
# ============================================================

def is_symmetric(root):
    """
    Check if tree is mirror of itself.
    
    VISUALIZATION:
    
    SYMMETRIC:
           1
          / \
         2   2
        / \ / \
       3  4 4  3
    
    Left subtree (2):     Right subtree (2):
       2                     2
      / \                   / \
     3   4                 4   3
    
    Check: Left of Left = Right of Right? (3 = 3 ✓)
           Right of Left = Left of Right? (4 = 4 ✓)
    
    NOT SYMMETRIC:
           1
          / \
         2   2
          \   \
           3   3
    
    Left subtree (2):     Right subtree (2):
       2                     2
        \                     \
         3                     3
    
    Check: Left of Left = Right of Right? (None ≠ 3 ✗)
    
    EXECUTION TRACE (symmetric case):
    
    is_symmetric(1):
      │
      └─ is_mirror(2, 2):              ← left and right subtrees
           ├─ 2 = 2? Yes ✓
           │
           ├─ is_mirror(3, 3):         ← left.left vs right.right
           │    ├─ 3 = 3? Yes ✓
           │    ├─ is_mirror(None, None) → True
           │    └─ is_mirror(None, None) → True
           │    └─ return True
           │
           └─ is_mirror(4, 4):         ← left.right vs right.left
                ├─ 4 = 4? Yes ✓
                ├─ is_mirror(None, None) → True
                └─ is_mirror(None, None) → True
                └─ return True
           │
           └─ return True (all checks passed)
    
    PATTERN: Compare left and right as mirrors
             - Left's left  ↔  Right's right
             - Left's right ↔  Right's left
    
    Time: O(n) - visit each node once
    Space: O(h) - recursion stack
    """
    def is_mirror(left, right):
        # Both None → symmetric
        if not left and not right:
            return True
        
        # One None, other not → not symmetric
        if not left or not right:
            return False
        
        # Values must match
        if left.val != right.val:
            return False
        
        # Check mirror properties:
        # Left's left = Right's right
        # Left's right = Right's left
        return (is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    if not root:
        return True
    
    return is_mirror(root.left, root.right)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def build_tree_from_list(values):
    """Helper to build tree from level-order list"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root
