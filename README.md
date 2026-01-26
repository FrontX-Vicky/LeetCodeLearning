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

### Day 6: January 6, 2026 - Fast & Slow Pointers

**Main Problem**:
- [LeetCode #141: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

**Related Problems** (reinforcement):
- Day 5: Two pointers on arrays (contrast with linked lists)
- Floyd's Cycle Detection Algorithm
- Pointer manipulation in linear data structures

**Topics Covered**:
- Fast and slow pointer technique (Floyd's algorithm)
- Cycle detection in linked lists
- Space optimization (O(1) vs O(n) with hash set)
- Pointer speed differential

**Key Concepts Learned**:
- Fast pointer moves 2x speed, slow moves 1x
- If cycle exists, pointers eventually meet
- No cycle → fast reaches end (None)
- O(1) space vs O(n) with visited set

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Constant space cycle detection
- Mathematical proof of convergence

**Personal Notes**:
- Classic interview question demonstrating pointer manipulation
- Foundation for more complex linked list problems
- Fast/slow pattern appears in other algorithms (finding middle, detecting patterns)

### Day 7: January 7, 2026 - Stack (LIFO)

**Main Problem**:
- [LeetCode #20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

**Related Problems** (reinforcement):
- Day 6: Linear data structure traversal
- Stack vs queue comparison
- LIFO behavior in nested structures

**Topics Covered**:
- Stack data structure (LIFO - Last In First Out)
- Bracket matching algorithms
- Dictionary mapping for pairs
- Early return optimizations

**Key Concepts Learned**:
- Stack perfect for nested/paired structures
- Push opening brackets, pop on closing
- Use dictionary for clean pair mapping
- Check stack empty before pop operation
- Final state must be empty stack

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Odd-length early termination
- Dictionary vs direct comparison trade-offs
- Immediate return on first mismatch

**Personal Notes**:
- Stack is fundamental for DFS, expression evaluation, backtracking
- LIFO naturally handles nesting (last opened must close first)
- Will build on this for more complex stack problems

### Day 8: January 8, 2026 - Queue & BFS Fundamentals

**Main Problem**:
- [LeetCode #933: Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)

**Related Problems** (reinforcement):
- Day 7: Stack vs Queue comparison (LIFO vs FIFO)
- Sliding window with time constraints
- Queue operations and use cases

**Topics Covered**:
- Queue data structure (FIFO - First In First Out)
- Sliding time window with queue
- collections.deque for O(1) operations
- Request buffering and rate limiting

**Key Concepts Learned**:
- Queue for chronological/ordered processing
- deque.popleft() is O(1), list.pop(0) is O(n)
- Sliding window: remove old, add new
- Queue is foundation for BFS traversal

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Using deque instead of list for queue operations
- Amortized O(1) per operation
- Window boundary handling (inclusive ranges)

**Personal Notes**:
- Queue complements stack (FIFO vs LIFO)
- Essential for BFS which we'll use for graphs/trees
- Time-based sliding windows common in real systems
- Queue = "first come, first served" like real-world lines

### Day 9: January 9, 2026 - Monotonic Stack

**Main Problem**:
- [LeetCode #739: Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

**Related Problems** (reinforcement):
- Day 7: Regular stack operations (foundation)
- Day 8: FIFO vs LIFO patterns
- Next Greater/Smaller Element pattern

**Topics Covered**:
- Monotonic stack (maintains sorted order)
- Next Greater Element pattern
- Stack-based optimization from O(n²) to O(n)
- Monotonic decreasing vs increasing stacks

**Key Concepts Learned**:
- Monotonic stack = stack maintaining monotonic order
- Decreasing stack finds next greater element
- Increasing stack finds next smaller element
- Each element pushed/popped once → O(n) amortized
- Store indices, not values (to calculate distances)

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Breaking monotonic property triggers pops
- Amortized O(n) despite nested loops
- Template pattern for next greater/smaller problems

**Personal Notes**:
- Powerful optimization: O(n²) brute force → O(n) with monotonic stack
- Common interview pattern ("next warmer/greater/smaller")
- Builds directly on Day 7's stack foundation
- Will see this pattern again in histograms, stock spans

### Day 10: January 10, 2026 - Linked List Manipulation

**Main Problem**:
- [LeetCode #206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

**Related Problems** (reinforcement):
- Day 6: Fast/Slow pointers (pointer manipulation foundation)
- Linked list traversal and modification
- Iterative vs recursive pointer manipulation

**Topics Covered**:
- Singly linked list reversal
- Three-pointer iterative technique
- Recursive reversal with unwinding
- Stack-based reversal approach
- Pointer manipulation and state management

**Key Concepts Learned**:
- Three-pointer pattern: prev, curr, next
- Must save next before breaking link
- Iterative: O(1) space, O(n) time
- Recursive: O(n) space (call stack), O(n) time
- Return new head (was the tail)

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Saving next pointer before link reversal
- Iterative approach better than recursive in practice
- Edge case handling (empty, single node)

**Personal Notes**:
- Fundamental linked list operation for interviews
- Three-pointer technique appears in many problems
- Recursive approach more elegant but less efficient
- Stack-based approach educational but impractical
- Foundation for advanced linked list problems (LeetCode #92, #25, etc.)

### Day 11: January 11, 2026 - Binary Search (Basic)

**Main Problem**:
- [LeetCode #704: Binary Search](https://leetcode.com/problems/binary-search/)

**Related Problems** (reinforcement):
- Foundation for binary search variations
- Day 5: Two pointers (similar narrowing concept)
- Search in sorted arrays/lists

**Topics Covered**:
- Classic binary search template
- Iterative vs recursive implementation
- Safe mid calculation (overflow prevention)
- Divide and conquer paradigm
- O(log n) time complexity

**Key Concepts Learned**:
- Binary search on sorted arrays only
- Condition: `left <= right` (not just `<`)
- Update: `left = mid + 1`, `right = mid - 1`
- Safe mid: `left + (right - left) // 2`
- Each iteration halves search space → log n steps

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Halving search space each iteration
- O(log n) incredibly efficient (1M → 20 steps)
- Safe mid calculation prevents overflow in other languages
- Template applies to many search problems

**Personal Notes**:
- Master this template - appears in 100+ LeetCode problems
- "Sorted" keyword = think binary search
- Foundation for binary search variations (rotated arrays, search range, etc.)
- Log time complexity is game-changing for large datasets

### Day 12: January 12, 2026 - Binary Search Variations

**Main Problem**:
- [LeetCode #34: Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

**Related Problems** (reinforcement):
- Day 11: Basic binary search (foundation)
- Modified binary search for boundary finding
- Range queries in sorted arrays

**Topics Covered**:
- Modified binary search (find leftmost/rightmost)
- Boundary finding in duplicates
- Python's bisect module
- Two binary searches vs linear expansion
- Template variations for first/last occurrence

**Key Concepts Learned**:
- Don't stop when found - continue searching for boundaries
- Leftmost: when found, search left (`right = mid - 1`)
- Rightmost: when found, search right (`left = mid + 1`)
- Need `result` variable to track last valid index
- `bisect_left` = first occurrence, `bisect_right - 1` = last

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Continuing search after finding maintains O(log n)
- Linear expansion is O(n) worst case (all elements match)
- Two independent binary searches better than one + expansion
- Save position while searching for better boundary

**Personal Notes**:
- Critical variation: "find first" vs "find any"
- Appears in range queries, duplicate handling
- Template: save result, continue searching in direction
- Bisect elegant but implement manually in interviews
- Foundation for insert position, count occurrences

### Day 13: January 13, 2026 - Recursion Fundamentals

**Main Problem**:
- [LeetCode #509: Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

**Bonus Problem**:
- Factorial calculation (classic recursion example)

**Related Problems** (reinforcement):
- Day 10: Recursive linked list reversal (applied recursion)
- Day 11: Recursive binary search
- Foundation for trees, backtracking, divide & conquer

**Topics Covered**:
- Pure recursion (naive approach)
- Memoization (Top-Down Dynamic Programming)
- Bottom-Up Dynamic Programming with array
- Space-optimized iteration (O(1) space)
- Base cases and recursive cases
- Performance comparison (O(2^n) → O(n) → O(1) space)

**Key Concepts Learned**:
- Every recursion needs base case + recursive case
- Memoization prevents redundant computation
- Overlapping subproblems = DP candidate
- Bottom-up builds solution iteratively
- Space optimization: only track what you need
- Evolution: Recursion → Memo → DP → Optimized

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Cache results to transform O(2^n) to O(n)
- Only store last 2 values instead of full array
- Iteration faster than recursion (no stack overhead)
- Recognize when problem has optimal substructure

**Personal Notes**:
- Fibonacci: classic intro to recursion and DP
- Pure recursion = intuitive but exponentially slow
- Memoization = game changer for overlapping subproblems
- Foundation for tree traversal, backtracking, DP problems
- Always ask: "What's simplest case?" (base case first!)

---

### **Day 14: Binary Tree Basics** 📅 *2026-01-14*

**Main Problem**:
- Binary Tree Traversals: Preorder, Inorder, Postorder
- Both recursive and iterative implementations

**Topics Covered**:
- Binary tree structure (nodes, left/right children)
- Preorder traversal (Root → Left → Right)
- Inorder traversal (Left → Root → Right)
- Postorder traversal (Left → Right → Root)
- Recursive vs iterative tree traversal
- Stack-based iteration simulation

**Key Concepts Learned**:
- Preorder = process root before children (useful for copying trees)
- Inorder = processes nodes in sorted order for BST
- Postorder = process root after children (useful for deleting trees)
- Recursive traversal = natural and elegant
- Iterative traversal = uses explicit stack to simulate recursion
- Each traversal type has unique applications

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Recursive: O(h) space for call stack, simple to implement
- Iterative: O(h) space for explicit stack, more control
- Both have O(n) time complexity
- Choose recursion for clarity, iteration for control

**Personal Notes**:
- Foundation for all tree problems
- Inorder traversal = sorted output for BST (critical!)
- Stack mimics call stack in iterative version
- Understanding traversals = understanding tree recursion

---

### **Day 15: Binary Search Trees** 📅 *2026-01-15*

**Main Problems**:
- Search in BST (recursive & iterative)
- Insert into BST (recursive & iterative)
- Validate BST
- Find Min/Max in BST
- Kth Smallest Element in BST

**Topics Covered**:
- BST property: Left < Root < Right
- BST search (O(log n) average)
- BST insertion while maintaining properties
- Range validation for BST
- Inorder traversal = sorted order
- Min = leftmost node, Max = rightmost node

**Key Concepts Learned**:
- BST enables binary search on trees
- Can't validate BST with local checks only - need range tracking
- Inorder traversal critical for BST problems
- Iterative versions use O(1) space vs O(h) recursive
- Min/max are trivial in BST (just go left/right!)
- Kth smallest = inorder traversal + counter

**Mistakes Made**:
- *To be filled in after attempting*

**Optimization Techniques Discovered**:
- Iterative search/insert saves stack space
- Early stopping in kth smallest (stop at k, not n)
- Range validation prevents redundant checks
- BST property makes many operations O(log n) instead of O(n)

**Personal Notes**:
- BST = binary search + tree structure
- Inorder traversal is the key to most BST problems
- Always think about range constraints for validation
- Height determines efficiency: balanced = O(log n), skewed = O(n)

---

## Master Concepts Index
- **Hash Maps**: Day 1, Day 2, Day 3, Day 4
- **Arrays**: Day 1, Day 2, Day 5
- **Prefix Sums**: Day 2
- **Sliding Window**: Day 3, Day 4, Day 8
- **Strings**: Day 3, Day 4
- **Frequency Counting**: Day 4
- **Two Pointers**: Day 5
- **Greedy Algorithms**: Day 5
- **Fast/Slow Pointers**: Day 6
- **Linked Lists**: Day 6, Day 10
- **Stack (LIFO)**: Day 7
- **Queue (FIFO)**: Day 8
- **BFS Foundation**: Day 8
- **Monotonic Stack**: Day 9
- **Next Greater Element Pattern**: Day 9
- **Linked List Reversal**: Day 10
- **Pointer Manipulation**: Day 6, Day 10
- **Recursion vs Iteration**: Day 10, Day 13
- **Binary Search**: Day 11, Day 12
- **Divide & Conquer**: Day 11
- **Binary Search Variations**: Day 12
- **Boundary Finding**: Day 12
- **Recursion Fundamentals**: Day 13
- **Memoization**: Day 13
- **Dynamic Programming**: Day 13
- **Space Optimization**: Day 13
- **Binary Trees**: Day 14
- **Tree Traversals**: Day 14
- **Preorder/Inorder/Postorder**: Day 14
- **Binary Search Trees**: Day 15
- **BST Operations**: Day 15
- **Range Validation**: Day 15
- **Inorder = Sorted**: Day 14, Day 15

---

## Upcoming Topics Roadmap

**Phase 1: Fundamentals** (Days 1-8) ✅ Complete
- Arrays, Hash Maps, Sliding Window, Two Pointers, Stack, Queue

**Phase 2: Advanced Patterns** (Days 9-12) ✅ Complete
- Day 9: Monotonic Stack ✅
- Day 10: Linked List Manipulation ✅
- Day 11: Binary Search (Basic) ✅
- Day 12: Binary Search Variations ✅

**Phase 3: Recursion & Trees** (Days 13-16) 🔄 In Progress
- Day 13: Recursion Fundamentals ✅
- Day 14: Binary Tree Basics ✅
- Day 15: Binary Search Trees (ready)
- Day 16: Tree DFS/BFS (ready)

**Phase 4: Advanced** (Days 17-20)
- Day 17: Heap/Priority Queue
- Day 18: Graphs (BFS)
- Day 19: Dynamic Programming Intro
- Day 20: Advanced DP

---
