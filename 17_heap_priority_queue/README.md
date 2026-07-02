# Day 17: Heap & Priority Queue

**Date**: January 17, 2026  
**Focus**: Master heap data structure and priority queue operations

---

## 📚 Today's Problems

### Problem 1: Kth Largest Element in Array
- **LeetCode**: [#215 - Kth Largest Element in Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- **Difficulty**: Medium
- **Approach**: Min heap, Max heap, Quickselect

### Problem 2: Top K Frequent Elements
- **LeetCode**: [#347 - Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- **Difficulty**: Medium
- **Approach**: Hash map + heap, bucket sort

### Problem 3: Merge K Sorted Lists
- **LeetCode**: [#23 - Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- **Difficulty**: Hard
- **Approach**: Min heap with linked list nodes

### Problem 4: Find Median from Data Stream
- **LeetCode**: [#295 - Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- **Difficulty**: Hard
- **Approach**: Two heaps (max heap + min heap)

### Problem 5: Last Stone Weight
- **LeetCode**: [#1046 - Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)
- **Difficulty**: Easy
- **Approach**: Max heap simulation

### Problem 6: K Closest Points to Origin
- **LeetCode**: [#973 - K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
- **Difficulty**: Medium
- **Approach**: Min heap with distance calculation

---

## 🎯 Learning Objectives

1. **Understand Heap Structure**
   - Complete binary tree property
   - Min heap vs max heap
   - Heapify operations

2. **Master Python's heapq Module**
   - `heappush()` and `heappop()`
   - `heapify()` for list conversion
   - `nlargest()` and `nsmallest()`
   - Simulating max heap with negation

3. **Priority Queue Pattern**
   - Insert: O(log n)
   - Extract min/max: O(log n)
   - Peek: O(1)
   - Build heap: O(n)

4. **Common Use Cases**
   - Top K elements
   - Kth largest/smallest
   - Merge sorted sequences
   - Streaming median
   - Task scheduling

---

## 🔑 Key Concepts

### Heap Properties
```
Min Heap:           Max Heap:
    1                  9
   / \                / \
  3   5              7   5
 / \ /              / \ /
4  8 6             3  2 1

Parent ≤ Children   Parent ≥ Children
```

### Time Complexities
| Operation | Time Complexity |
|-----------|----------------|
| Insert | O(log n) |
| Extract Min/Max | O(log n) |
| Peek | O(1) |
| Build Heap | O(n) |
| Heapify | O(log n) |

### Python heapq (Min Heap by Default)
```python
import heapq

# Min heap operations
heap = []
heapq.heappush(heap, 5)    # Insert
min_val = heapq.heappop(heap)  # Extract min
heapq.heapify(list)        # Convert list to heap

# Max heap trick (negate values)
max_heap = []
heapq.heappush(max_heap, -5)
max_val = -heapq.heappop(max_heap)
```

---

## 💡 Problem-Solving Patterns

### Pattern 1: Top K Elements
- Use min heap of size K
- If element > heap[0], replace it
- Result: K largest elements in heap

### Pattern 2: Kth Largest/Smallest
- Min heap for Kth largest (size K)
- Max heap for Kth smallest (size K)
- Return heap[0]

### Pattern 3: Merge K Sorted
- Push first element of each list to heap
- Pop min, push next from same list
- Repeat until all processed

### Pattern 4: Two Heap (Median)
- Max heap (left half) + Min heap (right half)
- Balance sizes: |left| ≈ |right|
- Median = heap tops

---

## 📝 Implementation Notes

### Files Structure
- `main.py` - Your implementations (work here!)
- `solutions.py` - Reference solutions with detailed comments
- `test_cases.py` - Comprehensive test suite

### Workflow
1. Read problem descriptions
2. Implement in `main.py`
3. Run: `python main.py` (smoke tests)
4. Run: `python test_cases.py` (full suite)
5. Compare with `solutions.py` if stuck

---

## 🚀 Getting Started

```bash
cd 17_heap_priority_queue
python main.py          # Quick smoke test
python test_cases.py    # Full test suite
```

---

## 📖 Resources

- [Python heapq Documentation](https://docs.python.org/3/library/heapq.html)
- [Heap Data Structure Visualization](https://visualgo.net/en/heap)
- [Priority Queue Patterns](https://leetcode.com/explore/learn/card/heap/)

---

## ✅ Success Criteria

- [ ] Understand min heap vs max heap
- [ ] Implement all 6 problems
- [ ] Pass all test cases
- [ ] Explain time/space complexity
- [ ] Recognize when to use heaps

---

**Next**: Day 18 - Graphs (BFS/DFS)
