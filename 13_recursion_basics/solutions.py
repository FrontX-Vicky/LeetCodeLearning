# Solutions.py - Reference Implementations
# These are complete solutions for you to compare against

def fib_recursive(n):
    """
    APPROACH 1: PURE RECURSION (Naive)
    
    Time: O(2^n) - exponential! Very slow for large n
    Space: O(n) - recursion call stack depth
    
    Why so slow? Massive redundant computation:
    F(5) recalculates F(3) twice, F(2) three times, etc.
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memoization(n, cache=None):
    """
    APPROACH 2: RECURSION WITH MEMOIZATION (Top-Down DP)
    
    Time: O(n) - each value computed once
    Space: O(n) - cache dictionary + recursion stack
    
    Game changer: cache[n] stores result, no recomputation!
    """
    # Initialize cache on first call
    if cache is None:
        cache = {}
    
    # Check cache first (key optimization!)
    if n in cache:
        return cache[n]
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Compute recursively and cache
    result = fib_memoization(n - 1, cache) + fib_memoization(n - 2, cache)
    cache[n] = result  # Store before returning
    
    return result


def fib_dp_array(n):
    """
    APPROACH 3: ITERATIVE BOTTOM-UP DP
    
    Time: O(n) - single loop
    Space: O(n) - array to store all values
    
    Build from bottom: dp[0], dp[1], ..., dp[n]
    No recursion overhead.
    """
    # Edge cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Create DP array
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    # Fill array bottom-up
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fib_optimized(n):
    """
    APPROACH 4: SPACE-OPTIMIZED ITERATIVE (Optimal!)
    
    Time: O(n) - single loop
    Space: O(1) - only 2-3 variables!
    
    Key insight: only need last two values, not entire array.
    This is the production-ready solution.
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Track only last two values
    prev2 = 0  # F(0)
    prev1 = 1  # F(1)
    
    # Compute from F(2) to F(n)
    for i in range(2, n + 1):
        curr = prev1 + prev2
        # Shift values
        prev2 = prev1
        prev1 = curr
    
    return prev1


# ============================================================
# BONUS: FACTORIAL
# ============================================================

def factorial_recursive(n):
    """
    BONUS: Factorial using recursion
    
    Time: O(n) - n recursive calls
    Space: O(n) - call stack
    
    factorial(n) = n × factorial(n-1)
    factorial(0) = 1 (base case)
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """
    BONUS: Factorial using iteration
    
    Time: O(n) - single loop
    Space: O(1) - constant space
    
    More efficient than recursion for factorial.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ============================================================
# VISUAL TRACE EXAMPLES
# ============================================================
"""
FIBONACCI PURE RECURSION TREE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Example: fib(5)

                    fib(5)
                   /      \
              fib(4)      fib(3)
             /      \      /    \
        fib(3)   fib(2) fib(2) fib(1)=1
       /    \    /   \   /   \
   fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
   /   \   =1    =1     =0     =1     =0
fib(1) fib(0)
 =1     =0

Count the calls:
  fib(5): 1 call
  fib(4): 1 call
  fib(3): 2 calls  ← REDUNDANT!
  fib(2): 3 calls  ← REDUNDANT!
  fib(1): 5 calls  ← REDUNDANT!
  fib(0): 3 calls  ← REDUNDANT!
  
Total: 15 function calls for just fib(5)!
For fib(20): over 21,000 calls! Exponential growth!


MEMOIZATION EXECUTION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Example: fib(5) with memoization

Call Stack (left to right is time):

1. fib(5) → not in cache → compute
2.   fib(4) → not in cache → compute
3.     fib(3) → not in cache → compute
4.       fib(2) → not in cache → compute
5.         fib(1) → return 1 (base)
6.         fib(0) → return 0 (base)
7.       fib(2) = 1, cache[2]=1 ✓
8.       fib(1) → return 1 (base)
9.     fib(3) = 2, cache[3]=2 ✓
10.    fib(2) → IN CACHE! return 1 ← No recomputation!
11.  fib(4) = 3, cache[4]=3 ✓
12.  fib(3) → IN CACHE! return 2 ← No recomputation!
13. fib(5) = 5, cache[5]=5 ✓

Total: Only 6 unique computations vs 15 calls in naive!
Linear time instead of exponential!


BOTTOM-UP DP ARRAY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Example: fib(5)

Step 1: Initialize
  dp = [0, 1, ?, ?, ?, ?]
       i=0 i=1

Step 2: Compute dp[2]
  dp[2] = dp[1] + dp[0] = 1 + 0 = 1
  dp = [0, 1, 1, ?, ?, ?]

Step 3: Compute dp[3]
  dp[3] = dp[2] + dp[1] = 1 + 1 = 2
  dp = [0, 1, 1, 2, ?, ?]

Step 4: Compute dp[4]
  dp[4] = dp[3] + dp[2] = 2 + 1 = 3
  dp = [0, 1, 1, 2, 3, ?]

Step 5: Compute dp[5]
  dp[5] = dp[4] + dp[3] = 3 + 2 = 5
  dp = [0, 1, 1, 2, 3, 5]

Return: dp[5] = 5 ✓


SPACE-OPTIMIZED ITERATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Example: fib(5)

Only track last two values:

Initial:
  prev2 = 0 (F(0))
  prev1 = 1 (F(1))

i=2: curr = prev1 + prev2 = 1 + 0 = 1
     shift: prev2=1, prev1=1

i=3: curr = prev1 + prev2 = 1 + 1 = 2
     shift: prev2=1, prev1=2

i=4: curr = prev1 + prev2 = 2 + 1 = 3
     shift: prev2=2, prev1=3

i=5: curr = prev1 + prev2 = 3 + 2 = 5
     shift: prev2=3, prev1=5

Return: prev1 = 5 ✓

Memory usage: Only 3 integers! (vs array of n+1 elements)


FACTORIAL RECURSION TRACE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Example: factorial(5)

Call Stack (top to bottom):

factorial(5)
  return 5 × factorial(4)
    return 4 × factorial(3)
      return 3 × factorial(2)
        return 2 × factorial(1)
          return 1 (base case)
        return 2 × 1 = 2
      return 3 × 2 = 6
    return 4 × 6 = 24
  return 5 × 24 = 120

Result: 120 ✓

Unwinding:
  factorial(1) = 1
  factorial(2) = 2 × 1 = 2
  factorial(3) = 3 × 2 = 6
  factorial(4) = 4 × 6 = 24
  factorial(5) = 5 × 24 = 120


PERFORMANCE COMPARISON:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For fib(30):

Pure Recursion:    2,692,537 function calls  ~1.5 seconds
Memoization:              30 unique calls     ~0.0001 seconds
Bottom-Up DP:             30 iterations       ~0.0001 seconds
Space-Optimized:          30 iterations       ~0.0001 seconds

Pure recursion is 10,000× slower!
Memoization transforms exponential to linear!
"""
