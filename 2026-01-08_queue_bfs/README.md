# Day 8: Queue & BFS Fundamentals - Recent Calls Counter

**Date:** January 22, 2026  
**Topic:** Queue Data Structure (FIFO - First In First Out)  
**Problem:** LeetCode #933 - Number of Recent Calls  
**Difficulty:** Easy

---

## Problem Statement

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:
- `RecentCounter()` Initializes the counter with zero recent requests.
- `int ping(int t)` Adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that have happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is **guaranteed** that every call to `ping` uses a strictly larger value of `t` than the previous call.

### Example 1:
```
Input:
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]

Output:
[null, 1, 2, 3, 3]

Explanation:
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
```

### Constraints:
- `1 <= t <= 10^9`
- Each test case will call `ping` with **strictly increasing** values of `t`
- At most `10^4` calls will be made to `ping`

---

## Approach 1: Queue with List

**Concept:** Use a list as a queue. Add new timestamps to the end, remove old timestamps from the front.

**Algorithm:**
1. Initialize empty list `self.requests`
2. On each `ping(t)`:
   - Append `t` to the queue
   - Remove all timestamps < `t - 3000` from front
   - Return length of queue

**Why Queue?**
- Need to track order of requests (chronological)
- Remove oldest first → FIFO behavior
- Only recent requests matter (within 3000ms window)

**Complexity:**
- Time: O(1) amortized per ping (each request added once, removed once)
- Space: O(W) where W is window size (at most 3000 requests in 3000ms)

**Pros:** Simple, intuitive  
**Cons:** Using list for queue is not optimal in Python

---

## Approach 2: Collections.deque (Optimized)

**Concept:** Use `collections.deque` for efficient queue operations.

**Algorithm:**
1. Initialize `self.queue = deque()`
2. On each `ping(t)`:
   - Append `t` to right
   - While leftmost element < `t - 3000`: popleft()
   - Return `len(self.queue)`

**Why Deque?**
- `deque.append()` → O(1)
- `deque.popleft()` → O(1)
- List's `pop(0)` → O(n) (shifts all elements)

**Complexity:**
- Time: O(1) amortized per operation
- Space: O(W) where W is max requests in 3000ms window

**Pros:** Optimal performance for queue operations  
**Cons:** Need to import `collections`

---

## Approach 3: Manual Sliding Window

**Concept:** Track only the count without storing all timestamps.

**Algorithm:**
1. Store timestamps in deque
2. Use two pointers to maintain window
3. Slide window as new requests come in

**Note:** For this specific problem, we need to track timestamps, so this approach is similar to Approach 2.

**Complexity:**
- Time: O(1) amortized
- Space: O(W)

---

## Key Learnings

1. **Queue = FIFO (First In, First Out):** Perfect for chronological/ordered processing
2. **Common Queue Uses:**
   - Request buffering
   - BFS traversal (upcoming)
   - Task scheduling
   - Sliding window with time constraints
   - Rate limiting
3. **Python Queue Options:**
   - `collections.deque` → Best for general queue (O(1) both ends)
   - `queue.Queue` → Thread-safe, slower
   - `list` → Poor for queue (O(n) for pop(0))
4. **Queue vs Stack:**
   - Queue: First added, first removed
   - Stack: Last added, first removed

---

## Queue Fundamentals

### What is a Queue?
```
Front (remove here)                    Back (add here)
    ↓                                       ↓
   [1] → [3] → [5] → [7] → [9]
    └─────────────────────────┘
         FIFO (First In, First Out)
```

### Operations:
- **Enqueue (append):** Add to back - O(1)
- **Dequeue (popleft):** Remove from front - O(1)
- **Peek:** View front without removing - O(1)
- **isEmpty:** Check if empty - O(1)

### In Python (using deque):
```python
from collections import deque

queue = deque()          # Create empty queue
queue.append(5)          # Enqueue (add to right)
front = queue[0]         # Peek (view front)
value = queue.popleft()  # Dequeue (remove from left)
is_empty = len(queue) == 0
```

