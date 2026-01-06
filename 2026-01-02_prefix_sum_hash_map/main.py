# Main.py - Your Working File
# Task: Solve LeetCode #560: Subarray Sum Equals K
# Goal: Write 3 progressive approaches

# TODO 1: Approach 1 - Brute Force (nested loops)
# - Enumerate all start/end pairs and sum the subarray
# - Time: O(n²), Space: O(1)
# - Use as a correctness baseline

def subarray_sum_brute_force(nums, k):
    """
    APPROACH 1: BRUTE FORCE
    """
    n = len(nums)
    res = 0
    for i in range(n):
        running = 0
        for j in range(i, n):
            running += nums[j]
            if running == k:
                res += 1
    return res

# TODO 2: Approach 2 - Prefix Sum + Hash Map (optimal)
# - Maintain running prefix sum and counts of prefix values seen so far
# - For each prefix, add count of (prefix - k) to answer
# - Time: O(n), Space: O(n)

def subarray_sum_prefix_hash(nums, k):
    """
    APPROACH 2: PREFIX SUM + HASH MAP (OPTIMAL)
    """
    count = 0
    prefix = 0
    freq = {0: 1}
    for num in nums:
        prefix += num
        need = prefix - k
        if need in freq:
            count += freq[need]
        freq[prefix] = freq.get(prefix, 0) + 1 
 
    return count


# TODO 3: Approach 3 - Prefix Sum precompute (educational variant)
# - Precompute prefix array, then iterate all end positions and look up needed prefix in a map
# - Same complexity as Approach 2 but shows prefix array explicitly

def subarray_sum_prefix_array(nums, k):
    """
    APPROACH 3: PREFIX ARRAY + MAP (VARIANT)
    """
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    freq = {0: 1}
    res = 0
    for i in range(1, n + 1):
        current = prefix[i]
        need = current - k
        if need in freq:
            res += freq[need]
        freq[current] = freq.get(current, 0) + 1
    return res


if __name__ == "__main__":
    # Smoke tests (expand in test_cases.py)
    assert subarray_sum_prefix_hash([1, 1, 1], 2) == 2
    assert subarray_sum_prefix_hash([1, 2, 3], 3) == 2  # [1,2], [3]
    assert subarray_sum_prefix_hash([1, -1, 1], 1) == 3  # [1], [1], [1,-1,1]
    assert subarray_sum_prefix_hash([0, 0, 0], 0) == 6   # all subarrays of zeros
    assert subarray_sum_prefix_hash([], 0) == 0
    assert subarray_sum_brute_force([1, 1, 1], 2) == 2
    assert subarray_sum_prefix_array([1, 1, 1], 2) == 2
    print("Quick checks passed. Run test_cases.py for more.")
