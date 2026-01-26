# Solutions.py - Reference Implementations
# Binary Search Tree Operations

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM 1: SEARCH IN BST
# ============================================================

def search_bst_recursive(root, val):
    """
    Search for a value in BST (recursive).
    
    Visual trace for searching 2 in:
           4
          / \
         2   7
        / \
       1   3
    
    Call stack:
    1. search(4, 2): 2 < 4, go left
       └─> search(2, 2): 2 == 2, found! Return Node(2)
    
    Result: Node(2)
    
    Time: O(log n) average, O(n) worst (skewed tree)
    Space: O(h) for recursion stack
    """
    # Base case: not found
    if not root:
        return None
    
    # Found!
    if val == root.val:
        return root
    
    # Search left if val < root.val
    if val < root.val:
        return search_bst_recursive(root.left, val)
    
    # Search right if val > root.val
    return search_bst_recursive(root.right, val)


def search_bst_iterative(root, val):
    """
    Search for a value in BST (iterative).
    
    Visual trace for searching 3 in:
           4
          / \
         2   7
        / \
       1   3
    
    Iteration:
    1. current = 4, val=3, 3 < 4 → go left
    2. current = 2, val=3, 3 > 2 → go right
    3. current = 3, val=3, 3 == 3 → found!
    
    Result: Node(3)
    
    Time: O(log n) average, O(n) worst
    Space: O(1) - no recursion!
    """
    current = root
    
    while current:
        if val == current.val:
            return current
        elif val < current.val:
            current = current.left
        else:
            current = current.right
    
    return None


# ============================================================
# PROBLEM 2: INSERT INTO BST
# ============================================================

def insert_bst_recursive(root, val):
    """
    Insert a value into BST (recursive).
    
    Visual trace for inserting 5 into:
           4
          / \
         2   7
        / \
       1   3
    
    Call stack:
    1. insert(4, 5): 5 > 4, insert in right subtree
       └─> insert(7, 5): 5 < 7, insert in left subtree
           └─> insert(None, 5): Create new node → Node(5)
    
    Result:
           4
          / \
         2   7
        / \  /
       1  3 5
    
    Time: O(log n) average, O(n) worst
    Space: O(h) for recursion
    """
    # Base case: found the position, insert here
    if not root:
        return TreeNode(val)
    
    # Recursively insert in left or right subtree
    if val < root.val:
        root.left = insert_bst_recursive(root.left, val)
    else:
        root.right = insert_bst_recursive(root.right, val)
    
    return root


def insert_bst_iterative(root, val):
    """
    Insert a value into BST (iterative).
    
    Visual trace for inserting 6 into:
           4
          / \
         2   7
    
    Iteration:
    1. current = 4, val=6, 6 > 4 → go right, parent = 4
    2. current = 7, val=6, 6 < 7 → go left, parent = 7
    3. current = None → insert Node(6) as left child of parent(7)
    
    Result:
           4
          / \
         2   7
            /
           6
    
    Time: O(log n) average, O(n) worst
    Space: O(1) - constant space!
    """
    # Edge case: empty tree
    if not root:
        return TreeNode(val)
    
    current = root
    
    while True:
        if val < current.val:
            if not current.left:
                current.left = TreeNode(val)
                break
            current = current.left
        else:
            if not current.right:
                current.right = TreeNode(val)
                break
            current = current.right
    
    return root


# ============================================================
# PROBLEM 3: VALIDATE BST
# ============================================================

