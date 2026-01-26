# Solutions.py - Reference Implementations

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
    PREORDER RECURSIVE
    
    Time: O(n) - visit each node once
    Space: O(h) - recursion stack, h = height
    
    Process: Root → Left → Right
    """
    if not root:
        return []
    
    # Root first, then left subtree, then right subtree
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)


def preorder_iterative(root):
    """
    PREORDER ITERATIVE
    
    Time: O(n)
    Space: O(h) - explicit stack
    
    Strategy: Use stack, push right before left (LIFO)
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)  # Process root
        
        # Push right first (LIFO - left will be processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


# ============================================================
# INORDER TRAVERSAL (Left → Root → Right)
# ============================================================

def inorder_recursive(root):
    """
    INORDER RECURSIVE
    
    Time: O(n)
    Space: O(h)
    
    Process: Left → Root → Right
    **For BST, this gives sorted order!**
    """
    if not root:
        return []
    
    # Left subtree first, then root, then right subtree
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)


def inorder_iterative(root):
    """
    INORDER ITERATIVE
    
    Time: O(n)
    Space: O(h)
    
    Strategy: Go left while pushing, pop and process, go right once
    """
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Go left as far as possible
        while current:
            stack.append(current)
            current = current.left
        
        # Process node
        current = stack.pop()
        result.append(current.val)
        
        # Go right once
        current = current.right
    
    return result


# ============================================================
# POSTORDER TRAVERSAL (Left → Right → Root)
# ============================================================

def postorder_recursive(root):
    """
    POSTORDER RECURSIVE
    
    Time: O(n)
    Space: O(h)
    
    Process: Left → Right → Root
    """
    if not root:
        return []
    
    # Left subtree, right subtree, then root
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]


def postorder_iterative(root):
    """
    POSTORDER ITERATIVE (Two-Stack Method)
    
    Time: O(n)
    Space: O(h)
    
    Strategy: Use two stacks - easier than single stack approach
    """
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []
    
    # Fill stack2 in reverse postorder
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        # Push left before right (will be reversed)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    # Pop from stack2 to get postorder
    result = []
    while stack2:
        result.append(stack2.pop().val)
    
    return result


