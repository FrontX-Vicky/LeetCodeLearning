# Day 1: Arrays & Hash Maps - Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to the target.

**Constraint**: You cannot use the same element twice.

**Example**:
```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

---

## Core Concept

This problem teaches the fundamental principle of **trading space for time**.

### The Problem's Core Question
> "How can I quickly find a complement for each number?"

### Key Insight
Instead of checking every pair (slow), **store numbers you've seen and check if the complement exists** (fast).

---

## Common Patterns

1. **Brute Force**: Check all pairs (O(n²) time)
2. **Hash Map Lookup**: Store seen numbers, check for complement (O(n) time, O(n) space)
3. **Two Pointers**: Sort first, then converge (O(n log n) time, O(1) space - but loses original indices)

---

## Edge Cases to Consider

- **Duplicates in array**: `[3, 3]` with target 6 → should return [0, 1]
- **Negative numbers**: `[-1, 0, 1, 2]` with target 1 → should find the right pair
- **No solution exists**: Should return something meaningful (or handle gracefully)
- **Single pair only**: There's always exactly one solution (per LeetCode constraints)

---

## Time & Space Complexity

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n²) | O(1) | Check every pair; too slow for large inputs |
| Hash Map | O(n) | O(n) | Single pass + dictionary lookup; optimal |
| Two Pointers | O(n log n) | O(1) | Requires sorting; loses index order |

---

## How to Run & Test

```bash
# Run all test cases
python test_cases.py

# Run with verbose output
python test_cases.py -v
```

Check `test_cases.py` for sample and edge cases.

---

## Key Takeaways

1. **Hash maps are your friend** when you need fast lookups
2. **Complement searching** is a powerful pattern for "find pair" problems
3. **Trade-offs matter**: More space can mean less time
4. **Iteration over nested loops** whenever possible

---
