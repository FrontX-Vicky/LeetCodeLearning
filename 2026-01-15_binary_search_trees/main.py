# Main.py - Your Working File
# Task: Implement Binary Search Tree Operations
# Goal: Master BST properties and operations

# Definition for a binary tree node
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
    
    BST Property: left < root < right
    
    Example:
           4
          / \
         2   7
        / \
       1   3
    
    search(root, 2) → Node(2)
    search(root, 5) → None
    
    Time: O(log n) average, O(n) worst
    Space: O(h) for recursion stack
    """
    # TODO: Implement recursive BST search
    if not root:
        return None
    
    if val == root.val:
        return root
    
    if val < root.val:
        return search_bst_recursive(root.left, val)
    
    return search_bst_recursive(root.right, val)


def search_bst_iterative(root, val):
    """
    Search for a value in BST (iterative).
    
    More space-efficient: O(1) space instead of O(h).
    
    Strategy:
    - Compare val with current node
    - Go left if val < node.val
    - Go right if val > node.val
    - Return when found or reach None
    """
    # TODO: Implement iterative BST search
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
    
    Example:
           4              4
          / \            / \
         2   7    →     2   7
        / \            / \   \
       1   3          1   3   5
    
    Insert 5 at correct position.
    
    Time: O(log n) average, O(n) worst
    Space: O(h) for recursion
    """
    # TODO: Implement recursive BST insertion
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_bst_recursive(root.left, val)
    else:
        root.right = insert_bst_recursive(root.right, val)

    return root


def insert_bst_iterative(root, val):
    """
    Insert a value into BST (iterative).
    
    Strategy:
    - Find the parent node where new node should be attached
    - Determine if it should be left or right child
    - Create and attach new node
    
    Space: O(1)
    """
    # TODO: Implement iterative BST insertion
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
    
    Valid:              Invalid:
          5                   5
         / \                 / \
        3   7               3   7
       / \                 / \
      2   4               2   6  ← 6 > 5!
    
    Tricky case:
          10
         /  \
        5   15
           /  \
          6   20   ← 6 < 10, invalid!
    
    Can't just check node.left < node < node.right!
    Need to track valid range for each node.
    
    Time: O(n) - visit every node
    Space: O(h) for recursion
    """
    # TODO: Implement BST validation with range checking
    # Hint: Use helper function with min_val and max_val parameters
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        # check if current node violates range
        if not (min_val < node.val < max_val):
            return False
        
        # validate left subtree: must be in range (min_val, node.val)
        # validate right subtree: must be in range (node.val, max_val)
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    # start with infinite range
    return validate(root, float('-inf'), float('inf'))


# ============================================================
# PROBLEM 4 & 5: FIND MINIMUM AND MAXIMUM
# ============================================================

def find_min_bst(root):
    """
    Find minimum value in BST.
    
    Key insight: Minimum is the leftmost node!
    
    Example:
           4
          / \
         2   7
        / \
       1   3
    
    Minimum: 1
    
    Time: O(log n) average, O(n) worst
    Space: O(1)
    """
    # TODO: Implement find minimum
    if not root:
        return None
    
    #keep going left until no more left child
    while root.left:
        root = root.left

    return root.val


def find_max_bst(root):
    """
    Find maximum value in BST.
    
    Key insight: Maximum is the rightmost node!
    
    Example:
           4
          / \
         2   7
        / \   \
       1   3   8
    
    Maximum: 8
    
    Time: O(log n) average, O(n) worst
    Space: O(1)
    """
    # TODO: Implement find maximum
    if not root:
        return None
    
    while root.right:
        root = root.right

    return root.val


# ============================================================
# PROBLEM 6: KTH SMALLEST ELEMENT
# ============================================================

def kth_smallest(root, k):
    """
    Find kth smallest element in BST (1-indexed).
    
    Key insight: Inorder traversal gives sorted order!
    
    Example:
           5
          / \
         3   7
        / \
       2   4
    
    k=1 → 2 (smallest)
    k=2 → 3
    k=3 → 4
    k=4 → 5
    
    Approach 1: Do full inorder, return result[k-1]
    Approach 2: Stop early when count reaches k (optimized)
    
    Time: O(n) worst case, O(k) if we stop early
    Space: O(h) for recursion
    """
    # TODO: Implement kth smallest
    result = []

    def inorder(node):
        if not node:
            return
        
        # left -> root -> right
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    # perform inorder traversal
    inorder(root)

    # return kth element (1 - indexed)
    return result[k - 1]


# ============================================================
# HELPER FUNCTIONS (Don't modify)
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


def print_tree(root, level=0, prefix="Root: "):
    """Helper to visualize tree structure"""
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


def tree_to_list(root):
    """Convert tree to level-order list for comparison"""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("BINARY SEARCH TREE - SMOKE TEST")
    print("=" * 60)
    
    # Build test BST: [4, 2, 7, 1, 3]
    #        4
    #       / \
    #      2   7
    #     / \
    #    1   3
    
    root = build_tree_from_list([4, 2, 7, 1, 3])
    
    print("\nBST Structure:")
    print_tree(root)
    
    print("\n" + "-" * 60)
    print("SEARCH")
    print("-" * 60)
    print(f"Search for 2 (recursive): {search_bst_recursive(root, 2)}")
    print(f"Search for 5 (recursive): {search_bst_recursive(root, 5)}")
    print(f"Search for 2 (iterative): {search_bst_iterative(root, 2)}")
    
    print("\n" + "-" * 60)
    print("INSERT")
    print("-" * 60)
    new_root = insert_bst_recursive(root, 5)
    print("After inserting 5:")
    print_tree(new_root)
    
    print("\n" + "-" * 60)
    print("VALIDATE")
    print("-" * 60)
    print(f"Is valid BST: {is_valid_bst(root)}")
    
    print("\n" + "-" * 60)
    print("MIN/MAX")
    print("-" * 60)
    print(f"Minimum value: {find_min_bst(root)}")
    print(f"Maximum value: {find_max_bst(root)}")
    
    print("\n" + "-" * 60)
    print("KTH SMALLEST")
    print("-" * 60)
    print(f"1st smallest: {kth_smallest(root, 1)}")
    print(f"2nd smallest: {kth_smallest(root, 2)}")
    print(f"3rd smallest: {kth_smallest(root, 3)}")
    
    print("\n" + "=" * 60)
    print("Run 'python test_cases.py' for full test suite!")
    print("=" * 60)