# ============================================================
# VISUAL TRACE EXAMPLES
# ============================================================
"""
TREE EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       1
      / \\
     2   3
    / \\
   4   5


PREORDER RECURSIVE TRACE (Root → Left → Right):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Call Stack:

1. preorder(1):
   - Process 1 ✓
   - Recurse left: preorder(2)
     2. preorder(2):
        - Process 2 ✓
        - Recurse left: preorder(4)
          3. preorder(4):
             - Process 4 ✓
             - Recurse left: preorder(None) → []
             - Recurse right: preorder(None) → []
             - Return [4]
        - Recurse right: preorder(5)
          4. preorder(5):
             - Process 5 ✓
             - Recurse left: preorder(None) → []
             - Recurse right: preorder(None) → []
             - Return [5]
        - Return [2, 4, 5]
   - Recurse right: preorder(3)
     5. preorder(3):
        - Process 3 ✓
        - Recurse left: preorder(None) → []
        - Recurse right: preorder(None) → []
        - Return [3]
   - Return [1, 2, 4, 5, 3]

Result: [1, 2, 4, 5, 3]


PREORDER ITERATIVE TRACE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Stack operations:

Initial: stack = [1]

Step 1: Pop 1, process 1, push right(3), push left(2)
  result = [1]
  stack = [3, 2]

Step 2: Pop 2, process 2, push right(5), push left(4)
  result = [1, 2]
  stack = [3, 5, 4]

Step 3: Pop 4, process 4, push nothing (leaf)
  result = [1, 2, 4]
  stack = [3, 5]

Step 4: Pop 5, process 5, push nothing (leaf)
  result = [1, 2, 4, 5]
  stack = [3]

Step 5: Pop 3, process 3, push nothing (leaf)
  result = [1, 2, 4, 5, 3]
  stack = []

Result: [1, 2, 4, 5, 3] ✓


INORDER RECURSIVE TRACE (Left → Root → Right):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Call Stack:

1. inorder(1):
   - Recurse left: inorder(2)
     2. inorder(2):
        - Recurse left: inorder(4)
          3. inorder(4):
             - Recurse left: inorder(None) → []
             - Process 4 ✓
             - Recurse right: inorder(None) → []
             - Return [4]
        - Process 2 ✓
        - Recurse right: inorder(5)
          4. inorder(5):
             - Recurse left: inorder(None) → []
             - Process 5 ✓
             - Recurse right: inorder(None) → []
             - Return [5]
        - Return [4, 2, 5]
   - Process 1 ✓
   - Recurse right: inorder(3)
     5. inorder(3):
        - Recurse left: inorder(None) → []
        - Process 3 ✓
        - Recurse right: inorder(None) → []
        - Return [3]
   - Return [4, 2, 5, 1, 3]

Result: [4, 2, 5, 1, 3]


INORDER ITERATIVE TRACE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Stack operations:

Initial: current = 1, stack = []

Step 1: Go left - push 1, move to 2
  stack = [1], current = 2

Step 2: Go left - push 2, move to 4
  stack = [1, 2], current = 4

Step 3: Go left - push 4, move to None
  stack = [1, 2, 4], current = None

Step 4: Pop 4, process 4, move to None
  result = [4]
  stack = [1, 2], current = None

Step 5: Pop 2, process 2, move to 5
  result = [4, 2]
  stack = [1], current = 5

Step 6: Go left - push 5, move to None
  stack = [1, 5], current = None

Step 7: Pop 5, process 5, move to None
  result = [4, 2, 5]
  stack = [1], current = None

Step 8: Pop 1, process 1, move to 3
  result = [4, 2, 5, 1]
  stack = [], current = 3

Step 9: Go left - push 3, move to None
  stack = [3], current = None

Step 10: Pop 3, process 3, move to None
  result = [4, 2, 5, 1, 3]
  stack = [], current = None

Result: [4, 2, 5, 1, 3] ✓


POSTORDER RECURSIVE TRACE (Left → Right → Root):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Call Stack:

1. postorder(1):
   - Recurse left: postorder(2)
     2. postorder(2):
        - Recurse left: postorder(4)
          3. postorder(4):
             - Recurse left: postorder(None) → []
             - Recurse right: postorder(None) → []
             - Process 4 ✓
             - Return [4]
        - Recurse right: postorder(5)
          4. postorder(5):
             - Recurse left: postorder(None) → []
             - Recurse right: postorder(None) → []
             - Process 5 ✓
             - Return [5]
        - Process 2 ✓
        - Return [4, 5, 2]
   - Recurse right: postorder(3)
     5. postorder(3):
        - Recurse left: postorder(None) → []
        - Recurse right: postorder(None) → []
        - Process 3 ✓
        - Return [3]
   - Process 1 ✓
   - Return [4, 5, 2, 3, 1]

Result: [4, 5, 2, 3, 1]


POSTORDER ITERATIVE (Two-Stack) TRACE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Two-stack method (easier than single stack):

Initial: stack1 = [1], stack2 = []

Step 1: Pop 1 from stack1, push to stack2, push left(2), push right(3)
  stack1 = [2, 3]
  stack2 = [1]

Step 2: Pop 3 from stack1, push to stack2, push nothing (leaf)
  stack1 = [2]
  stack2 = [1, 3]

Step 3: Pop 2 from stack1, push to stack2, push left(4), push right(5)
  stack1 = [4, 5]
  stack2 = [1, 3, 2]

Step 4: Pop 5 from stack1, push to stack2, push nothing (leaf)
  stack1 = [4]
  stack2 = [1, 3, 2, 5]

Step 5: Pop 4 from stack1, push to stack2, push nothing (leaf)
  stack1 = []
  stack2 = [1, 3, 2, 5, 4]

Now pop from stack2:
  Pop 4 → result = [4]
  Pop 5 → result = [4, 5]
  Pop 2 → result = [4, 5, 2]
  Pop 3 → result = [4, 5, 2, 3]
  Pop 1 → result = [4, 5, 2, 3, 1]

Result: [4, 5, 2, 3, 1] ✓


WHY INORDER IS SPECIAL FOR BST:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Binary Search Tree:
       4
      / \\
     2   6
    / \\ / \\
   1  3 5  7

Inorder traversal:
  Visit 1 → 2 → 3 → 4 → 5 → 6 → 7
  Result: [1, 2, 3, 4, 5, 6, 7] ← SORTED!

This is why inorder is crucial for BST operations:
- Validate BST: check if inorder is sorted
- Find kth smallest: do inorder, stop at k
- Convert to sorted array: just do inorder!
"""
