# solutions.py - Reference solutions


def longest_substring_sliding_window(s):
    """
    Optimal: Sliding Window + Set
    Time: O(n), Space: O(min(n, charset))
    """
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # Shrink window until duplicate is removed
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


def longest_substring_with_indices(s):
    """
    Variant: Sliding Window + Dict (tracks last index)
    Time: O(n), Space: O(min(n, charset))
    Advantage: Jump left directly instead of incrementing one by one
    """
    char_index = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in char_index:
            # Jump left to one position after the last occurrence
            left = max(left, char_index[s[right]] + 1)
        
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len


def longest_substring_brute_force(s):
    """
    Baseline: O(n³) time, O(n) space
    """
    max_len = 0
    n = len(s)

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)

    return max_len


# Which to use?
# Primary: longest_substring_sliding_window (clearer logic)
# Alternative: longest_substring_with_indices (slightly faster in practice)
