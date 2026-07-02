# Test Cases for Binary Search
import sys
from main import (
    binary_search_iterative,
    binary_search_recursive,
    binary_search_safe
)

def run_tests():
    """Comprehensive test suite for binary search"""
    
    # Test cases: (nums, target, expected_index)
    test_cases = [
        # Basic cases
        ([-1, 0, 3, 5, 9, 12], 9, 4, "example from problem"),
        ([-1, 0, 3, 5, 9, 12], 2, -1, "target not in array"),
        
        # Edge cases
        ([5], 5, 0, "single element - found"),
        ([5], -5, -1, "single element - not found"),
        ([1, 2], 1, 0, "two elements - first"),
        ([1, 2], 2, 1, "two elements - second"),
        ([1, 2], 0, -1, "two elements - not found"),
        
        # Target at boundaries
        ([1, 2, 3, 4, 5], 1, 0, "target at start"),
        ([1, 2, 3, 4, 5], 5, 4, "target at end"),
        ([1, 2, 3, 4, 5], 3, 2, "target at middle"),
        
        # Larger arrays
        ([1, 3, 5, 7, 9, 11, 13, 15], 7, 3, "8 elements - found middle-left"),
        ([1, 3, 5, 7, 9, 11, 13, 15], 11, 5, "8 elements - found middle-right"),
        ([1, 3, 5, 7, 9, 11, 13, 15], 1, 0, "8 elements - found first"),
        ([1, 3, 5, 7, 9, 11, 13, 15], 15, 7, "8 elements - found last"),
        ([1, 3, 5, 7, 9, 11, 13, 15], 4, -1, "8 elements - not found"),
        ([1, 3, 5, 7, 9, 11, 13, 15], 0, -1, "8 elements - before start"),
        ([1, 3, 5, 7, 9, 11, 13, 15], 20, -1, "8 elements - after end"),
        
        # Negative numbers
        ([-100, -50, -10, 0, 10, 50, 100], -10, 2, "negative target"),
        ([-100, -50, -10, 0, 10, 50, 100], 0, 3, "zero target"),
        ([-100, -50, -10, 0, 10, 50, 100], 100, 6, "positive target"),
        
        # All negative
        ([-10, -8, -6, -4, -2], -6, 2, "all negative numbers"),
        ([-10, -8, -6, -4, -2], -1, -1, "all negative - not found"),
        
        # Large array
        (list(range(0, 100, 2)), 50, 25, "50 elements - found"),
        (list(range(0, 100, 2)), 51, -1, "50 elements - odd number not found"),
        (list(range(0, 100, 2)), 0, 0, "50 elements - first"),
        (list(range(0, 100, 2)), 98, 49, "50 elements - last"),
        
        # Dense array
        (list(range(1, 21)), 10, 9, "consecutive 1-20, find 10"),
        (list(range(1, 21)), 1, 0, "consecutive 1-20, find 1"),
        (list(range(1, 21)), 20, 19, "consecutive 1-20, find 20"),
        (list(range(1, 21)), 15, 14, "consecutive 1-20, find 15"),
        
        # Powers of 2
        ([1, 2, 4, 8, 16, 32, 64, 128], 16, 4, "powers of 2 - find 16"),
        ([1, 2, 4, 8, 16, 32, 64, 128], 32, 5, "powers of 2 - find 32"),
        ([1, 2, 4, 8, 16, 32, 64, 128], 5, -1, "powers of 2 - not found"),
    ]
    
    approaches = [
        ("Iterative (Classic)", binary_search_iterative),
        ("Recursive", binary_search_recursive),
        ("Safe Mid Calculation", binary_search_safe),
    ]
    
    print("=" * 70)
    print("LEETCODE #704: BINARY SEARCH - TEST SUITE")
    print("=" * 70)
    print()
    
    total_passed = 0
    total_tests = 0
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name}:")
        passed = 0
        
        for i, (nums, target, expected, description) in enumerate(test_cases, 1):
            total_tests += 1
            try:
                result = func(nums[:], target)  # Pass copy
                
                if result == expected:
                    status = "PASS"
                    passed += 1
                    total_passed += 1
                else:
                    status = "FAIL"
                    print(f"  [{status}] Test {i:2d}: {description}")
                    print(f"          Input: nums={nums if len(nums) <= 10 else f'{nums[:5]}...{nums[-5:]}'}, target={target}")
                    print(f"          Expected: {expected}, Got: {result}")
                    continue
                
                # For passed tests, show brief summary
                if len(nums) <= 8:
                    nums_str = str(nums)
                else:
                    nums_str = f"[{nums[0]}...{nums[-1]}] (len={len(nums)})"
                
                print(f"  [{status}] Test {i:2d}: {description:30s} nums={nums_str}, target={target} → {result}")
                
            except Exception as e:
                status = "ERROR"
                print(f"  [{status}] Test {i:2d}: {description}")
                print(f"          Exception: {e}")
        
        print(f"  Summary: {passed}/{len(test_cases)} passed")
        print()
    
    print("=" * 70)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed ({len(approaches)} approaches × {len(test_cases)} cases)")
    print("=" * 70)
    
    return total_passed == total_tests


if __name__ == "__main__":
    all_passed = run_tests()
    sys.exit(0 if all_passed else 1)
