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
    # YOUR CODE HERE
    pass


# TODO 2: Approach 2 - Sliding Window + Set (optimal)
# - Maintain a window with a set of unique characters
# - Expand right, shrink left when duplicate found
# - Time: O(n), Space: O(min(n, charset_size))
# - This is the standard interview solution

def longest_substring_sliding_window(s):
    """
    APPROACH 2: SLIDING WINDOW + SET (OPTIMAL)
    """
    # YOUR CODE HERE
    pass


# TODO 3: Approach 3 - Sliding Window + Dict (tracks indices)
# - Store character -> last seen index
# - Jump left pointer directly to duplicate's position + 1
# - Time: O(n), Space: O(min(n, charset_size))

def longest_substring_with_indices(s):
    """
    APPROACH 3: SLIDING WINDOW + DICT (INDEX TRACKING)
    """
    # YOUR CODE HERE
    pass


if __name__ == "__main__":
    # Smoke tests
    assert longest_substring_sliding_window("abcabcbb") == 3
    assert longest_substring_sliding_window("bbbbb") == 1
    assert longest_substring_sliding_window("pwwkew") == 3
    assert longest_substring_sliding_window("") == 0
    assert longest_substring_sliding_window("au") == 2
    print("Quick checks passed. Run test_cases.py for more.")
