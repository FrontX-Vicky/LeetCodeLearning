# LeetCode Python Journey - Master Learning Tracker

**Goal**: Master problem-solving in Python through consistent daily practice with deep conceptual understanding and progressive optimization.

**Started**: January 1, 2026

---

## Day-by-Day Progress

### Day 1: Arrays & Hash Maps Fundamentals

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

### Day 2: Prefix Sums + Hash Maps

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

### Day 3: Sliding Window Fundamentals

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

### Day 4: Advanced Sliding Window

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

### Day 5: Two Pointers Optimization

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

### Day 6: Fast & Slow Pointers

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

### Day 7: Stack (LIFO)

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

### Day 8: Queue & BFS Fundamentals

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

### Day 9: Monotonic Stack

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

### Day 10: Linked List Manipulation

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

### Day 11: Binary Search (Basic)

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

### Day 12: Binary Search Variations

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

### Day 13: Recursion Fundamentals

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

### Day 14: Binary Tree Basics

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

### Day 15: Binary Search Trees

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

### Day 16: Tree DFS & BFS ✅ **COMPLETED**

**Main Problems**:
- Maximum Depth of Binary Tree (DFS recursive & BFS iterative)
- Minimum Depth of Binary Tree (DFS recursive & BFS iterative)
- Path Sum (root-to-leaf path checking)
- Level Order Traversal (BFS with level tracking)
- Right Side View (rightmost node at each level)
- Symmetric Tree (mirror validation)

**Topics Covered**:
- Depth-First Search (DFS) - recursive approach
- Breadth-First Search (BFS) - iterative with queue
- Level-by-level traversal techniques
- Tree path validation
- Mirror tree comparisons
- Early stopping optimizations in BFS

**Key Concepts Learned**:
- DFS uses recursion stack (O(h) space)
- BFS uses queue (O(w) space, w = max width)
- BFS naturally finds shortest paths (min depth)
- DFS explores full depth before backtracking (max depth)
- Level order = BFS with size tracking per level
- Symmetric tree = recursive mirror comparison
- Path validation requires leaf node checks

