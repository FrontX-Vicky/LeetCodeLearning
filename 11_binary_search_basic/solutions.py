# Solutions.py - Reference Implementations
# These are complete solutions for you to compare against

def binary_search_iterative(nums, target):
    """
    APPROACH 1: ITERATIVE BINARY SEARCH (Classic Template)
    
    Time: O(log n) - halve search space each iteration
    Space: O(1) - only use two pointers
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:  # NOTE: <= because single element valid
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # Target in right half, exclude mid
        else:
            right = mid - 1  # Target in left half, exclude mid
    
    return -1  # Target not found


def binary_search_recursive(nums, target, left=None, right=None):
    """
    APPROACH 2: RECURSIVE BINARY SEARCH
    
    Time: O(log n) - log n recursive calls
    Space: O(log n) - recursion call stack
    """
    # Initialize boundaries on first call
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1
    
    # Base case: search space exhausted
    if left > right:
        return -1
    
    # Calculate middle
    mid = (left + right) // 2
    
    # Check if found
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        # Search right half [mid+1, right]
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        # Search left half [left, mid-1]
        return binary_search_recursive(nums, target, left, mid - 1)


def binary_search_safe(nums, target):
    """
    APPROACH 3: SAFE MID CALCULATION (Prevents Overflow)
    
    Uses: mid = left + (right - left) // 2
    Mathematically equivalent to (left + right) // 2
    But prevents overflow in languages with fixed-size integers
    
    Time: O(log n)
    Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        # Safe mid calculation (industry standard)
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


# ============================================================
# VISUAL TRACE EXAMPLE
# ============================================================
"""
Example: nums = [-1, 0, 3, 5, 9, 12], target = 9

ITERATIVE TRACE:
--------------
Initial: left=0, right=5

Iteration 1:
  mid = (0 + 5) // 2 = 2
  nums[2] = 3
  3 < 9 → search right half
  left = mid + 1 = 3

Iteration 2:
  mid = (3 + 5) // 2 = 4
  nums[4] = 9
  9 == 9 → FOUND!
  return 4

RECURSIVE TRACE:
---------------
Call 1: search(nums, 9, left=0, right=5)
  mid = 2, nums[2] = 3 < 9
  → search(nums, 9, left=3, right=5)
  
Call 2: search(nums, 9, left=3, right=5)
  mid = 4, nums[4] = 9 == 9
  → return 4
  
Call 1 returns: 4

SAFE MID CALCULATION:
--------------------
Instead of: mid = (left + right) // 2
Use:        mid = left + (right - left) // 2

Why?
- If left=2147483640, right=2147483647 (near max int in Java)
- left + right = 4294967287 → OVERFLOW! (wraps to negative)
- left + (right-left)//2 = 2147483640 + 3 = 2147483643 ✓

Python doesn't have this issue (arbitrary precision integers)
But use safe version for interview best practices!
"""
