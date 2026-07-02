# Day 4: Advanced Sliding Window - Minimum Window Substring

## Problem Statement
Given two strings `s` and `t`, return the minimum window substring of `s` that contains all the characters in `t` (including duplicates).

If there is no such window, return an empty string.

**Example**:
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "ADOBEC"
Explanation: Minimum window is "ADOBEC" (length 6)

Input: s = "a", t = "aa"
Output: ""
Explanation: No valid window exists

Input: s = "a", t = "a"
Output: "a"
```

---

## Core Concept
Use a **sliding window with frequency maps** to find the shortest substring containing all required characters.

### Key Insight
1. Count required characters in `t`
2. Expand window right until all required chars are present
3. Shrink from left while maintaining validity
4. Track the minimum window seen

---

## Common Patterns
1. **Brute Force**: Check all substrings O(n³) time
2. **Sliding Window + Hash Maps (Optimal)**: One pass with freq tracking O(n + m) time, O(m) space
3. **Variant**: Use a counter to track how many unique chars still needed

---

## Edge Cases to Consider
- `t` longer than `s` → return ""
- `t` has duplicates → must match count, not just presence
- Empty strings
- `t` is longer than `s`
- All characters match immediately

---

## Time & Space Complexity

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n³) | O(1) | Very slow; educational only |
| Sliding Window + Maps | O(n + m) | O(m) | m = charset size; optimal |

---

## How to Run & Test
From repo root:
```bash
python 04_advanced_sliding_window/main.py
python 04_advanced_sliding_window/test_cases.py
```

---

## Key Takeaways
- **Frequency matching** requires tracking counts, not just presence
- **Two hash maps** compare required vs. current window state
- **Sliding window** combined with hashing is powerful for "find substring" problems
- **Early termination** makes brute force viable for small inputs but impractical at scale
