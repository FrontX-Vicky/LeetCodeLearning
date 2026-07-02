# solutions.py - Reference solutions for Subarray Sum Equals K


def subarray_sum_prefix_hash(nums, k):
    """
    Optimal: Prefix Sum + Hash Map
    Time: O(n), Space: O(n)
    """
    count = 0
    prefix = 0
    freq = {0: 1}  # prefix sum 0 seen once (empty prefix)

    for num in nums:
        prefix += num
        need = prefix - k
        if need in freq:
            count += freq[need]
        freq[prefix] = freq.get(prefix, 0) + 1

    return count


def subarray_sum_brute_force(nums, k):
    """
    Baseline: O(n^2) time, O(1) space
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


def subarray_sum_prefix_array(nums, k):
    """
    Variant: Explicit prefix array + map lookup
    Same complexity as prefix_hash
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


# Which to use?
# Use subarray_sum_prefix_hash as the primary solution; the others are for learning and cross-checking.
