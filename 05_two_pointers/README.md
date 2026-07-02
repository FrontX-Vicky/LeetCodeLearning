# Day 5: Two Pointers - Container With Most Water

## Problem Statement
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container such that the container holds the most water.

**Return the maximum area of water a container can store.**

**Example**:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines at indices 1 and 8 (height 8 and 7) 
form a container with width 7 and height min(8,7) = 7.
Area = width × height = 7 × 7 = 49

Input: height = [1,1]
Output: 1
```

---

## Core Concept
Use **two pointers** starting from both ends and move inward, always shrinking the side with the smaller height. This greedy approach guarantees finding the maximum.

### Key Insight
- Area = width × min(height[left], height[right])
- Width decreases as we move pointers closer
- Height can only increase (or stay same) by shrinking the smaller side
- Therefore, moving the taller side cannot yield a larger area

---

## Common Patterns
1. **Brute Force**: Check all pairs of indices O(n²) time
2. **Two Pointers (Optimal)**: Start at both ends, shrink inward O(n) time
3. **Greedy Strategy**: Move the shorter height pointer inward

---

## Edge Cases to Consider
- Same height for both pointers
- All same heights
- Very small array (length 2)
- Decreasing heights from left to right
- Increasing heights from left to right

---

## Time & Space Complexity

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n²) | O(1) | Check all pairs |
| Two Pointers | O(n) | O(1) | Single pass, optimal |

---

## How to Run & Test
From repo root:
```bash
python 05_two_pointers/main.py
python 05_two_pointers/test_cases.py
```

---

## Key Takeaways
- **Two pointers** are not just for sorted arrays
- **Greedy approach** can optimize when problem has monotonic properties
- **Area calculation** depends on both width AND height constraints
- **Early termination possible** when width becomes negligible
