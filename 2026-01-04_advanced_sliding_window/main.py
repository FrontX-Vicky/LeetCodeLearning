# Main.py - Your Working File
# Task: Solve LeetCode #76: Minimum Window Substring
# Goal: Write 3 progressive approaches

# TODO 1: Approach 1 - Brute Force
# - Check all substrings, verify if they contain all chars from t
# - Time: O(n³), Space: O(m) where m = len(t)
# - Educational baseline only

from collections import Counter


def min_window_brute_force(s, t):
    """
    APPROACH 1: BRUTE FORCE
    """
    if not s or not t:
        return ""

    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1

    min_len = float("inf")
    min_start = 0

    for i in range(len(s)):
        window_counts = {}
        for j in range(i, len(s)):
            char = s[j]
            window_counts[char] = window_counts.get(char, 0) + 1

            if all(window_counts.get(c, 0) >= dict_t[c] for c in dict_t):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    min_start = i
                break
    return "" if min_len == float("inf") else s[min_start:min_start + min_len]

# TODO 2: Approach 2 - Sliding Window + Hash Maps (optimal)
# - Maintain freq map of required chars and current window chars
# - Expand right until window is valid, shrink left for minimum
# - Time: O(n + m), Space: O(m) where m = len(charset in t)
# - This is the standard interview solution

def min_window_sliding(s, t):
    """
    APPROACH 2: SLIDING WINDOW + HASH MAPS (OPTIMAL)
    """
    if not s and not t:
        return ""
    
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1

    print("dict_t:", dict_t)
    required = len(dict_t)
    print("required:", required)
    formed = 0

    window_counts = {}
    left = 0
    ans = float("inf"), None, None
    print("Initial ans:", ans)

    for right in range(len(s)):
        print("Right pointer at:", right)
        char = s[right]
        print("Right char:", char)
        window_counts[char] = window_counts.get(char, 0) + 1
        print("Window counts:", window_counts)

        if char in dict_t and window_counts[char] == dict_t[char]:
            print(char, "in", dict_t,  "and", window_counts[char], "==", dict_t[char])
            formed += 1
            print("Increased formed for char:", char)
            print(formed)

        
        while left <= right and formed == required:
            print("formed == required:", formed, "==", required)
            char = s[left]
            print("Left char:", char)
            print(right ,"-", left + 1, "<", ans[0])

            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
                print("Updating ans:", (right - left + 1, left, right))
                print(ans)


            window_counts[char] -= 1
            print("Window after right =", right, ":", s[left:right+1])
            if char in dict_t and window_counts[char] < dict_t[char]:
                print("Decreasing formed for char:", char)
                formed -= 1
        
            left += 1
            print("--while--")
            print("")
        print("--for--")
        print("")
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


# TODO 3: Approach 3 - Sliding Window + Counter (pythonic variant)
# - Use Python's Counter from collections
# - Track how many unique chars from t are still needed
# - Time: O(n + m), Space: O(m)

def min_window_counter(s, t):
    """
    APPROACH 3: SLIDING WINDOW + COUNTER (PYTHONIC)
    """
    if not s or not t:
        return ""
    
    dict_t = Counter(t)
    window_counts = {}
    required = len(dict_t)
    formed = 0

    left = 0
    ans = float("inf"), None, None

    for right in range(len(s)):
        char = s[right]
        # print("Right char:", char)
        
        window_counts[char] = window_counts.get(char, 0) + 1
        # print("Window counts:", window_counts)


        if char in dict_t and window_counts[char] == dict_t[char]:
            # print(char, "in", dict_t,  "and", window_counts[char], "==", dict_t[char])
            formed += 1
            # print("Increased formed for char:", char)
            # print(formed)

        # print(char in dict_t and window_counts[char] == dict_t[char] )
        # continue
        while left <= right and formed == required:
            # print("formed == required:", formed, "==", required)
            char = s[left]
            # print("Left char:", char)
            # print(right ,"-", left + 1, "<", ans[0])
            if right - left + 1 < ans[0]:
                # print("Updating ans:", (right - left + 1, left, right))
                ans = (right - left + 1, left, right)

            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                # print("Decreasing formed for char:", char)
                formed -= 1

            # print("Window after right =", right, ":", s[left:right+1])
            # print("----")
            left += 1
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

if __name__ == "__main__":
    # Smoke tests
    # print(min_window_counter("ADOBECODEBANC", "ABC"))
    assert min_window_sliding("ADOBECODEBANC", "ABC") == "BANC"
    # assert min_window_counter("ADOBECODEBANC", "ABC") == "ADOBEC"
    # assert min_window_counter("a", "aa") == ""
    # assert min_window_counter("a", "a") == "a"
    # assert min_window_counter("ab", "b") == "b"
    # assert min_window_counter("", "a") == ""
    # assert min_window_brute_force("ADOBECODEBANC", "ABC") == "ADOBEC"
    # assert min_window_brute_force("a", "aa") == ""
    # assert min_window_brute_force("a", "a") == "a"
    # assert min_window_brute_force("ab", "b") == "b"
    # assert min_window_brute_force("", "a") == ""
    # assert min_window_sliding("ADOBECODEBANC", "ABC") == "ADOBEC"
    # assert min_window_sliding("a", "aa") == ""
    # assert min_window_sliding("a", "a") == "a"
    # assert min_window_sliding("ab", "b") == "b"
    # assert min_window_sliding("", "a") == ""
    print("Quick checks passed. Run test_cases.py for more.")