def is_valid_bst(root):
    """
    Check if a binary tree is a valid BST.
    
    Why we need ranges:
    
    Example that fails simple check:
          10
         /  \
        5   15
           /  \
          6   20
    
    Node 15: 6 < 15 < 20 ✓ (locally valid)
    BUT: 6 < 10! (globally invalid)
    
    Range approach:
    Node 10: range (-∞, +∞) ✓
    Node 5: range (-∞, 10) ✓
    Node 15: range (10, +∞) ✓
    Node 6: range (10, 15) ✗ (6 < 10!)
    
    Visual trace for valid BST:
           5
          / \
         3   7
        / \
       2   4
    
    validate(5, -∞, +∞): 
      → validate(3, -∞, 5): 
         → validate(2, -∞, 3): True
         → validate(4, 3, 5): True
      → validate(7, 5, +∞): True
    
    Result: True
    
    Time: O(n) - visit every node
    Space: O(h) for recursion
    """
    def validate(node, min_val, max_val):
        # Empty node is valid
        if not node:
            return True
        
        # Check if current node violates range
        if not (min_val < node.val < max_val):
            return False
        
        # Validate left subtree: must be in range (min_val, node.val)
        # Validate right subtree: must be in range (node.val, max_val)
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    # Start with infinite range
    return validate(root, float('-inf'), float('inf'))


# ============================================================
# PROBLEM 4 & 5: FIND MINIMUM AND MAXIMUM
# ============================================================

def find_min_bst(root):
    """
    Find minimum value in BST.
    
    Key insight: Keep going left!
    
    Visual trace:
           4
          / \
         2   7
        / \
       1   3
    
    Steps:
    1. Start at 4
    2. Go left to 2
    3. Go left to 1
    4. No more left → found minimum: 1
    
    Time: O(log n) average, O(n) worst (skewed left)
    Space: O(1)
    """
    if not root:
        return None
    
    # Keep going left until no more left child
    while root.left:
        root = root.left
    
    return root.val


def find_max_bst(root):
    """
    Find maximum value in BST.
    
    Key insight: Keep going right!
    
    Visual trace:
           4
          / \
         2   7
        / \   \
       1   3   8
    
    Steps:
    1. Start at 4
    2. Go right to 7
    3. Go right to 8
    4. No more right → found maximum: 8
    
    Time: O(log n) average, O(n) worst (skewed right)
    Space: O(1)
    """
    if not root:
        return None
    
    # Keep going right until no more right child
    while root.right:
        root = root.right
    
    return root.val


# ============================================================
# PROBLEM 6: KTH SMALLEST ELEMENT
# ============================================================

def kth_smallest(root, k):
    """
    Find kth smallest element in BST (1-indexed).
    
    Key insight: Inorder traversal = sorted order!
    
    Visual trace for k=3 in:
           5
          / \
         3   7
        / \
       2   4
    
    Inorder traversal:
    1. Visit left subtree of 5:
       - Visit left subtree of 3:
         - Visit 2 → [2] (k=1)
       - Visit 3 → [2, 3] (k=2)
       - Visit right subtree of 3:
         - Visit 4 → [2, 3, 4] (k=3) ← Found!
    
    Result: 4 (3rd smallest)
    
    Time: O(n) worst case, O(k) average
    Space: O(h) for recursion stack
    """
    # Store result during traversal
    result = []
    
    def inorder(node):
        if not node:
            return
        
        # Left → Root → Right
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    # Perform inorder traversal
    inorder(root)
    
    # Return kth element (1-indexed)
    return result[k - 1]


# Optimized version: stop early when we reach k
def kth_smallest_optimized(root, k):
    """
    Find kth smallest element (optimized - stop at k).
    
    Instead of traversing entire tree, stop when count reaches k.
    
    Visual trace for k=2 in:
           5
          / \
         3   7
        / \
       2   4
    
    Inorder with counter:
    1. Visit 2, count=1 (not k yet)
    2. Visit 3, count=2 (k reached!) → return 3
    
    Time: O(k) - stop early!
    Space: O(h) for recursion
    """
    counter = [0]  # Use list to allow modification in nested function
    result = [None]
    
    def inorder(node):
        if not node or result[0] is not None:
            return
        
        inorder(node.left)
        
        counter[0] += 1
        if counter[0] == k:
            result[0] = node.val
            return
        
        inorder(node.right)
    
    inorder(root)
    return result[0]
