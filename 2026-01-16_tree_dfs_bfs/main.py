# Main.py - Your Working File
# Task: Implement Tree DFS and BFS Algorithms
# Goal: Master depth-first and breadth-first traversals

# Definition for a binary tree node
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
    
    Depth = number of nodes along longest path from root to leaf.
    
    Example:
           3
          / \
         9  20
           /  \
          15   7
    
    Max depth: 3 (path: 3 → 20 → 15 or 7)
    
    Approach: depth = 1 + max(left_depth, right_depth)
    
    Time: O(n)
    Space: O(h) for recursion stack
    """
    # TODO: Implement recursive max depth
    pass


def max_depth_bfs(root):
    """
    Find maximum depth of binary tree (BFS iterative).
    
    Count levels while doing level-order traversal.
    
    Time: O(n)
    Space: O(w) where w = max width
    """
    # TODO: Implement BFS max depth
    pass


# ============================================================
# PROBLEM 2: MINIMUM DEPTH OF BINARY TREE
# ============================================================

def min_depth_recursive(root):
    """
    Find minimum depth to nearest leaf node (DFS recursive).
    
    Example:
           3
          / \
         9  20
           /  \
          15   7
    
    Min depth: 2 (path: 3 → 9, since 9 is a leaf)
    
    Key: Must reach a LEAF node (no children).
    
    Tricky case:
           1
          /
         2
    
    Min depth: 2 (not 1, because 1 is not a leaf)
    
    Time: O(n)
    Space: O(h)
    """
    # TODO: Implement recursive min depth
    pass


def min_depth_bfs(root):
    """
    Find minimum depth to nearest leaf node (BFS iterative).
    
    BFS naturally finds shortest path!
    Stop as soon as we find a leaf.
    
    Time: O(n) worst case, but can stop early
    Space: O(w)
    """
    # TODO: Implement BFS min depth
    pass


# ============================================================
# PROBLEM 3: PATH SUM
# ============================================================

def has_path_sum(root, target_sum):
    """
    Check if tree has root-to-leaf path with given sum.
    
    Example:
           5
          / \
         4   8
        /   / \
       11  13  4
      /  \      \
     7    2      1
    
    Target: 22
    Path: 5 → 4 → 11 → 2 = 22 ✓
    
    Approach:
    - Subtract current node value from target
    - Check if we reach 0 at a leaf node
    
    Time: O(n)
    Space: O(h)
    """
    # TODO: Implement path sum check
    pass


# ============================================================
# PROBLEM 4: LEVEL ORDER TRAVERSAL (BFS)
# ============================================================

def level_order(root):
    """
    Return level-order traversal as list of lists.
    
    Example:
           3
          / \
         9  20
           /  \
          15   7
    
    Result: [[3], [9, 20], [15, 7]]
    
    Key technique: Track level size before processing.
    
    Time: O(n)
    Space: O(w) for queue
    """
    # TODO: Implement level order traversal
    pass


# ============================================================
# PROBLEM 5: RIGHT SIDE VIEW
# ============================================================

def right_side_view(root):
    """
    Return values visible from right side of tree.
    
    Example:
           1
          / \
         2   3
          \   \
           5   4
    
    Right view: [1, 3, 4]
    (Rightmost node at each level)
    
    Approach: BFS, take last node of each level.
    
    Time: O(n)
    Space: O(w)
    """
    # TODO: Implement right side view
    pass


# ============================================================
# PROBLEM 6: SYMMETRIC TREE
# ============================================================

def is_symmetric(root):
    """
    Check if tree is mirror of itself.
    
    Example (symmetric):
           1
          / \
         2   2
        / \ / \
       3  4 4  3
    
    Example (not symmetric):
           1
          / \
         2   2
          \   \
           3   3
    
    Approach: Compare left and right subtrees.
    Left's left must equal Right's right.
    Left's right must equal Right's left.
    
    Time: O(n)
    Space: O(h)
    """
    # TODO: Implement symmetric tree check
    pass


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


if __name__ == "__main__":
    print("=" * 60)
    print("TREE DFS & BFS - SMOKE TEST")
    print("=" * 60)
    
    # Build test tree: [3, 9, 20, None, None, 15, 7]
    #        3
    #       / \
    #      9  20
    #        /  \
    #       15   7
    
    root = build_tree_from_list([3, 9, 20, None, None, 15, 7])
    
    print("\nTree Structure:")
    print_tree(root)
    
    print("\n" + "-" * 60)
    print("MAXIMUM DEPTH")
    print("-" * 60)
    print(f"Recursive: {max_depth_recursive(root)}")
    print(f"BFS:       {max_depth_bfs(root)}")
    print(f"Expected:  3")
    
    print("\n" + "-" * 60)
    print("MINIMUM DEPTH")
    print("-" * 60)
    print(f"Recursive: {min_depth_recursive(root)}")
    print(f"BFS:       {min_depth_bfs(root)}")
    print(f"Expected:  2")
    
    print("\n" + "-" * 60)
    print("PATH SUM")
    print("-" * 60)
    print(f"Has path sum 32? {has_path_sum(root, 32)}")
    print(f"Expected: True (3 + 9 + 20 = 32)")
    print(f"Has path sum 100? {has_path_sum(root, 100)}")
    print(f"Expected: False")
    
    print("\n" + "-" * 60)
    print("LEVEL ORDER TRAVERSAL")
    print("-" * 60)
    print(f"Result:   {level_order(root)}")
    print(f"Expected: [[3], [9, 20], [15, 7]]")
    
    print("\n" + "-" * 60)
    print("RIGHT SIDE VIEW")
    print("-" * 60)
    print(f"Result:   {right_side_view(root)}")
    print(f"Expected: [3, 20, 7]")
    
    print("\n" + "-" * 60)
    print("SYMMETRIC TREE")
    print("-" * 60)
    symmetric_tree = build_tree_from_list([1, 2, 2, 3, 4, 4, 3])
    print(f"Result:   {is_symmetric(symmetric_tree)}")
    print(f"Expected: True")
    
    print("\n" + "=" * 60)
    print("Run 'python test_cases.py' for full test suite!")
    print("=" * 60)