---

## Common Mistakes

1. **Using list.pop(0) instead of deque.popleft():**
   ```python
   # ❌ WRONG (O(n) operation)
   queue = []
   queue.pop(0)  # Shifts all elements left
   
   # ✅ CORRECT (O(1) operation)
   from collections import deque
   queue = deque()
   queue.popleft()  # Efficient removal
   ```

2. **Not removing old requests:**
   ```python
   # ❌ WRONG
   def ping(self, t):
       self.queue.append(t)
       return len(self.queue)  # Includes ALL requests, not just recent!
   
   # ✅ CORRECT
   def ping(self, t):
       self.queue.append(t)
       while self.queue and self.queue[0] < t - 3000:
           self.queue.popleft()
       return len(self.queue)
   ```

3. **Forgetting the window is inclusive:**
   ```python
   # ❌ WRONG
   while self.queue[0] <= t - 3000:  # Should be <, not <=
   
   # ✅ CORRECT
   while self.queue[0] < t - 3000:  # Requests at exactly t-3000 are valid
   ```

4. **Not checking if queue is empty:**
   ```python
   # ❌ WRONG
   while self.queue[0] < t - 3000:  # IndexError if queue empty!
   
   # ✅ CORRECT
   while self.queue and self.queue[0] < t - 3000:
   ```

---

## Visual Trace Example

**Input:** `ping(1), ping(100), ping(3001), ping(3002)`

```
Step  Action      Queue State           Window [t-3000, t]    Count
─────────────────────────────────────────────────────────────────────
0     ping(1)     [1]                   [-2999, 1]            1
1     ping(100)   [1, 100]              [-2900, 100]          2
2     ping(3001)  [1, 100, 3001]        [1, 3001]             3
                  Remove 1? No (1 >= 1)
3     ping(3002)  [1, 100, 3001, 3002]  [2, 3002]             ?
                  Remove 1? Yes (1 < 2)
                  [100, 3001, 3002]                           3
```

**Detailed Step 3:**
- New request at t=3002
- Window: [3002 - 3000, 3002] = [2, 3002]
- Check queue front:
  - `1 < 2` → Remove 1 ✓
  - `100 >= 2` → Keep 100 and rest ✓
- Result: [100, 3001, 3002] → count = 3

---

## Queue vs Stack Comparison

| Feature | Queue (FIFO) | Stack (LIFO) |
|---------|--------------|--------------|
| **Add** | Enqueue (back) | Push (top) |
| **Remove** | Dequeue (front) | Pop (top) |
| **Order** | First In, First Out | Last In, First Out |
| **Use Cases** | BFS, scheduling, buffers | DFS, undo, parentheses |
| **Python** | `deque()` | `list` (append/pop) |
| **Analogy** | Line at store | Stack of plates |

---

## Follow-up Variations

- **LeetCode #346:** Moving Average from Data Stream (similar sliding window)
- **LeetCode #362:** Design Hit Counter (time-based counting)
- **LeetCode #641:** Design Circular Deque (fixed-size queue)
- **LeetCode #622:** Design Circular Queue (array-based implementation)

---

## When to Use Queue Pattern?

✅ **Use Queue When:**
- Processing items in order received (FIFO)
- BFS traversal (level-order)
- Sliding window with time/order constraints
- Task scheduling
- Request buffering
- Rate limiting

❌ **Don't Use Queue When:**
- Need last-in-first-out (use stack)
- Need random access (use array/list)
- Need priority-based processing (use heap)
- Need sorted order (use sorted container)

---

## Connection to BFS

**Why is Queue important for BFS?**
- BFS explores level-by-level
- Nodes at same level processed before next level
- Queue ensures correct order: closer nodes → farther nodes

**Preview (Day 18 - Graphs):**
```python
# BFS Template using Queue
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = {start}
    
    while queue:
        node = queue.popleft()  # Process closest nodes first
        
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # Add to back of queue
```

This is exactly the FIFO behavior we're learning today!
