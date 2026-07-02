# Day 9: Monotonic Stack - Daily Temperatures

**Date:** January 23, 2026  
**Topic:** Monotonic Stack (Next Greater Element Pattern)  
**Problem:** LeetCode #739 - Daily Temperatures  
**Difficulty:** Medium

---

## Problem Statement

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i-th` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

### Example 1:
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Explanation:
- Day 0 (73°): Next warmer is day 1 (74°) → wait 1 day
- Day 1 (74°): Next warmer is day 2 (75°) → wait 1 day
- Day 2 (75°): Next warmer is day 6 (76°) → wait 4 days
- Day 3 (71°): Next warmer is day 5 (72°) → wait 2 days
- Day 4 (69°): Next warmer is day 5 (72°) → wait 1 day
- Day 5 (72°): Next warmer is day 6 (76°) → wait 1 day
- Day 6 (76°): No warmer day → 0
- Day 7 (73°): No warmer day → 0
```

### Example 2:
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

### Example 3:
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

### Constraints:
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

---

## Approach 1: Brute Force (Nested Loops)

**Concept:** For each day, scan forward to find the next warmer temperature.

**Algorithm:**
1. For each day `i`:
   - Look at days `i+1, i+2, ..., n-1`
   - Find first day `j` where `temperatures[j] > temperatures[i]`
   - Set `answer[i] = j - i`
   - If no warmer day found, `answer[i] = 0`

**Complexity:**
- Time: O(n²) - for each day, potentially scan all remaining days
- Space: O(1) - excluding output array

**Pros:** Simple, intuitive  
**Cons:** Too slow for large inputs (up to 10^5 elements)

---

## Approach 2: Monotonic Decreasing Stack

**Concept:** Use stack to track indices of days waiting for warmer temperature. Stack maintains decreasing temperatures (monotonic property).

**Algorithm:**
1. Initialize empty stack and result array (all zeros)
2. Iterate through temperatures:
   - While stack not empty AND current temp > temp at stack top:
     - Pop index from stack
     - Calculate days waited: `current_index - popped_index`
     - Update result for popped index
   - Push current index to stack
3. Return result (remaining stack indices stay 0)

**Why Monotonic Stack?**
- Stack stores indices of days in **decreasing temperature order**
- When we find warmer day, we can resolve all cooler days on stack
- Each element pushed once, popped once → O(n)

**Complexity:**
- Time: O(n) - each index pushed/popped at most once
- Space: O(n) - stack can hold up to n indices

**Pros:** Optimal time complexity, elegant solution  
**Cons:** Requires understanding of monotonic stack pattern

---

## Approach 3: Monotonic Stack with Optimization

**Concept:** Same as Approach 2 but store (index, temperature) tuples for clarity.

**Algorithm:**
1. Store both index and temperature in stack
2. Use tuple unpacking for cleaner code
3. Same O(n) complexity

**Complexity:**
- Time: O(n)
- Space: O(n)

**Pros:** More readable code  
**Cons:** Slightly more memory for tuples

---

## Key Learnings

1. **Monotonic Stack Definition:**
   - Stack that maintains elements in monotonic order (increasing or decreasing)
   - Breaks monotonic property → pop elements until property restored

2. **When to Use Monotonic Stack:**
   - Next Greater Element (NGE) problems
   - Next Smaller Element problems
   - Finding spans (stock span, histogram area)
   - Range queries with min/max

3. **Monotonic Decreasing vs Increasing:**
   - **Decreasing:** Find next greater element (this problem)
   - **Increasing:** Find next smaller element

4. **Pattern Recognition:**
   - "Next greater/smaller..."
   - "Days until..."
   - "Span of..."
   - These all hint at monotonic stack

---

## Monotonic Stack Fundamentals

### What Makes a Stack "Monotonic"?

**Monotonic Decreasing** (this problem):
```
Stack maintains: top → bottom in DECREASING order
Example: [80, 75, 73, 70]
         ↑            ↑
        top         bottom
```

