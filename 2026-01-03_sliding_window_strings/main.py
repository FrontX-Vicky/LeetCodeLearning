# Main.py - Your Working File
# Task: Solve LeetCode #3: Longest Substring Without Repeating Characters
# Goal: Write 3 progressive approaches

# TODO 1: Approach 1 - Brute Force
# - Check all substrings and verify no duplicates
# - Time: O(n³), Space: O(1)
# - Use as baseline for understanding

def longest_substring_brute_force(s):
    """
    APPROACH 1: BRUTE FORCE
    """
    max_len = 0
    n = len(s)

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i +1)

    return max_len          

# TODO 2: Approach 2 - Sliding Window + Set (optimal)
# - Maintain a window with a set of unique characters
# - Expand right, shrink left when duplicate found
# - Time: O(n), Space: O(min(n, charset_size))
# - This is the standard interview solution

def longest_substring_sliding_window(s):
    """
    APPROACH 2: SLIDING WINDOW + SET (OPTIMAL)
    """
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

# TODO 3: Approach 3 - Sliding Window + Dict (tracks indices)
# - Store character -> last seen index
# - Jump left pointer directly to duplicate's position + 1
# - Time: O(n), Space: O(min(n, charset_size))

def longest_substring_with_indices(s):
    """
    APPROACH 3: SLIDING WINDOW + DICT (INDEX TRACKING)
    """
    char_index = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)

        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len

if __name__ == "__main__":
    # Smoke tests

    # assert longest_substring_brute_force("abcabcbb") == 3
    # assert longest_substring_with_indices("pwwkew") == 3
    # assert longest_substring_brute_force("dvdf") == 3   
    # assert longest_substring_brute_force("bbbbb") == 1
    # assert longest_substring_brute_force("") == 0
    # assert longest_substring_brute_force("au") == 2

    assert longest_substring_sliding_window("abcabcbb") == 3
    assert longest_substring_sliding_window("bbbbb") == 1
    assert longest_substring_sliding_window("pwwkew") == 3
    assert longest_substring_sliding_window("") == 0
    assert longest_substring_sliding_window("au") == 2
    print("Quick checks passed. Run test_cases.py for more.")
