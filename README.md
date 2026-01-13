# LeetCode Python Journey - Master Learning Tracker

**Goal**: Master problem-solving in Python through consistent daily practice with deep conceptual understanding and progressive optimization.

**Started**: January 1, 2026

---

## Day-by-Day Progress

### Day 1: January 1, 2026 - Arrays & Hash Maps Fundamentals

**Main Problem**:
- [LeetCode #1: Two Sum](https://leetcode.com/problems/two-sum/)

**Related Problems** (for future reinforcement):
- *N/A - First day*

**Topics Covered**:
- Hash Maps / Dictionaries in Python
- Trade-off between time and space complexity
- Two-pointer and lookup optimization
- Common pitfalls with duplicates and edge cases

**Key Concepts Learned**:
- Using dictionaries for O(1) lookups
- Why brute force O(n²) fails at scale
- Space-time complexity trade-offs

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- *To be filled in after coding*

**Personal Notes**:
- Starting with the classic "Two Sum" problem because it teaches hash maps, which are fundamental to many algorithms
- Will use this as a foundation for future array/dictionary problems

### Day 2: January 2, 2026 - Prefix Sums + Hash Maps

**Main Problem**:
- [LeetCode #560: Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

**Related Problems** (reinforcement from previous day):
- Re-run Day 1: Two Sum (hash map focus)
- Two Sum with negatives and zeros (practice edge handling)
- Two Sum brute-force vs hash map (complexity contrast)

**Topics Covered**:
- Prefix sums for subarray queries
- Hash map frequency counting of prefixes
- Handling negatives (why sliding window fails here)

**Key Concepts Learned**:
- For each prefix `p`, subarrays ending here with sum `k` equal count of `p - k`
- Initialize prefix frequency with `{0:1}` to count subarrays starting at index 0
- Time/space trade-offs between brute force O(n²) and prefix-hash O(n)

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Prefix-sum counting in one pass with a hash map

**Personal Notes**:
- Sliding window is not reliable when negatives exist; prefix sums remain stable

### Day 3: January 3, 2026 - Sliding Window Fundamentals

**Main Problem**:
- [LeetCode #3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

**Related Problems** (reinforcement):
- Day 1: Two Sum with sliding window context (when sliding window doesn't apply)
- Day 2: Prefix sums vs. sliding window trade-offs
- Compare brute force O(n³) vs. optimal sliding window O(n)

**Topics Covered**:
- Two-pointer sliding window technique
- Set-based uniqueness checking
- Character index tracking with dictionaries
- When to use sliding window vs. prefix sums

**Key Concepts Learned**:
- Sliding window collapses search space from O(n²) to O(n)
- "Expand right, shrink left" pattern for maintaining constraints
- Character tracking prevents duplicate processing

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Direct index jumping vs. incremental pointer movement

**Personal Notes**:
- Sliding window requires constraint satisfaction (no duplicates, valid window, etc.)
- Works best with "longest/shortest substring/subarray" problems

### Day 4: January 4, 2026 - Advanced Sliding Window

**Main Problem**:
- [LeetCode #76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

**Related Problems** (reinforcement):
- Day 3: Longest Substring (simpler sliding window, unique chars only)
- Contrast: find longest unique vs. find shortest with duplicates allowed
- Frequency matching patterns

**Topics Covered**:
- Multi-constraint sliding window (not just presence, but counts)
- Dual hash maps (required vs. current window)
- Shrinking from left for minimum length
- Character frequency validation

**Key Concepts Learned**:
- Track "formed" counter for progress toward solution
- Frequency-based validation instead of set membership
- Early termination via while loop for minimum window
- Time complexity O(n + m) vs. O(n³) brute force

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Using Counter object for cleaner frequency tracking
- Tuple packing for result (length, start, end) to avoid repeated comparisons

**Personal Notes**:
- This is interview-level hard; combines everything from Days 1-3
- Frequency matching is a common pattern across many problems
- Window validity can be complex; must track multiple conditions

### Day 5: January 5, 2026 - Two Pointers Optimization

**Main Problem**:
- [LeetCode #11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

**Related Problems** (reinforcement):
- Day 3 & 4: Sliding window (expansion/contraction patterns)
- Two Sum variants with sorted arrays
- Contrasting: sliding window vs. two pointers (different constraints)

**Topics Covered**:
- Two-pointer technique (start from ends)
- Greedy algorithm strategy
- Area/geometry calculations
- Monotonic property exploitation

**Key Concepts Learned**:
- Why moving the shorter side is greedy-optimal
- Two pointers approach differs from sliding window (no constraint to maintain)
- Width always decreases, height must compensate
- Early termination optimization for large inputs

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Pruning with max possible area remaining
- Greedy choice correctness proof

**Personal Notes**:
- Two pointers is a distinct technique from sliding window
- Greedy proofs are important for understanding correctness
- Geometry + algorithm design (area calculation)

---

## Master Concepts Index
- **Hash Maps**: Day 1, Day 2, Day 3, Day 4
- **Arrays**: Day 1, Day 2, Day 5
- **Prefix Sums**: Day 2
- **Sliding Window**: Day 3, Day 4
- **Strings**: Day 3, Day 4
- **Frequency Counting**: Day 4
- **Two Pointers**: Day 5
- **Greedy Algorithms**: Day 5
- Sliding Window
- Linked Lists
- Trees & Recursion
- Dynamic Programming
- Graphs

---
