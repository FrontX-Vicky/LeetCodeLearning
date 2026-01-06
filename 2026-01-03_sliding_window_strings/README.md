# Day 3: Sliding Window - Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s`, find the length of the **longest substring** without repeating characters.

**Example**:
```
Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring without repeating characters.

Input: s = "bbbbb"
Output: 1
Explanation: "b"

Input: s = "pwwkew"
Output: 3
Explanation: "wke"
```

---

## Core Concept
Use a **sliding window** with two pointers (left and right) and a dictionary/set to track character positions or counts.

### Key Insight
When you encounter a duplicate:
1. Shrink the window from the left until the duplicate is removed
2. Update the max length as you expand the window
3. The window always contains unique characters

---

## Common Patterns
1. **Brute Force**: Check all substrings O(n³) time
2. **Two Pointers + Set/Dict (Optimal)**: One pass, maintain unique chars O(n) time, O(min(n, charset)) space
3. **Variant**: Track character indices instead of just a set

---

## Edge Cases to Consider
- Empty string
- Single character
- All unique characters
- All same character
- Special characters and spaces

---

## Time & Space Complexity

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n³) | O(1) | Check all substrings; very slow |
| Sliding Window + Set/Dict | O(n) | O(min(n, m)) | m = charset size; optimal |

---

## How to Run & Test
From repo root:
```bash
python 2026-01-03_sliding_window_strings/main.py
python 2026-01-03_sliding_window_strings/test_cases.py
```

---

## Key Takeaways
- **Sliding window** is ideal for "longest/shortest substring/subarray" with a constraint
- **Two pointers** allow O(n) time by avoiding redundant rechecks
- **Character tracking** (set or dict) prevents revisiting already-seen characters
