# Main.py - Your Working File
# Task: Implement Binary Tree Traversals
# Goal: Master preorder, inorder, and postorder traversals

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PREORDER TRAVERSAL (Root → Left → Right)
# ============================================================

def preorder_recursive(root):
    """
    PREORDER: Root → Left → Right
    
    Process root first, then recursively traverse left and right.
    
    Example:
           1
          / \
         2   3
        / \
       4   5
    
    Order: 1 → 2 → 4 → 5 → 3
    Result: [1, 2, 4, 5, 3]
    """
    # Your code here
    pass


def preorder_iterative(root):
    """
    PREORDER: Iterative with stack
    
    Strategy:
    1. Push root to stack
    2. Pop node, process it, push right child, push left child
    3. Repeat until stack empty
    
    Why right before left? Stack is LIFO - left will be popped first!
    """
    # Your code here
    pass


# ============================================================
# INORDER TRAVERSAL (Left → Root → Right)
# ============================================================

def inorder_recursive(root):
    """
    INORDER: Left → Root → Right
    
    Process left subtree, then root, then right subtree.
    **Important: For BST, this gives sorted order!**
    
    Example:
           1
          / \
         2   3
        / \
       4   5
    
    Order: 4 → 2 → 5 → 1 → 3
    Result: [4, 2, 5, 1, 3]
    """
    # Your code here
    pass


def inorder_iterative(root):
    """
    INORDER: Iterative with stack
    
    Strategy:
    1. Go left as far as possible, pushing all nodes
    2. Pop node, process it
    3. Go right once
    4. Repeat
    
    Trickier than preorder because we don't process while pushing.
    """
    # Your code here
    pass


# ============================================================
# POSTORDER TRAVERSAL (Left → Right → Root)
# ============================================================

def postorder_recursive(root):
    """
    POSTORDER: Left → Right → Root
    
    Process left subtree, right subtree, then root.
    Used for: deleting tree, calculating height.
    
    Example:
           1
          / \
         2   3
        / \
       4   5
    
    Order: 4 → 5 → 2 → 3 → 1
    Result: [4, 5, 2, 3, 1]
    """
    # Your code here
    pass


def postorder_iterative(root):
    """
    POSTORDER: Iterative with stack
    
    Strategy (two-stack method - easier):
    1. Use stack1 for traversal, stack2 for result
    2. Push root to stack1
    3. Pop from stack1, push to stack2, push left, push right
    4. Pop all from stack2 for final result
    
    Alternative: Single stack with visited tracking (more complex)
    """
    # Your code here
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
    # Quick smoke test
    print("=" * 60)
    print("BINARY TREE TRAVERSAL SMOKE TEST")
    print("=" * 60)
    
    # Build test tree: [1, 2, 3, 4, 5]
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    
    root = build_tree_from_list([1, 2, 3, 4, 5])
    
    print("\nTree Structure:")
    print_tree(root)
    
    print("\n" + "-" * 60)
    print("PREORDER (Root → Left → Right)")
    print("-" * 60)
    print(f"Recursive:  {preorder_recursive(root)}")
    print(f"Expected:   [1, 2, 4, 5, 3]")
    print(f"Iterative:  {preorder_iterative(root)}")
    
    print("\n" + "-" * 60)
    print("INORDER (Left → Root → Right)")
    print("-" * 60)
    print(f"Recursive:  {inorder_recursive(root)}")
    print(f"Expected:   [4, 2, 5, 1, 3]")
    print(f"Iterative:  {inorder_iterative(root)}")
    
    print("\n" + "-" * 60)
    print("POSTORDER (Left → Right → Root)")
    print("-" * 60)
    print(f"Recursive:  {postorder_recursive(root)}")
    print(f"Expected:   [4, 5, 2, 3, 1]")
    print(f"Iterative:  {postorder_iterative(root)}")
    
    print("\n" + "=" * 60)
    print("Run 'python test_cases.py' for full test suite!")
    print("=" * 60)