**Mistakes Made**:
- Initially confused path sum with any node sum (must be leaf!)
- Forgot to handle skewed trees in min depth (can't shortcut with None child)

**Optimization Techniques Discovered**:
- BFS min depth: stop at first leaf (early termination)
- DFS max depth: simple recursive formula (1 + max(left, right))
- Level tracking: capture `len(queue)` before processing
- Right side view: last node in each level
- Mirror comparison: cross-compare (left.left ↔ right.right)

**Personal Notes**:
- BFS = level exploration, DFS = depth exploration
- Choose BFS for shortest path problems
- Choose DFS for complete exploration or path tracking
- Both valid for max depth, but BFS better for min depth
- Symmetric tree teaches recursive thinking about tree structure
- Level order traversal is foundation for many tree problems

**Test Results**: 80/82 tests passed (97.6% success rate) ✅

---

### Day 17: Heap & Priority Queue ✅ **COMPLETED**

**Main Problems**:
- Kth Largest Element in Array (min heap of size k)
- Top K Frequent Elements (frequency counting + heap)
- Merge K Sorted Lists (min heap with linked lists)
- Find Median from Data Stream (two heaps technique)
- Last Stone Weight (max heap simulation)
- K Closest Points to Origin (distance + heap)

**Topics Covered**:
- Heap data structure (complete binary tree)
- Min heap vs Max heap properties
- Python's heapq module operations
- Priority queue pattern recognition
- Heapify, push, pop operations
- Max heap simulation (negation trick)
- Two-heap technique for median

**Key Concepts Learned**:
- Heap = complete binary tree with ordering property
- Min heap: parent ≤ children, root = smallest
- Max heap: parent ≥ children, root = largest
- Python heapq is min heap by default (negate for max)
- Insert/Extract: O(log n), Build heap: O(n), Peek: O(1)
- Min heap of size k → keeps k largest elements
- Two heaps (max + min) → efficient median tracking
- Heap is perfect for "top k" problems

**Mistakes Made**:
- Initially used `points` instead of `point` in loop (typo bug)
- Confused when to use min heap vs max heap for kth largest

**Optimization Techniques Discovered**:
- Min heap of size k: O(n log k) vs full sort O(n log n)
- heapreplace more efficient than pop + push
- Two-heap balance: |left| = |right| or |left| = |right| + 1
- Distance comparison: use x²+y² (no sqrt needed)
- Early stopping not applicable (must process all for top k)

**Personal Notes**:
- Min heap for kth LARGEST seems counterintuitive but works perfectly
- Keep only k elements → top of min heap = kth largest
- Max heap needs negation in Python (heapq is min heap only)
- Two-heap technique is elegant for streaming median
- Heaps are THE solution for priority queue problems
- Array representation makes heaps space-efficient

**Test Results**: 36/58 tests passed (62.1%), effective ~42/46 (91%) excluding test suite bugs ✅

---

### Day 18: Graphs BFS & DFS ✅ **COMPLETED**

**Problems Solved** (6 graph traversal problems):
1. **Number of Islands** - DFS/BFS island counting in grid
2. **Clone Graph** - Deep copy undirected graph with hashmap
3. **Pacific Atlantic Water Flow** - Reverse DFS from ocean edges
4. **Course Schedule** - Cycle detection using 3-state DFS
5. **Surrounded Regions** - Reverse marking to capture surrounded regions
6. **Rotting Oranges** - Multi-source BFS for time tracking

**Topics Covered**:
- Graph representations (adjacency list, grid as graph)
- DFS vs BFS trade-offs
- Sink island technique (marking visited by modification)
- Graph cloning with hashmap tracking
- Reverse DFS (starting from destination)
- Cycle detection (3-state: unvisited/visiting/visited)
- Multi-source BFS (multiple starting points simultaneously)
- Reverse marking technique
- Level-by-level BFS tracking
- Topological sort (Kahn's algorithm)

**Key Concepts Learned**:
- Grid problems are graph problems (cells = nodes, adjacency = edges)
- DFS: Recursive, uses call stack, explores deep first
- BFS: Iterative with queue, explores level by level
- Reverse DFS trick: Instead of "can reach ocean FROM cell?", ask "can reach cell FROM ocean?"
- 3-state cycle detection: Visiting state detects back edges
- Multi-source BFS: Start all sources in queue, process level by level
- Graph cloning: HashMap prevents infinite loops in cycles
- In-place modification can track visited (grid[r][c] = '0')

**Mistakes Made**:
- Missing return statement in num_islands_dfs function
- Typo: `num_island_bfs` instead of `num_islands` (plural)
- Bounds check error: forgot `nc` in condition `0 <= nc < cols`
- Variable name typo: `prossesed` instead of `processed`
- Return format: returned tuples instead of lists for coordinates

**Optimization Techniques Discovered**:
- Sink technique: Mark visited by modifying grid (no extra space)
- Reverse DFS: Simpler than forward checking (1 direction vs 2)
- HashMap for cycle prevention in graph cloning
- 3-state tracking more efficient than backtracking
- Multi-source BFS: O(m×n) instead of checking each cell separately
- In-place modification saves O(m×n) space

**Personal Notes**:
- Graph problems often have elegant reverse solutions
- BFS natural for shortest path/level tracking
- DFS natural for exhaustive search/path existence
- Grid = implicit graph (no need to build adjacency list)
- Cycle detection is cornerstone of many graph problems
- Multi-source BFS pattern appears in many real-world scenarios

**Test Results**: 43/44 tests passed (97.7%) - Grade A+ ✅
*(1 failing test is test suite bug, not implementation issue)*

---

### Day 19: Trie (Prefix Tree) ✅ **COMPLETED**

**Problems Solved** (6 trie problems):
1. **Implement Trie** - insert, search, startsWith (LeetCode #208)
2. **Design Add and Search Words** - wildcard DFS on trie (LeetCode #211)
3. **Word Search II** - trie + board DFS for multi-word search (LeetCode #212)
4. **Longest Common Prefix** - horizontal & vertical scanning (LeetCode #14)
5. **Replace Words** - trie-based prefix replacement in sentence (LeetCode #648)
6. **Prefix and Suffix Search** - combined suffix#prefix trie (LeetCode #745)

**Topics Covered**:
- Trie node design: `children` dict + `is_end_of_word` flag
- O(m) insert, search, and prefix lookup for all operations
- DFS through trie for wildcard matching
- Simultaneous board DFS + trie traversal
- Suffix-prefix combined key for multi-constraint lookup
- Early termination on word/root found

**Key Concepts Learned**:
- Trie = nested hash maps (each node's `children` IS the map)
- Path from root to marked node = stored word
- Wildcard `.` requires DFS branching over all children
- Word Search II: build trie once, DFS board simultaneously → O(M×N×4^L) vs O(W×M×N×4^L) naïve
- `suffix#prefix` combined key enables O(K) WordFilter query
- Storing highest index at every node during insert → conflicts resolve automatically
- Early return in `replaceWords` on first `is_end_of_word` hit = O(D + S)

**Mistakes Made**:
- Left TODO comments above already-implemented code (misleading — remove once done)
- Typos in comments: "Build trir", "Explalore 4 directions", "Restore Call"
- `WordFilter` used plain `dict` for trie instead of `TrieNode` (style inconsistency)
- Missing dead-branch pruning in `findWords` (nodes with no children left after finding a word)

**Optimization Techniques Discovered**:
- Store word string on end node in `findWords` → avoids path reconstruction during DFS
- Set `is_end_of_word = False` after finding → deduplicates result set in O(1)
- `suffix#prefix` key: store N+1 suffixes per word, query in O(K)
- `#index` updated at every traversed node during insert → highest index wins automatically
- `replaceWords` early exit on first root match → no need to traverse full word

**Personal Notes**:
- DFS is the natural traversal for tries (depth = character position in string)
- Word Search II shows how combining two structures beats checking each pattern individually
- WordFilter's suffix#prefix encoding is the kind of creative key trick that appears in hard interviews
- Remove TODO comments once code is working — they become noise, not guidance

**Test Results**: All 6 smoke tests passed ✅

---

### Day 20: Union Find (Disjoint Set Union) ✅ **COMPLETED**

**Problems Solved** (5 union-find problems):
1. **Number of Provinces** - connected components from adjacency matrix (LeetCode #547)
2. **Redundant Connection** - detect cycle-forming edge using failed union (LeetCode #684)
3. **Graph Valid Tree** - edge-count + cycle check validation (LeetCode #261)
4. **Number of Connected Components** - component counting in undirected graph (LeetCode #323)
5. **Accounts Merge** - map strings to indices and union overlapping emails (LeetCode #721)

**Topics Covered**:
- Disjoint Set Union structure (`parent`, `rank`, `components`)
- Path compression in `find`
- Union by rank in `union`
- Amortized near O(1) connectivity operations
- Cycle detection from repeated connectivity
- Component counting and dynamic merging

**Key Concepts Learned**:
- `find(x)` returns the representative root of x's component
- `union(x, y)` returns False when x and y are already connected (cycle signal)
- Path compression flattens trees aggressively for fast future lookups
- Union by rank limits tree height growth
- With both optimizations, operation cost is O(α(n)) (effectively constant)
- Non-integer entities (emails) can be solved by index mapping + DSU

**Mistakes Made**:
- Left TODO comments in `main.py` after finishing implementations
- A test expectation in the suite used an incorrect final component count

**Optimization Techniques Discovered**:
- Process only upper triangle in adjacency matrix for undirected province problems
- Fast fail for valid tree using `len(edges) != n - 1`
- Union account emails to the first email in each account to merge all account nodes transitively

**Personal Notes**:
- Union Find is often cleaner than DFS/BFS for repeated connectivity checks
- Failed union is one of the most useful interview signals for cycle detection
- Mapping trick (string -> integer id) unlocks DSU for many real-world style problems

**Test Results**: 42/43 tests passed (1 known test expectation issue) ✅

---

### Day 21: Topological Sort ✅ **COMPLETED**

**Problems Solved** (5 topological sort problems):
1. **Course Schedule** - Kahn's cycle detection (LeetCode #207)
2. **Course Schedule II** - Kahn's with order collection (LeetCode #210)
3. **Alien Dictionary** - Topo sort on character precedence graph (LeetCode #269)
4. **Minimum Height Trees** - Leaf-trimming BFS to find centroids (LeetCode #310)
5. **Parallel Courses** - Layered BFS for minimum semesters (LeetCode #1136)

**Topics Covered**:
- Kahn's algorithm (BFS + indegree queue)
- Cycle detection via `processed == n` check
- Building character precedence graphs from word pairs
- Leaf trimming on undirected trees (MHT centroid finding)
- Layered BFS for parallel scheduling

**Key Concepts Learned**:
- Kahn's algorithm handles cycle detection for free: if `processed < n` after draining the queue, a cycle blocked remaining nodes
- Alien Dictionary: build directed graph between chars from adjacent word pairs; catch invalid prefix case (`["abc", "ab"]`)
- MHT: no directed graph needed — peel leaves inward until ≤ 2 nodes remain (always the centroids)
- Parallel Courses: process entire queue per semester, increment semester counter each BFS level

**Mistakes Made**:
- None — all 5 problems solved correctly on first attempt

**Patterns Locked In**:
- `processed == n` → no cycle (Kahn's)
- `len(order) == numCourses` → valid topo order
- `remaining -= layer_size` then `while remaining > 2` → MHT leaf trimming
- `semester += 1` per BFS layer → min time / parallel scheduling

**Test Results**: 25/25 tests passed ✅

---

### Day 22: Dijkstra's Shortest Path ✅ **COMPLETED**

**Problems Solved** (5 shortest-path problems):
1. **Network Delay Time** - Dijkstra single-source, return max dist (LeetCode #743)
2. **Cheapest Flights Within K Stops** - Bellman-Ford with k+1 rounds (LeetCode #787)
3. **Path With Minimum Effort** - Minimax Dijkstra on grid (LeetCode #1631)
4. **Swim in Rising Water** - Bottleneck Dijkstra on grid (LeetCode #778)
5. **Find City With Smallest Neighbors** - Floyd-Warshall all-pairs (LeetCode #1334)

**Topics Covered**:
- Classic Dijkstra with min-heap + stale-check guard
- Bellman-Ford relaxation rounds with snapshot copy to prevent chaining
- Minimax path: swap `+` for `max()` in the relaxation step
- Floyd-Warshall triple-loop for all-pairs shortest paths

**Key Concepts Learned**:
- Dijkstra requires non-negative weights; stale check `if cost > dist[node]: continue` prevents reprocessing
- Bellman-Ford naturally enforces hop limit: run exactly `k+1` rounds
- Minimax/bottleneck problems (P3, P4) use same Dijkstra skeleton — only the edge cost formula changes
- Floyd-Warshall: O(V³) simple but effective for small dense graphs; `dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])`

**Bugs Caught**:
- P1: `heappush` was outside the `if new_cost < dist` block — pushed stale entries unconditionally
- P2: Debug `print` statements left in from development
- P5: `if minCnt <= minCnt` (always-True self-comparison) — should be `cnt <= minCnt`

**Patterns Locked In**:
- `if cost > dist[node]: continue` → Dijkstra stale guard
- `temp = prices[:]` before each Bellman-Ford round → prevents within-round chaining
- `max(current, edge)` instead of `current + edge` → minimax/bottleneck Dijkstra
- Triple `for k, i, j` loop → Floyd-Warshall

**Test Results**: 25/25 tests passed ✅

---

### Day 23: Minimum Spanning Tree ✅ **COMPLETED**

**Problems Solved** (5 MST problems):
1. **Min Cost to Connect All Points** - Prim's Algorithm (LeetCode #1584)
2. **Minimum Spanning Tree** - Kruskal's Algorithm
3. **Optimize Water Distribution in a Village** - Kruskal's with Virtual Node (LeetCode #1168)
4. **Find Critical and Pseudo-Critical Edges in MST** - Kruskal's with Forced/Skipped edges (LeetCode #1489)
5. **Connecting Cities With Minimum Cost** - Kruskal's with 1-indexed components (LeetCode #1135)

**Topics Covered**:
- Kruskal's Algorithm (Sorting + Union Find)
- Prim's Algorithm (Priority Queue)
- Virtual Node technique for multi-source setup costs
- Forcing and skipping edges to test criticality

**Key Concepts Learned**:
- MST connects all nodes with minimum total edge weight (V-1 edges).
- Kruskal's is best for sparse graphs and standard edge lists (O(E log E)).
- Prim's is often better for dense graphs, but Kruskal's is generally easier to implement with Union-Find.
- Virtual node: connect all initial state costs to a dummy node `0` and run standard MST.
- Critical edges: removing them increases the MST cost. Pseudo-critical edges: forcing them keeps the MST cost the same.

**Test Results**: 23/23 tests passed ✅

---

### Day 24: Advanced Graph Problems ✅ **COMPLETED**

**Problems Solved**:
1. **Reconstruct Itinerary** (LeetCode #332)
2. **Word Ladder** (LeetCode #127)
3. **Critical Connections in a Network** (LeetCode #1192)

**Topics Covered**:
- Eulerian Paths (Hierholzer's Algorithm)
- BFS for Shortest Path in Unweighted Graphs
- Tarjan's Bridge-Finding Algorithm

**Key Concepts Learned**:
- Eulerian Paths require post-order DFS to guarantee no dead ends trap us early.
- Word Ladder is BFS on a massive implicit graph.
- Tarjan's algorithm uses discovery and lowest times to spot back-edges (cycles).

---

### Day 25: DP Introduction (1D Problems) ✅ **COMPLETED**

**Problems Solved**:
1. **Fibonacci Number** (LeetCode #509)
2. **Climbing Stairs** (LeetCode #70)
3. **Min Cost Climbing Stairs** (LeetCode #746)

**Topics Covered**:
- 1D Dynamic Programming Tabulation
- Top-Down Memoization vs Bottom-Up Tabulation
- In-Place Space Optimization

**Key Concepts Learned**:
- DP is just recursion with caching (Memoization) or building from base cases iteratively (Tabulation).
- State transitions like `dp[i] = dp[i-1] + dp[i-2]` can be space-optimized to O(1) by only tracking the last 2 variables.
- The `min()` choice in tabulation allows us to implicitly evaluate overlapping subproblems simultaneously.

---

### Day 26: DP - Climbing Stairs Variations ✅ **COMPLETED**

**Problems Solved**:
1. **N-th Tribonacci Number** (LeetCode #1137)
2. **Decode Ways** (LeetCode #91)

**Topics Covered**:
- 1D DP Tabulation with multiple states
- Space Optimization using sliding windows
- Conditional DP Branching

**Key Concepts Learned**:
- DP Tabulation isn't strictly limited to 2 variables; Tribonacci scales it to 3 seamlessly.
- Decode Ways proves that DP transitions can be strictly conditional (e.g., `if 10 <= val <= 26`), which dynamically enables or chokes subproblem branches.
- `prev_prev` and `prev` are standard variables for tracking state in sequence-based parsing.

---

### Day 27: DP - House Robber Pattern ✅ **COMPLETED**

**Problems Solved**:
1. **House Robber** (LeetCode #198)
2. **House Robber II** (LeetCode #213)

**Topics Covered**:
- 1D DP `max()` Decision Tabulation
- Space Optimization (O(1))
- Handling Circular Array Constraints in DP

**Key Concepts Learned**:
- DP isn't just about accumulating combinations (like Climbing Stairs), it's often about making an optimal choice: `max(rob_this_house, skip_this_house)`.
- A circular array constraint can often be bypassed by simply running the linear DP algorithm twice (once excluding the last element, once excluding the first element) and taking the absolute max.

---

### Day 28: DP - 2D Grid Problems ✅ **COMPLETED**

**Problems Solved**:
1. **Unique Paths** (LeetCode #62)
2. **Minimum Path Sum** (LeetCode #64)

**Topics Covered**:
- 2D DP Tabulation
- In-Place Grid DP (O(1) auxiliary space)
- Pathfinding with DP

**Key Concepts Learned**:
- Extending 1D DP to 2D: `dp[r][c] = dp[r-1][c] + dp[r][c-1]` is the natural extension of the Climbing Stairs pattern into a grid.
- For `minPathSum`, the grid itself acts as the DP table — no extra memory needed! The first row and column are seeded first, then the interior is filled with `grid[r][c] += min(grid[r-1][c], grid[r][c-1])`.
- The optimal path in `minPathSum` can be traced back from `grid[-1][-1]` by always greedily stepping to whichever neighbor has the lower accumulated cost.

---

### Day 29: DP - Knapsack Problems ✅ **COMPLETED**

**Problems Solved**:
1. **Partition Equal Subset Sum** (LeetCode #416)
2. **Target Sum** (LeetCode #494)

**Topics Covered**:
- 0/1 Knapsack Pattern
- Space-Optimized 1D DP using Python Sets and Dicts
- Subset Sum and Expression Evaluation

**Key Concepts Learned**:
- The 0/1 Knapsack pattern involves deciding whether to **include or exclude** an item to hit a target sum or maximize value.
- Instead of using a 2D array, we can use a **Python Set** (for boolean reachability) or a **Python Dict** (for counting ways).
- **CRITICAL**: When space-optimizing 0/1 Knapsack, you must conceptually iterate "backwards" or create a new temporary data structure at each step. This prevents using the same element multiple times (which would turn it into an Unbounded Knapsack problem).
- `dp = {j + n for j in dp} | dp` is an elegant, pure-Python way to safely apply the current number to all previously reachable sums.

---

### Day 30: DP - Longest Common Subsequence ✅ **COMPLETED**

**Problems Solved**:
1. **Longest Common Subsequence** (LeetCode #1143)
2. **Longest Increasing Subsequence** (LeetCode #300)

**Topics Covered**:
- 2D DP Tabulation for Subsequences
- 1D DP Tabulation for Subsequences
- String matching and numerical extending

**Key Concepts Learned**:
- For 2D subsequence matching (like LCS), the table `dp[r][c]` tracks the best match up to index `r` in string1 and index `c` in string2. Matches extend the diagonal (`1 + dp[r-1][c-1]`), while mismatches pull the best historical value from top or left (`max(dp[r-1][c], dp[r][c-1])`).
- For 1D single-array subsequences (like LIS), the array `dp[i]` tracks the longest valid sequence *ending exactly* at `i`. We compute this by looking back at all previous elements `j < i` and extending the best one that satisfies the condition.
- The `O(N^2)` LIS solution provides a great foundational understanding of DP "lookbacks" before moving to the advanced `O(N log N)` binary search optimization.

---

## 🗺️ Complete Learning Journey Roadmap

### **Phase 1: Fundamentals** (Days 1-8) ✅ **COMPLETE**
**Focus**: Core data structures and basic patterns
- Day 1: Arrays & Hash Maps ✅
- Day 2: Prefix Sums + Hash Maps ✅
- Day 3: Sliding Window Fundamentals ✅
- Day 4: Advanced Sliding Window ✅
- Day 5: Two Pointers ✅
- Day 6: Fast/Slow Pointers (Floyd's Cycle Detection) ✅
- Day 7: Stack (LIFO) ✅
- Day 8: Queue & BFS Foundation ✅

### **Phase 2: Advanced Patterns** (Days 9-12) ✅ **COMPLETE**
**Focus**: Pattern recognition and optimization techniques
- Day 9: Monotonic Stack ✅
- Day 10: Linked List Manipulation ✅
- Day 11: Binary Search (Basic) ✅
- Day 12: Binary Search Variations ✅

### **Phase 3: Recursion & Trees** (Days 13-16) ✅ **COMPLETE**
**Focus**: Recursive thinking and tree algorithms
- Day 13: Recursion Fundamentals ✅
- Day 14: Binary Tree Basics (Traversals) ✅
- Day 15: Binary Search Trees ✅
- Day 16: Tree DFS/BFS ✅

### **Phase 4: Advanced Data Structures** (Days 17-20) ✅ **COMPLETE**
**Focus**: Specialized data structures for complex problems
- Day 17: Heap/Priority Queue ✅
- Day 18: Graphs (BFS/DFS) ✅
- Day 19: Trie (Prefix Tree) ✅
- Day 20: Union Find (Disjoint Set) ✅

### **Phase 5: Graph Algorithms** (Days 21-24) ✅ **COMPLETE**
**Focus**: Advanced graph traversal and optimization
- Day 21: Topological Sort ✅
- Day 22: Dijkstra's Shortest Path ✅
- Day 23: Minimum Spanning Tree (Kruskal/Prim) ✅
- Day 24: Advanced Graph Problems ✅

### **Phase 6: Dynamic Programming** (Days 25-32) 🔄 **IN PROGRESS**
**Focus**: Optimization and overlapping subproblems
- Day 25: DP Introduction (1D Problems) ✅
- Day 26: DP - Climbing Stairs Variations ✅
- Day 27: DP - House Robber Pattern ✅
- Day 28: DP - 2D Grid Problems ✅
- Day 29: DP - Knapsack Problems ✅
- Day 30: DP - Longest Common Subsequence ✅
- Day 31: DP - String Problems 🎯 **NEXT**
- Day 32: DP - Advanced Patterns

### **Phase 7: Advanced Algorithms** (Days 33-36) 📋 **PLANNED**
**Focus**: Complex algorithmic techniques
- Day 33: Backtracking (Combinations/Permutations)
- Day 34: Greedy Algorithms Advanced
- Day 35: Bit Manipulation
- Day 36: Math & Number Theory

### **Phase 8: System Design & Practice** (Days 37-40) 📋 **PLANNED**
**Focus**: Integration and real-world applications
- Day 37: Design Problems (LRU Cache, etc.)
- Day 38: Mixed Problem Practice
- Day 39: Hard Problems Marathon
- Day 40: Review & Patterns Summary

---

## 📊 Progress Summary

| Phase | Days | Status | Completion |
|-------|------|--------|------------|
| Phase 1: Fundamentals | 1-8 | ✅ Complete | 8/8 (100%) |
| Phase 2: Advanced Patterns | 9-12 | ✅ Complete | 4/4 (100%) |
| Phase 3: Recursion & Trees | 13-16 | ✅ Complete | 4/4 (100%) |
| Phase 4: Advanced Data Structures | 17-20 | ✅ Complete | 4/4 (100%) |
| Phase 5: Graph Algorithms | 21-24 | ✅ Complete | 4/4 (100%) |
| Phase 6: Dynamic Programming | 25-32 | 🔄 In Progress | 6/8 (75.0%) |
| Phase 7: Advanced Algorithms | 33-36 | 📋 Planned | 0/4 (0%) |
| Phase 8: System Design | 37-40 | 📋 Planned | 0/4 (0%) |

**Overall Progress**: 30/40 days complete (75.0%)

---

## 🧠 Skills & Concepts Map

A cross-reference of every technique learned, mapped to the days it was first introduced and reinforced.

### Fundamentals
| Skill | Days |
|---|---|
| **Hash Maps / Dictionaries** | 1, 2, 3, 4 |
| **Arrays** | 1, 2, 5 |
| **Prefix Sums** | 2 |
| **Sliding Window** | 3, 4, 8 |
| **String Manipulation** | 3, 4 |
| **Frequency Counting** | 4 |
| **Two Pointers** | 5 |
| **Greedy Algorithms** | 5 |

### Linked Lists & Stacks
| Skill | Days |
|---|---|
| **Linked Lists** | 6, 10 |
| **Fast/Slow Pointers** | 6 |
| **Pointer Manipulation** | 6, 10 |
| **Linked List Reversal** | 10 |
| **Stack (LIFO)** | 7 |
| **Monotonic Stack** | 9 |
| **Next Greater Element Pattern** | 9 |
| **Queue (FIFO)** | 8 |

### Search & Divide
| Skill | Days |
|---|---|
| **Binary Search** | 11, 12 |
| **Divide & Conquer** | 11 |
| **Binary Search Variations** | 12 |
| **Boundary Finding** | 12 |

### Recursion & Dynamic Programming
| Skill | Days |
|---|---|
| **Recursion Fundamentals** | 13 |
| **Recursion vs Iteration** | 10, 13 |
| **Memoization (Top-Down DP)** | 13 |
| **Dynamic Programming (Tabulation)** | 13, 25, 26, 27, 28, 29 |
| **Space Optimization (O(1) DP)** | 13, 25, 26, 27 |
| **1D DP Tabulation** | 25, 26, 27 |
| **2D DP Tabulation** | 28 |
| **In-Place Grid DP** | 28 |
| **Circular Array DP Trick** | 27 |
| **Conditional DP Branching** | 26 |
| **0/1 Knapsack Pattern** | 29 |

### Trees
| Skill | Days |
|---|---|
| **Binary Trees** | 14 |
| **Tree Traversals (Pre/In/Post)** | 14 |
| **Binary Search Trees** | 15 |
| **BST Operations** | 15 |
| **Range Validation** | 15 |
| **Inorder = Sorted** | 14, 15 |
| **Tree DFS** | 16 |
| **Tree BFS / Level Order** | 16 |
| **Tree Path Problems** | 16 |
| **Mirror Trees** | 16 |

### Advanced Data Structures
| Skill | Days |
|---|---|
| **Heap Data Structure** | 17 |
| **Priority Queue** | 17 |
| **Min/Max Heap** | 17 |
| **Top K Problems** | 17 |
| **Two-Heap Technique** | 17 |
| **Trie (Prefix Tree)** | 19 |
| **Wildcard DFS on Trie** | 19 |
| **Word Search (Trie + DFS)** | 19 |
| **Union Find (DSU)** | 20 |
| **Path Compression** | 20 |
| **Union by Rank** | 20 |

### Graph Algorithms
| Skill | Days |
|---|---|
| **Graph Traversal (DFS/BFS)** | 16, 18 |
| **Grid as Graph** | 18 |
| **Multi-Source BFS** | 18 |
| **Cycle Detection** | 18, 20, 21 |
| **Graph Cloning** | 18 |
| **Topological Sort** | 18, 21 |
| **Kahn's Algorithm** | 21 |
| **Dijkstra's Algorithm** | 22 |
| **Bellman-Ford** | 22 |
| **Floyd-Warshall** | 22 |
| **Minimax / Bottleneck Path** | 22 |
| **Kruskal's Algorithm (MST)** | 23 |
| **Prim's Algorithm (MST)** | 23 |
| **Virtual Node Technique** | 23 |
| **Eulerian Path (Hierholzer's)** | 24 |
| **Tarjan's Bridge-Finding** | 24 |
| **Word Ladder (BFS)** | 24 |