When new element arrives:
- If new > top → **Pop** until new ≤ top (or stack empty)
- Then **Push** new element

**Monotonic Increasing:**
```
Stack maintains: top → bottom in INCREASING order
Example: [70, 73, 75, 80]
         ↑            ↑
        top         bottom
```

---

## Visual Trace Example

**Input:** `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`

```
Index:  0   1   2   3   4   5   6   7
Temp:  73  74  75  71  69  72  76  73
```

**Step-by-Step:**

```
═══════════════════════════════════════════════════════════════════════
i=0, temp=73
═══════════════════════════════════════════════════════════════════════
Stack: []
Action: Push index 0
Stack: [0(73)]
Result: [0, 0, 0, 0, 0, 0, 0, 0]


═══════════════════════════════════════════════════════════════════════
i=1, temp=74
═══════════════════════════════════════════════════════════════════════
Stack: [0(73)]
Action: 74 > 73 → Pop 0, answer[0] = 1 - 0 = 1
Stack: []
Action: Push index 1
Stack: [1(74)]
Result: [1, 0, 0, 0, 0, 0, 0, 0]


═══════════════════════════════════════════════════════════════════════
i=2, temp=75
═══════════════════════════════════════════════════════════════════════
Stack: [1(74)]
Action: 75 > 74 → Pop 1, answer[1] = 2 - 1 = 1
Stack: []
Action: Push index 2
Stack: [2(75)]
Result: [1, 1, 0, 0, 0, 0, 0, 0]


═══════════════════════════════════════════════════════════════════════
i=3, temp=71
═══════════════════════════════════════════════════════════════════════
Stack: [2(75)]
Action: 71 < 75 → No pop, just push
Stack: [2(75), 3(71)]
Result: [1, 1, 0, 0, 0, 0, 0, 0]


═══════════════════════════════════════════════════════════════════════
i=4, temp=69
═══════════════════════════════════════════════════════════════════════
Stack: [2(75), 3(71)]
Action: 69 < 71 → No pop, just push
Stack: [2(75), 3(71), 4(69)]
Result: [1, 1, 0, 0, 0, 0, 0, 0]


═══════════════════════════════════════════════════════════════════════
i=5, temp=72
═══════════════════════════════════════════════════════════════════════
Stack: [2(75), 3(71), 4(69)]
Action: 72 > 69 → Pop 4, answer[4] = 5 - 4 = 1
Stack: [2(75), 3(71)]
Action: 72 > 71 → Pop 3, answer[3] = 5 - 3 = 2
Stack: [2(75)]
Action: 72 < 75 → Stop, push 5
Stack: [2(75), 5(72)]
Result: [1, 1, 0, 2, 1, 0, 0, 0]


═══════════════════════════════════════════════════════════════════════
i=6, temp=76
═══════════════════════════════════════════════════════════════════════
Stack: [2(75), 5(72)]
Action: 76 > 72 → Pop 5, answer[5] = 6 - 5 = 1
Stack: [2(75)]
Action: 76 > 75 → Pop 2, answer[2] = 6 - 2 = 4
Stack: []
Action: Push 6
Stack: [6(76)]
Result: [1, 1, 4, 2, 1, 1, 0, 0]


═══════════════════════════════════════════════════════════════════════
i=7, temp=73
═══════════════════════════════════════════════════════════════════════
Stack: [6(76)]
Action: 73 < 76 → No pop, just push
Stack: [6(76), 7(73)]
Result: [1, 1, 4, 2, 1, 1, 0, 0]


═══════════════════════════════════════════════════════════════════════
END: Stack has leftover indices [6, 7]
These days never found warmer → already 0 in result
═══════════════════════════════════════════════════════════════════════

Final Result: [1, 1, 4, 2, 1, 1, 0, 0] ✓
```

---

## Why O(n) Time?

