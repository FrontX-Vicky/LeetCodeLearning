# Main.py - Your Working File
# Task: Solve LeetCode #509: Fibonacci Number
# Goal: Master recursion fundamentals and optimization techniques

# TODO 1: Approach 1 - Pure Recursion (Naive)
# - Direct translation of F(n) = F(n-1) + F(n-2)
# - Base cases: F(0) = 0, F(1) = 1
# - Time: O(2^n), Space: O(n) stack

def fib_recursive(n):
    """
    APPROACH 1: PURE RECURSION (Naive)
    
    Most intuitive but slowest - exponential time!
    Calculates same values many times.
    
    Args:
        n: non-negative integer
    
    Returns:
        nth Fibonacci number
    
    Example:
        fib(5):
          = fib(4) + fib(3)
          = (fib(3) + fib(2)) + (fib(2) + fib(1))
          = ... many recursive calls
          = 5
    """
    # Your code here
    pass


# TODO 2: Approach 2 - Recursion with Memoization
# - Cache computed results
# - Check cache before computing
# - Time: O(n), Space: O(n)

def fib_memoization(n, cache=None):
    """
    APPROACH 2: RECURSION WITH MEMOIZATION (Top-Down DP)
    
    Cache results to avoid recomputation.
    Each F(n) calculated only once!
    
    Args:
        n: non-negative integer
        cache: dictionary to store computed values
    
    Returns:
        nth Fibonacci number
    
    Pattern:
        1. Check if n in cache → return immediately
        2. Otherwise compute recursively
        3. Store in cache before returning
    """
    # Initialize cache on first call
    if cache is None:
        cache = {}
    
    # Your code here
    pass


# TODO 3: Approach 3 - Iterative Bottom-Up DP
# - Build array from F(0) to F(n)
# - dp[i] = dp[i-1] + dp[i-2]
# - Time: O(n), Space: O(n)

def fib_dp_array(n):
    """
    APPROACH 3: ITERATIVE BOTTOM-UP DP
    
    Build solution from bottom up using array.
    No recursion overhead.
    
    Args:
        n: non-negative integer
    
    Returns:
        nth Fibonacci number
    
    Strategy:
        dp[0] = 0
        dp[1] = 1
        dp[i] = dp[i-1] + dp[i-2] for i from 2 to n
    """
    # Your code here
    pass


# TODO 4: Approach 4 - Space-Optimized Iterative
# - Only track last two values
# - Update: prev2, prev1, curr
# - Time: O(n), Space: O(1)

def fib_optimized(n):
    """
    APPROACH 4: SPACE-OPTIMIZED ITERATIVE (Optimal!)
    
    Only need previous two numbers to compute next.
    Constant space - most efficient!
    
    Args:
        n: non-negative integer
    
    Returns:
        nth Fibonacci number
    
    Strategy:
        Track only: prev2, prev1
        Compute: curr = prev1 + prev2
        Shift: prev2 = prev1, prev1 = curr
    """
    # Your code here
    pass


# ============================================================
# BONUS: FACTORIAL (Additional Recursion Practice)
# ============================================================

def factorial_recursive(n):
    """
    BONUS: Factorial using recursion
    
    factorial(n) = n! = n × (n-1)!
    factorial(0) = 1 (base case)
    
    Example:
        factorial(5) = 5 × 4 × 3 × 2 × 1 = 120
    """
    # Your code here
    pass


def factorial_iterative(n):
    """
    BONUS: Factorial using iteration
    
    More efficient than recursion for this problem.
    """
    # Your code here
    pass


# ============================================================
# TESTING HELPERS (Don't modify)
# ============================================================

def test_function(func, n, expected):
    """Helper to test a single function"""
    result = func(n)
    return result == expected, result


if __name__ == "__main__":
    # Quick smoke test
    print("=" * 60)
    print("FIBONACCI SMOKE TEST")
    print("=" * 60)
    
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (5, 5),
        (10, 55)
    ]
    
    print("\nTesting Pure Recursion:")
    for n, expected in test_cases:
        result = fib_recursive(n)
        status = "✓" if result == expected else "✗"
        print(f"  {status} fib({n}) = {result} (expected {expected})")
    
    print("\nTesting Memoization:")
    for n, expected in test_cases:
        result = fib_memoization(n)
        status = "✓" if result == expected else "✗"
        print(f"  {status} fib({n}) = {result} (expected {expected})")
    
    print("\nTesting Bottom-Up DP:")
    for n, expected in test_cases:
        result = fib_dp_array(n)
        status = "✓" if result == expected else "✗"
        print(f"  {status} fib({n}) = {result} (expected {expected})")
    
    print("\nTesting Space-Optimized:")
    for n, expected in test_cases:
        result = fib_optimized(n)
        status = "✓" if result == expected else "✗"
        print(f"  {status} fib({n}) = {result} (expected {expected})")
    
    print("\n" + "=" * 60)
    print("FACTORIAL SMOKE TEST")
    print("=" * 60)
    
    factorial_tests = [(0, 1), (1, 1), (5, 120), (10, 3628800)]
    
    print("\nTesting Factorial Recursive:")
    for n, expected in factorial_tests:
        result = factorial_recursive(n)
        status = "✓" if result == expected else "✗"
        print(f"  {status} {n}! = {result} (expected {expected})")
    
    print("\nTesting Factorial Iterative:")
    for n, expected in factorial_tests:
        result = factorial_iterative(n)
        status = "✓" if result == expected else "✗"
        print(f"  {status} {n}! = {result} (expected {expected})")
    
    print("\nRun 'python test_cases.py' for full test suite!")
