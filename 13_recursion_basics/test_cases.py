# Test Cases for Fibonacci and Factorial
import sys
import time
from main import (
    fib_recursive,
    fib_memoization,
    fib_dp_array,
    fib_optimized,
    factorial_recursive,
    factorial_iterative
)

def run_tests():
    """Comprehensive test suite for recursion problems"""
    
    # Fibonacci test cases: (n, expected)
    fib_tests = [
        (0, 0, "base case F(0)"),
        (1, 1, "base case F(1)"),
        (2, 1, "F(2) = F(1) + F(0)"),
        (3, 2, "F(3) = 1 + 1"),
        (4, 3, "F(4) = 2 + 1"),
        (5, 5, "F(5) = 3 + 2"),
        (6, 8, "F(6) = 5 + 3"),
        (7, 13, "F(7)"),
        (8, 21, "F(8)"),
        (9, 34, "F(9)"),
        (10, 55, "F(10)"),
        (15, 610, "F(15)"),
        (20, 6765, "F(20)"),
        (25, 75025, "F(25)"),
        (30, 832040, "F(30) - max constraint"),
    ]
    
    # Factorial test cases: (n, expected)
    factorial_tests = [
        (0, 1, "0! = 1 (base case)"),
        (1, 1, "1! = 1"),
        (2, 2, "2! = 2"),
        (3, 6, "3! = 6"),
        (4, 24, "4! = 24"),
        (5, 120, "5! = 120"),
        (6, 720, "6!"),
        (7, 5040, "7!"),
        (8, 40320, "8!"),
        (9, 362880, "9!"),
        (10, 3628800, "10!"),
        (12, 479001600, "12!"),
    ]
    
    fib_approaches = [
        ("Pure Recursion (Naive)", fib_recursive, 20),  # Limit to 20 for speed
        ("Memoization (Top-Down DP)", fib_memoization, None),
        ("Bottom-Up DP Array", fib_dp_array, None),
        ("Space-Optimized (Optimal)", fib_optimized, None),
    ]
    
    factorial_approaches = [
        ("Recursive", factorial_recursive),
        ("Iterative", factorial_iterative),
    ]
    
    print("=" * 80)
    print("LEETCODE #509: FIBONACCI NUMBER - TEST SUITE")
    print("=" * 80)
    print()
    
    total_passed = 0
    total_tests = 0
    
    # Test Fibonacci approaches
    for approach_name, func, limit in fib_approaches:
        print(f"Testing {approach_name}:")
        passed = 0
        
        # Filter tests based on limit (for slow naive recursion)
        tests_to_run = fib_tests if limit is None else [(n, e, d) for n, e, d in fib_tests if n <= limit]
        
        for n, expected, description in tests_to_run:
            total_tests += 1
            try:
                result = func(n)
                
                if result == expected:
                    status = "PASS"
                    passed += 1
                    total_passed += 1
                else:
                    status = "FAIL"
                    print(f"  [{status}] {description:30s} n={n:2d}, expected={expected}, got={result}")
                    continue
                
                print(f"  [{status}] {description:30s} F({n:2d}) = {result}")
                
            except Exception as e:
                status = "ERROR"
                print(f"  [{status}] {description:30s} n={n}")
                print(f"          Exception: {e}")
        
        skipped = len(fib_tests) - len(tests_to_run)
        skip_msg = f" (skipped {skipped} large tests for performance)" if skipped > 0 else ""
        print(f"  Summary: {passed}/{len(tests_to_run)} passed{skip_msg}")
        print()
    
    # Performance comparison for F(25)
    print("=" * 80)
    print("PERFORMANCE COMPARISON - F(25)")
    print("=" * 80)
    
    test_n = 25
    expected = 75025
    
    # Skip naive recursion for F(25) - too slow!
    print(f"\n⚠ Pure Recursion: SKIPPED (would take ~10 seconds for F(25))")
    print(f"  Exponential time: O(2^n) = ~33 million calls!")
    
    for approach_name, func, _ in fib_approaches[1:]:  # Skip first (naive)
        start = time.time()
        result = func(test_n)
        elapsed = time.time() - start
        
        status = "✓" if result == expected else "✗"
        print(f"{status} {approach_name:30s} = {result:7d} in {elapsed*1000:.4f}ms")
    
    print()
    
    # Test Factorial approaches
    print("=" * 80)
    print("BONUS: FACTORIAL - TEST SUITE")
    print("=" * 80)
    print()
    
    for approach_name, func in factorial_approaches:
        print(f"Testing {approach_name}:")
        passed = 0
        
        for n, expected, description in factorial_tests:
            total_tests += 1
            try:
                result = func(n)
                
                if result == expected:
                    status = "PASS"
                    passed += 1
                    total_passed += 1
                else:
                    status = "FAIL"
                    print(f"  [{status}] {description:30s} n={n:2d}, expected={expected}, got={result}")
                    continue
                
                print(f"  [{status}] {description:30s} {n:2d}! = {result}")
                
            except Exception as e:
                status = "ERROR"
                print(f"  [{status}] {description:30s} n={n}")
                print(f"          Exception: {e}")
        
        print(f"  Summary: {passed}/{len(factorial_tests)} passed")
        print()
    
    print("=" * 80)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed")
    print("=" * 80)
    
    return total_passed == total_tests


if __name__ == "__main__":
    all_passed = run_tests()
    sys.exit(0 if all_passed else 1)
