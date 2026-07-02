# solutions.py - Reference solutions

from collections import Counter


def min_window_sliding(s, t):
    """
    Optimal: Sliding Window + Hash Maps
    Time: O(n + m), Space: O(m)
    """
    if not s or not t:
        return ""
    
    # Count required characters
    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1
    
    required = len(dict_t)  # Unique chars needed
    formed = 0  # Unique chars with correct frequency in window
    
    window_counts = {}
    left = 0
    ans = float("inf"), None, None  # (length, left, right)
    
    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # If this char's count matches, we've formed one more required char
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        
        # Shrink window while it's valid
        while left <= right and formed == required:
            char = s[left]
            
            # Update result if this window is smaller
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            # Remove from left and update formed count
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            
            left += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


def min_window_counter(s, t):
    """
    Variant: Using Python's Counter
    Time: O(n + m), Space: O(m)
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
        window_counts[char] = window_counts.get(char, 0) + 1
        
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        
        while left <= right and formed == required:
            char = s[left]
            
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            
            left += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


def min_window_brute_force(s, t):
    """
    Baseline: O(n³) time, O(m) space
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
            
            # Check if window contains all required chars
            if all(window_counts.get(c, 0) >= dict_t[c] for c in dict_t):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    min_start = i
                break
    
    return "" if min_len == float("inf") else s[min_start:min_start + min_len]


# Which to use?
# Primary: min_window_sliding (clearest logic)
# Alternative: min_window_counter (more Pythonic)
