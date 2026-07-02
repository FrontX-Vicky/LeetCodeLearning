# Main.py - Your Working File
# Task: Solve LeetCode #1: Two Sum
# Goal: Write 3 progressive approaches

# TODO 1: Write Approach 1 - Brute Force (nested loops)
# - Check every pair of numbers
# - Return indices when sum equals target
# - Time: O(n²), Space: O(1)
# - Don't optimize yet; just make it work

def two_sum_brute_force(nums, target):
    """
    APPROACH 1: BRUTE FORCE
    - Try every pair
    """
    # YOUR CODE HERE
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []


# TODO 2: Write Approach 2 - Hash Map Single Pass
# - Iterate once through the array
# - Store numbers in a dictionary as you go
# - For each number, check if complement (target - num) exists
# - Return indices immediately when found
# - Time: O(n), Space: O(n)
# - More efficient; this is the "sweet spot" for most cases

def two_sum_hash_map(nums, target):
    """
    APPROACH 2: HASH MAP (OPTIMIZED)
    - Single pass with dictionary lookup
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []

# TODO 3: Understand Approach 3 - Two Pointers (reference only)
# - This approach requires sorting, which loses original indices
# - Useful when you only need values, not indices
# - Mention in your comments why we don't use it here

def two_sum_two_pointers(nums, target):
    """
    APPROACH 3: TWO POINTERS (REFERENCE)
    - Sort and converge from both ends
    - NOTE: This loses original indices, so not suitable for THIS problem
    - But it's useful for other variations
    """
    # YOUR CODE HERE
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    indexed_nums.sort()

    left, right = 0, len(indexed_nums) - 1
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]

        if current_sum == target:
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

# Test your code (write at least 5 test cases)
if __name__ == "__main__":
    # Test Case 1: Basic example
    assert two_sum_hash_map([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_brute_force([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_two_pointers([2, 7, 11, 15], 9) == [0, 1]
    
    # Test Case 2: Different indices
    assert two_sum_hash_map([3, 2, 4], 6) == [1, 2]
    assert two_sum_brute_force([3, 2, 4], 6) == [1, 2]
    assert two_sum_two_pointers([3, 2, 4], 6) == [1, 2]

    
    # Test Case 3: Edge case
    assert two_sum_hash_map([3, 3], 6) == [0, 1]
    assert two_sum_brute_force([3, 3], 6) == [0, 1]
    assert two_sum_two_pointers([3, 3], 6) == [0, 1]

    #no solution cases
    assert two_sum_hash_map([], 6) == []
    assert two_sum_brute_force([], 6) == []
    assert two_sum_two_pointers([], 6) == []

    assert two_sum_hash_map([1, 2, 3], 100) == []
    assert two_sum_brute_force([1, 2, 3], 100) == []
    assert two_sum_two_pointers([1, 2, 3], 100) == [] 
    
    # Test Case 4: Duplicates
    assert two_sum_hash_map([0, 0], 0) == [0, 1]
    assert two_sum_brute_force([0, 0], 0) == [0, 1]
    assert two_sum_two_pointers([0, 0], 0) == [0, 1]
    
    
    # Test Case 5: Negative numbers
    assert two_sum_hash_map([-1, -2, -3, 5, 10], 7) == [2, 4]
    assert two_sum_brute_force([-1, -2, -3, 5, 10], 7) == [2, 4]
    assert two_sum_two_pointers([-1, -2, -3, 5, 10], 7) == [2, 4]
    
    print("All tests passed!")
