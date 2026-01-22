# Main.py - Your Working File
# Task: Solve LeetCode #704: Binary Search
# Goal: Implement classic binary search with O(log n) time complexity

# TODO 1: Approach 1 - Iterative Binary Search (Classic Template)
# - Use left and right pointers
# - Loop while left <= right
# - Calculate mid, compare with target
# - Time: O(log n), Space: O(1)

def binary_search_iterative(nums, target):
    """
    APPROACH 1: ITERATIVE BINARY SEARCH
    
    Classic template - master this pattern!
    
    Args:
        nums: sorted list of integers
        target: integer to find
    
    Returns:
        index of target, or -1 if not found
    
    Example:
        nums = [-1, 0, 3, 5, 9, 12], target = 9
        Step 1: left=0, right=5, mid=2, nums[2]=3 < 9 → left=3
        Step 2: left=3, right=5, mid=4, nums[4]=9 == 9 → return 4
    """
    # Your code here
    pass


# TODO 2: Approach 2 - Recursive Binary Search
# - Base case: left > right → not found
# - Calculate mid, compare with target
# - Recursively search left or right half
# - Time: O(log n), Space: O(log n) call stack

def binary_search_recursive(nums, target, left=None, right=None):
    """
    APPROACH 2: RECURSIVE BINARY SEARCH
    
    Elegant recursion approach.
    
    Args:
        nums: sorted list of integers
        target: integer to find
        left: left boundary (defaults to 0)
        right: right boundary (defaults to len(nums)-1)
    
    Returns:
        index of target, or -1 if not found
    
    Example:
        nums = [-1, 0, 3, 5, 9, 12], target = 9
        Call 1: search(0, 5) → mid=2, 3 < 9 → search(3, 5)
        Call 2: search(3, 5) → mid=4, 9 == 9 → return 4
    """
    # Initialize left and right on first call
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1
    
    # Your code here
    pass


# TODO 3: Approach 3 - Safe Mid Calculation (Avoids Overflow)
# - Same as Approach 1 but use: mid = left + (right - left) // 2
# - Prevents integer overflow in other languages
# - Time: O(log n), Space: O(1)

def binary_search_safe(nums, target):
    """
    APPROACH 3: SAFE MID CALCULATION
    
    Industry-standard implementation preventing overflow.
    Uses: mid = left + (right - left) // 2
    
    Args:
        nums: sorted list of integers
        target: integer to find
    
    Returns:
        index of target, or -1 if not found
    
    Why it matters:
        In Java/C++, (left + right) can overflow if both are large.
        left + (right - left) // 2 is mathematically equivalent but safe.
        Python handles big integers, but this is interview best practice.
    """
    # Your code here
    pass


# ============================================================
# TESTING HELPERS (Don't modify)
# ============================================================

def test_function(func, nums, target, expected):
    """Helper to test a single function"""
    result = func(nums[:], target)  # Pass copy to avoid mutation
    return result == expected, result


if __name__ == "__main__":
    # Quick smoke test
    test_nums = [-1, 0, 3, 5, 9, 12]
    test_target = 9
    
    print("Running quick smoke test...")
    print(f"Array: {test_nums}")
    print(f"Target: {test_target}")
    print()
    
    result1 = binary_search_iterative(test_nums, test_target)
    print(f"Iterative result: {result1} (expected: 4)")
    
    result2 = binary_search_recursive(test_nums, test_target)
    print(f"Recursive result: {result2} (expected: 4)")
    
    result3 = binary_search_safe(test_nums, test_target)
    print(f"Safe Mid result: {result3} (expected: 4)")
    
    print("\nRun 'python test_cases.py' for full test suite!")
