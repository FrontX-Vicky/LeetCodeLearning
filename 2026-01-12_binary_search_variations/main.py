# Main.py - Your Working File
# Task: Solve LeetCode #34: Find First and Last Position
# Goal: Find range of target in sorted array with O(log n) time

# TODO 1: Approach 1 - Two Binary Searches (Optimal)
# - Find leftmost occurrence (keep searching left when found)
# - Find rightmost occurrence (keep searching right when found)
# - Time: O(log n), Space: O(1)

def search_range_two_binary(nums, target):
    """
    APPROACH 1: TWO MODIFIED BINARY SEARCHES
    
    The optimal O(log n) solution.
    
    Args:
        nums: sorted list of integers (may have duplicates)
        target: integer to find range for
    
    Returns:
        [first_index, last_index] or [-1, -1] if not found
    
    Example:
        nums = [5, 7, 7, 8, 8, 10], target = 8
        Find leftmost 8 → index 3
        Find rightmost 8 → index 4
        Return [3, 4]
    """
    def find_leftmost(nums, target):
        # Your code here to find FIRST occurrence
        pass
    
    def find_rightmost(nums, target):
        # Your code here to find LAST occurrence
        pass
    
    # Use helper functions
    left = find_leftmost(nums, target)
    right = find_rightmost(nums, target)
    
    return [left, right]


# TODO 2: Approach 2 - Find One, Expand Linearly
# - Use standard binary search to find ANY occurrence
# - Expand left and right linearly to find boundaries
# - Time: O(n) worst case, Space: O(1)

def search_range_expand(nums, target):
    """
    APPROACH 2: FIND ANY, THEN EXPAND
    
    Quick but not optimal (O(n) worst case).
    Educational - shows why we need modified binary search.
    
    Args:
        nums: sorted list of integers
        target: integer to find range for
    
    Returns:
        [first_index, last_index] or [-1, -1] if not found
    
    Example:
        nums = [5, 7, 7, 8, 8, 10], target = 8
        Binary search finds index 3 or 4 (any 8)
        Expand left: check indices 2, 1, ... (stop at 7)
        Expand right: check indices 5, 6, ... (stop at 10)
        Return [3, 4]
    """
    # Your code here
    pass


# TODO 3: Approach 3 - Using Python's bisect
# - Use bisect_left for leftmost position
# - Use bisect_right for rightmost position
# - Time: O(log n), Space: O(1)

def search_range_bisect(nums, target):
    """
    APPROACH 3: PYTHON BISECT (LIBRARY SOLUTION)
    
    Elegant one-liner using Python's built-in binary search.
    
    Args:
        nums: sorted list of integers
        target: integer to find range for
    
    Returns:
        [first_index, last_index] or [-1, -1] if not found
    
    How bisect works:
        bisect_left(nums, target): leftmost position to INSERT target
        bisect_right(nums, target): rightmost position to INSERT target
        
        If target exists:
          bisect_left = first occurrence
          bisect_right - 1 = last occurrence
    """
    # Your code here
    # from bisect import bisect_left, bisect_right
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
    test_nums = [5, 7, 7, 8, 8, 10]
    test_target = 8
    
    print("Running quick smoke test...")
    print(f"Array: {test_nums}")
    print(f"Target: {test_target}")
    print()
    
    result1 = search_range_two_binary(test_nums, test_target)
    print(f"Two Binary result: {result1} (expected: [3, 4])")
    
    result2 = search_range_expand(test_nums, test_target)
    print(f"Expand result: {result2} (expected: [3, 4])")
    
    result3 = search_range_bisect(test_nums, test_target)
    print(f"Bisect result: {result3} (expected: [3, 4])")
    
    print("\nRun 'python test_cases.py' for full test suite!")
