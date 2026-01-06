# Main.py - Your Working File
# Task: Solve LeetCode #76: Minimum Window Substring
# Goal: Write 3 progressive approaches

# TODO 1: Approach 1 - Brute Force
# - Check all substrings, verify if they contain all chars from t
# - Time: O(n³), Space: O(m) where m = len(t)
# - Educational baseline only

def min_window_brute_force(s, t):
    """
    APPROACH 1: BRUTE FORCE
    """
    # YOUR CODE HERE
    pass


# TODO 2: Approach 2 - Sliding Window + Hash Maps (optimal)
# - Maintain freq map of required chars and current window chars
# - Expand right until window is valid, shrink left for minimum
# - Time: O(n + m), Space: O(m) where m = len(charset in t)
# - This is the standard interview solution

def min_window_sliding(s, t):
    """
    APPROACH 2: SLIDING WINDOW + HASH MAPS (OPTIMAL)
    """
    # YOUR CODE HERE
    pass


# TODO 3: Approach 3 - Sliding Window + Counter (pythonic variant)
# - Use Python's Counter from collections
# - Track how many unique chars from t are still needed
# - Time: O(n + m), Space: O(m)

def min_window_counter(s, t):
    """
    APPROACH 3: SLIDING WINDOW + COUNTER (PYTHONIC)
    """
    # YOUR CODE HERE
    pass


if __name__ == "__main__":
    # Smoke tests
    assert min_window_sliding("ADOBECODEBANC", "ABC") == "ADOBEC"
    assert min_window_sliding("a", "aa") == ""
    assert min_window_sliding("a", "a") == "a"
    assert min_window_sliding("ab", "b") == "b"
    assert min_window_sliding("", "a") == ""
    print("Quick checks passed. Run test_cases.py for more.")
