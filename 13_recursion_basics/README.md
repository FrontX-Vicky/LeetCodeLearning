# Day 13: Recursion Fundamentals - Fibonacci & Factorial

## LeetCode #509: Fibonacci Number

### Problem Description
The **Fibonacci numbers**, commonly denoted `F(n)`, form a sequence called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is:

```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1
```

Given `n`, calculate `F(n)`.

**Example 1:**
```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1
```

**Example 2:**
```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2
```

**Example 3:**
```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3
```

**Constraints:**
- 0 ≤ n ≤ 30

---

## Four Approaches

### Approach 1: Pure Recursion (Naive)
**Direct translation of mathematical definition**

**Strategy:**
1. Base cases: `F(0) = 0`, `F(1) = 1`
2. Recursive case: `F(n) = F(n-1) + F(n-2)`
3. Let recursion handle the rest

**Why it's simple but slow:**
- Most intuitive approach
- **Major problem:** Massive redundant computation!
- Calculates same values repeatedly

**Time Complexity:** O(2^n) - exponential (very slow!)
**Space Complexity:** O(n) - recursion call stack depth

**Visualization of redundancy:**
```
F(5) calls:
    F(4) + F(3)
    F(4) calls: F(3) + F(2)  ← F(3) calculated again!
    F(3) calls: F(2) + F(1)  ← F(2) calculated again!
    ... many repeated calls
```

---

### Approach 2: Recursion with Memoization (Top-Down DP)
**Cache results to avoid recomputation**

**Strategy:**
1. Use a dictionary/array to store computed results
2. Before computing `F(n)`, check if already in cache
3. If in cache, return it immediately
4. Otherwise, compute, store in cache, then return

**Why it works:**
- Each F(n) calculated only once
- Subsequent calls use cached value
- This is **Dynamic Programming (Top-Down)**

**Time Complexity:** O(n) - each value computed once
**Space Complexity:** O(n) - cache + recursion stack

---

### Approach 3: Iterative with Array (Bottom-Up DP)
**Build solution from bottom up**

**Strategy:**
1. Create array to store all Fibonacci numbers up to n
2. Fill array iteratively: `dp[i] = dp[i-1] + dp[i-2]`
3. Return `dp[n]`

**Why it's better:**
- No recursion overhead
- Straightforward loop
- Can see all intermediate values

**Time Complexity:** O(n) - one loop
**Space Complexity:** O(n) - array storage

---

### Approach 4: Iterative Space-Optimized (Optimal)
**Only track last two values**

**Strategy:**
1. Only need previous two numbers to compute next
2. Use two variables: `prev2`, `prev1`
3. Update variables as you go: `curr = prev1 + prev2`
4. Shift variables: `prev2 = prev1`, `prev1 = curr`

**Why it's optimal:**
- O(n) time (same as others)
- **O(1) space** - only 2-3 variables!
- Most efficient solution

**Time Complexity:** O(n)
**Space Complexity:** O(1) - constant space!

---

## Bonus: Factorial Problem

We'll also implement **Factorial** to practice recursion:
```
factorial(n) = n! = n × (n-1) × (n-2) × ... × 1
factorial(0) = 1 (base case)
factorial(n) = n × factorial(n-1)
```

**Example:** `factorial(5) = 5 × 4 × 3 × 2 × 1 = 120`

---

## Key Learnings

### 1. **Recursion Components (The Recipe)**
Every recursive function needs:
```python
def recursive_function(n):
    # 1. BASE CASE(S) - when to stop
    if n == 0 or n == 1:
        return base_value
    
    # 2. RECURSIVE CASE - break down problem
    return combine(recursive_function(n-1), ...)
    
    # 3. TRUST THE RECURSION - assume smaller calls work!
```

### 2. **Recursion Tree Visualization**
```
F(5)
├── F(4)
│   ├── F(3)
│   │   ├── F(2)
│   │   │   ├── F(1) → 1
│   │   │   └── F(0) → 0
│   │   └── F(1) → 1
│   └── F(2)
│       ├── F(1) → 1
│       └── F(0) → 0
└── F(3)
    ├── F(2)
    │   ├── F(1) → 1
    │   └── F(0) → 0
    └── F(1) → 1

Notice: F(3) calculated TWICE, F(2) THREE times!
```

### 3. **Memoization Pattern**
```python
cache = {}

def fib_memo(n):
    if n in cache:  # Check cache first!
        return cache[n]
    
    # Base cases
    if n <= 1:
        return n
    
    # Compute and cache
    result = fib_memo(n-1) + fib_memo(n-2)
    cache[n] = result  # Store before returning
    return result
```

### 4. **Space Optimization Technique**
```python
# Instead of: dp = [0, 1, 1, 2, 3, 5, 8, ...]
# Just track: prev2=3, prev1=5, curr=8
# Then shift:  prev2=5, prev1=8, curr=13
```

### 5. **When to Use Each Approach**
| Approach | Use When | Avoid When |
|----------|----------|------------|
| **Pure Recursion** | Learning, small inputs | Performance matters |
| **Memoization** | Top-down thinking natural | Space is tight |
| **Bottom-Up DP** | Need all intermediate values | Only need final answer |
| **Space-Optimized** | Production code, constraints | Debugging needed |

---

## Common Recursion Mistakes

❌ **No base case** → Infinite recursion → Stack overflow
❌ **Wrong base case** → Incorrect results
❌ **Not making progress** → Each call must get "smaller"
❌ **Modifying during recursion** → Unexpected side effects

✅ **Always ask:** "What's the simplest case?" (base case)
✅ **Trust the recursion** - don't try to trace entire tree mentally!
✅ **Test with small inputs** - base case, n=2, n=3

---

## Real-World Applications

1. **Tree/Graph traversal** - DFS uses recursion
2. **Divide & conquer algorithms** - merge sort, quick sort
3. **Backtracking** - solving puzzles, generating combinations
4. **Dynamic programming** - optimal substructure problems
5. **Compiler design** - parsing expressions

---

## Testing Strategy

**Test Cases:**
- Base cases: n=0, n=1
- Small values: n=2, n=3, n=4
- Medium values: n=10, n=15
- Larger values: n=20, n=30
- Edge cases: boundary of constraints

**Verify:**
- Correct values (known Fibonacci sequence)
- Performance (memoized vs naive)
- Space usage (optimized vs array)

---

## Master Concept: **Recursion & Dynamic Programming**

**Core Principle:**
Break problem into smaller, identical subproblems. Solve base case, combine results.

**Pattern Recognition:**
- "Can be expressed in terms of itself" = Recursion candidate
- "Overlapping subproblems" = Add memoization (DP)
- "Only need last few values" = Space optimize

**Recursion → Memoization → Bottom-Up → Space-Optimized**
This is the **evolution of optimization**!

---

## Time to Practice! 🚀

Open `main.py` and implement all approaches. Compare performance. Run `python test_cases.py` to verify!