**Key Insight:** Each index is pushed and popped **at most once**.

```
Push operations:  n (every index pushed once)
Pop operations:   ≤ n (each index popped at most once)
Total:            2n → O(n)
```

Even though we have nested loops (while loop inside for loop), the **amortized** complexity is O(n).

---

## Common Mistakes

1. **Not storing indices (storing temperatures instead):**
   ```python
   # ❌ WRONG
   stack.append(temp)  # Can't calculate days difference!
   
   # ✅ CORRECT
   stack.append(i)  # Store index to calculate i - stack[-1]
   ```

2. **Checking wrong comparison:**
   ```python
   # ❌ WRONG (for next GREATER)
   while stack and temperatures[i] < temperatures[stack[-1]]:
   
   # ✅ CORRECT
   while stack and temperatures[i] > temperatures[stack[-1]]:
   ```

3. **Forgetting to push current index:**
   ```python
   # ❌ WRONG
   while stack and temperatures[i] > temperatures[stack[-1]]:
       # ... pop and update
   # Missing: stack.append(i)
   
   # ✅ CORRECT
   while stack and temperatures[i] > temperatures[stack[-1]]:
       # ... pop and update
   stack.append(i)  # Always push current!
   ```

4. **Initializing result incorrectly:**
   ```python
   # ❌ WRONG
   result = []  # Need pre-allocated array
   
   # ✅ CORRECT
   result = [0] * len(temperatures)  # Pre-fill with 0
   ```

---

## Monotonic Stack Pattern Template

**For Next Greater Element:**
```python
def next_greater(arr):
    n = len(arr)
    result = [0] * n
    stack = []  # Stores indices in decreasing order of values
    
    for i in range(n):
        # Pop all smaller elements (current is their next greater)
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx  # or arr[i] depending on problem
        
        stack.append(i)
    
    return result
```

**For Next Smaller Element:**
```python
def next_smaller(arr):
    n = len(arr)
    result = [0] * n
    stack = []  # Stores indices in increasing order of values
    
    for i in range(n):
        # Pop all greater elements (current is their next smaller)
        while stack and arr[i] < arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        
        stack.append(i)
    
    return result
```

---

## Follow-up Variations

- **LeetCode #496:** Next Greater Element I
- **LeetCode #503:** Next Greater Element II (circular array)
- **LeetCode #901:** Online Stock Span
- **LeetCode #84:** Largest Rectangle in Histogram (uses monotonic stack)
- **LeetCode #42:** Trapping Rain Water (can use monotonic stack)

---

## When to Use Monotonic Stack?

✅ **Use Monotonic Stack When:**
- Finding next/previous greater/smaller element
- Calculating spans or widths
- Range queries with min/max constraints
- Problems asking "how long until..."
- Histogram-based problems

❌ **Don't Use Monotonic Stack When:**
- Need all elements in order (use regular iteration)
- Need random access (use array/list)
- Problem involves sorting (use sort or heap)
- No "next greater/smaller" pattern

---

## Monotonic Stack vs Regular Stack

| Feature | Regular Stack (Day 7) | Monotonic Stack (Day 9) |
|---------|----------------------|-------------------------|
| **Order** | Any order | Strictly monotonic order |
| **Push** | Always push | Conditionally push (after pops) |
| **Pop** | When needed | When monotonic property breaks |
| **Use Case** | Parentheses, DFS, undo | Next greater/smaller |
| **Example** | Valid parentheses | Daily temperatures |

---

## Connection to Previous Days

- **Day 7 (Stack):** Basic LIFO operations → Foundation for monotonic stack
- **Day 8 (Queue):** FIFO vs LIFO comparison → Different access patterns
- **Day 3-4 (Sliding Window):** Both process ranges/windows efficiently

**Key Difference from Day 7:**
- Day 7: Stack stores **what we need** (unmatched brackets)
- Day 9: Stack stores **what we're waiting for** (indices waiting for warmer day)
