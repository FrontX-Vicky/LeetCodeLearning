# Day 2: Prefix Sums + Hash Maps - Subarray Sum Equals K

## Problem Statement
Given an integer array `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

**Example**:
```
Input: nums = [1, 1, 1], k = 2
Output: 2
Explanation: The subarrays [1,1] (indices 0-1) and [1,1] (indices 1-2) sum to 2.
```

--- 

## Core Concept
Use a running prefix sum and a hash map of prefix-sum frequencies to count how many previous prefixes would form a subarray summing to `k` with the current prefix.

### Key Insight
For each position `i`, we have `prefix[i] - prefix[j] = k` ⇒ we need to know how many `prefix[j]` equal `prefix[i] - k`. Counting those on the fly gives an O(n) solution.

---

## Common Patterns
1. **Brute Force**: Enumerate all subarrays and sum (O(n²) time, O(1) space)
2. **Prefix Sum + Hash Map (Optimal)**: One pass, maintain counts of seen prefix sums (O(n) time, O(n) space)
3. **Prefix Sum + Sorting (Not needed here)**: Sort prefix sums and use two pointers/binary search — slower (O(n log n)) and unnecessary.

---

## Edge Cases to Consider
- `k = 0` with zeros in the array
- Negative numbers (breaks sliding-window-only approaches; prefix sums still work)
- Single-element arrays
- Large arrays where O(n²) would time out

---

## Time & Space Complexity

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n²) | O(1) | Sum each subarray; educational baseline |
| Prefix Sum + Hash Map | O(n) | O(n) | Counts prefix frequencies; optimal |

---

## How to Run & Test
From repo root:
```bash
python 2026-01-02_prefix_sum_hash_map/main.py
python 2026-01-02_prefix_sum_hash_map/test_cases.py
```

---

## Key Takeaways
- Prefix sums turn subarray problems into prefix-difference checks.
- Hash maps let you count compatible prefixes in O(1) average time.
- Sliding window fails when negatives exist; prefix sums remain robust.
