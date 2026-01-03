# Solutions.py - Reference Solutions
# Clean, optimized, fully-commented implementations

def two_sum_optimal(nums: list, target: int) -> list:
    """
    TWO SUM - Hash Map Approach (OPTIMAL)
    
    Algorithm:
    1. Create an empty dictionary to store (number -> index) pairs
    2. Iterate through the array once
    3. For each number, calculate complement = target - number
    4. Check if complement exists in dictionary
       - If YES: return [index_of_complement, current_index]
       - If NO: add current number to dictionary and continue
    5. If no solution found, return empty (won't happen per LeetCode guarantee)
    
    Time Complexity: O(n)
    - Single pass through array: O(n)
    - Dictionary lookup & insertion: O(1) average case
    
    Space Complexity: O(n)
    - Dictionary stores up to n numbers
    
    Why this is optimal:
    - Only one pass through data (can't do better than O(n))
    - Fast lookups with hash map
    - Preserves original indices
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
    """
    seen = {}  # Dictionary: number -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if we've already seen the complement
        if complement in seen:
            return [seen[complement], i]
        
        # Store current number and its index for future lookups
        seen[num] = i
    
    return []  # No solution found (shouldn't happen per LeetCode constraints)


def two_sum_brute_force(nums: list, target: int) -> list:
    """
    TWO SUM - Brute Force Approach (REFERENCE - DO NOT USE IN PRODUCTION)
    
    Algorithm:
    1. Check every pair of numbers (nested loops)
    2. Return indices when sum equals target
    
    Time Complexity: O(n²)
    - Outer loop: O(n)
    - Inner loop: O(n)
    - Combined: O(n²) - becomes very slow for large inputs
    
    Space Complexity: O(1)
    - No extra data structures
    
    Why NOT optimal:
    - Redundant comparisons (checks same pairs multiple times)
    - Scales poorly (100,000 numbers → 10 billion operations)
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []


def two_sum_two_pointers(nums: list, target: int) -> list:
    """
    TWO SUM - Two Pointers Approach (REFERENCE - NOT SUITABLE FOR THIS PROBLEM)
    
    Algorithm:
    1. Create list of (value, original_index) pairs
    2. Sort by value
    3. Use two pointers from both ends
    4. Move pointers based on sum vs target
    
    Time Complexity: O(n log n)
    - Sorting dominates: O(n log n)
    - Two-pointer traversal: O(n)
    - Combined: O(n log n)
    
    Space Complexity: O(n)
    - Extra list for (value, index) pairs
    
    IMPORTANT: This loses original indices during sorting!
    For THIS problem (return original indices), use Hash Map instead.
    But this approach is useful for:
    - Finding values only (not indices)
    - When array is already sorted
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List of two indices from original array
    """
    # Create pairs of (value, original_index)
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    # Sort by value
    indexed_nums.sort()
    
    left, right = 0, len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            # Return original indices
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


# ============================================================================
# SUMMARY: Which Approach to Use?
# ============================================================================
"""
Problem: LeetCode #1 - Two Sum

RECOMMENDATION FOR THIS PROBLEM:
✅ Use: two_sum_optimal() - Hash Map approach
  - Reason: O(n) time, returns original indices

❌ Avoid: two_sum_brute_force()
  - Reason: O(n²) is too slow for large inputs

❌ Avoid: two_sum_two_pointers() 
  - Reason: O(n log n) is slower and loses index order

LEARNING PATTERN TO REMEMBER:
When you need to "find a pair with property X":
1. First ask: "Can I use a hash map/set for O(1) lookups?"
2. If YES → Hash Map approach is usually optimal
3. If NO → Consider two pointers or other techniques
"""
