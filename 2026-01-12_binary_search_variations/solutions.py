# Solutions.py - Reference Implementations
# These are complete solutions for you to compare against

def search_range_two_binary(nums, target):
    """
    APPROACH 1: TWO MODIFIED BINARY SEARCHES (Optimal)
    
    Time: O(log n) - two independent binary searches
    Space: O(1) - only use pointers
    """
    
    def find_leftmost(nums, target):
        """Find FIRST occurrence of target"""
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                result = mid        # Save this position
                right = mid - 1     # Keep searching LEFT for earlier occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    def find_rightmost(nums, target):
        """Find LAST occurrence of target"""
        left, right = 0, len(nums) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                result = mid        # Save this position
                left = mid + 1      # Keep searching RIGHT for later occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    # Find boundaries
    left = find_leftmost(nums, target)
    right = find_rightmost(nums, target)
    
    return [left, right]


def search_range_expand(nums, target):
    """
    APPROACH 2: FIND ANY, THEN EXPAND LINEARLY
    
    Time: O(n) worst case - if all elements are target
    Space: O(1)
    
    Not optimal but educational!
    """
    if not nums:
        return [-1, -1]
    
    # Standard binary search to find ANY occurrence
    left, right = 0, len(nums) - 1
    found_idx = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            found_idx = mid
            break  # Found any occurrence, stop here
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Not found
    if found_idx == -1:
        return [-1, -1]
    
    # Expand left to find first occurrence
    first = found_idx
    while first > 0 and nums[first - 1] == target:
        first -= 1
    
    # Expand right to find last occurrence
    last = found_idx
    while last < len(nums) - 1 and nums[last + 1] == target:
        last += 1
    
    return [first, last]


def search_range_bisect(nums, target):
    """
    APPROACH 3: PYTHON BISECT (LIBRARY SOLUTION)
    
    Time: O(log n) - bisect uses binary search internally
    Space: O(1)
    
    Elegant but may not satisfy "implement the algorithm" requirement.
    """
    from bisect import bisect_left, bisect_right
    
    if not nums:
        return [-1, -1]
    
    # bisect_left: leftmost position to insert (first occurrence)
    left = bisect_left(nums, target)
    
    # bisect_right: rightmost position to insert (one past last occurrence)
    right = bisect_right(nums, target) - 1
    
    # Validate: check if target actually exists
    if left < len(nums) and nums[left] == target:
        return [left, right]
    else:
        return [-1, -1]


# ============================================================
# VISUAL TRACE EXAMPLE
# ============================================================
"""
Example: nums = [5, 7, 7, 7, 7, 10], target = 7

FINDING LEFTMOST (FIRST) OCCURRENCE:
────────────────────────────────────────────────
Initial: left=0, right=5

Iteration 1:
  mid = 2, nums[2] = 7
  7 == 7 → SAVE result=2
          Continue searching LEFT for earlier 7
          right = mid - 1 = 1

Iteration 2:
  mid = 0, nums[0] = 5
  5 < 7 → Target in right half
         left = mid + 1 = 1

Iteration 3:
  mid = 1, nums[1] = 7
  7 == 7 → SAVE result=1
          Continue searching LEFT
          right = mid - 1 = 0

Iteration 4:
  left=1, right=0 → left > right, exit loop
  Return result = 1 ✓ (leftmost 7 is at index 1)


FINDING RIGHTMOST (LAST) OCCURRENCE:
────────────────────────────────────────────────
Initial: left=0, right=5

Iteration 1:
  mid = 2, nums[2] = 7
  7 == 7 → SAVE result=2
          Continue searching RIGHT for later 7
          left = mid + 1 = 3

Iteration 2:
  mid = 4, nums[4] = 7
  7 == 7 → SAVE result=4
          Continue searching RIGHT
          left = mid + 1 = 5

Iteration 3:
  mid = 5, nums[5] = 10
  10 > 7 → Target in left half
          right = mid - 1 = 4

Iteration 4:
  left=5, right=4 → left > right, exit loop
  Return result = 4 ✓ (rightmost 7 is at index 4)


FINAL RESULT: [1, 4]


WHY WE NEED THE result VARIABLE:
────────────────────────────────────────────────
Without it:
  When found, we continue searching
  Loop exits when left > right
  We'd return -1 (no explicit return) → WRONG!

With it:
  When found, we SAVE the index in result
  Continue searching to narrow bounds
  Loop exits → return the LAST saved index ✓


BISECT EXPLANATION:
────────────────────────────────────────────────
Array: [5, 7, 7, 7, 7, 10]
       0  1  2  3  4   5

bisect_left(nums, 7):
  "Where would I insert 7 to keep it leftmost?"
  Answer: index 1 (before existing 7s)
  
bisect_right(nums, 7):
  "Where would I insert 7 to keep it rightmost?"
  Answer: index 5 (after existing 7s)
  Last occurrence = bisect_right - 1 = 4

Result: [1, 4] ✓
"""
