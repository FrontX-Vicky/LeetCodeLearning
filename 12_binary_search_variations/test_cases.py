# Test Cases for Find First and Last Position
import sys
from main import (
    search_range_two_binary,
    search_range_expand,
    search_range_bisect
)

def run_tests():
    """Comprehensive test suite for search range"""
    
    # Test cases: (nums, target, expected_range)
    test_cases = [
        # Example cases
        ([5, 7, 7, 8, 8, 10], 8, [3, 4], "example 1 - multiple occurrences"),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1], "example 2 - not found"),
        ([], 0, [-1, -1], "example 3 - empty array"),
        
        # Single element
        ([1], 1, [0, 0], "single element - found"),
        ([1], 2, [-1, -1], "single element - not found"),
        
        # Two elements
        ([1, 1], 1, [0, 1], "two elements - both match"),
        ([1, 2], 1, [0, 0], "two elements - first matches"),
        ([1, 2], 2, [1, 1], "two elements - second matches"),
        ([1, 2], 3, [-1, -1], "two elements - not found"),
        
        # All same
        ([5, 5, 5, 5], 5, [0, 3], "all elements are target"),
        ([1, 1, 1, 1, 1, 1], 1, [0, 5], "six same elements"),
        
        # Target at boundaries
        ([1, 2, 3, 4, 5], 1, [0, 0], "target at start - single"),
        ([1, 2, 3, 4, 5], 5, [4, 4], "target at end - single"),
        ([1, 1, 2, 3, 4], 1, [0, 1], "target at start - multiple"),
        ([1, 2, 3, 4, 4], 4, [3, 4], "target at end - multiple"),
        
        # Target in middle
        ([1, 2, 3, 3, 3, 4, 5], 3, [2, 4], "target in middle - multiple"),
        ([1, 2, 3, 4, 5, 6, 7], 4, [3, 3], "target in middle - single"),
        
        # Long sequences
        ([1, 2, 2, 2, 2, 2, 3], 2, [1, 5], "long sequence in middle"),
        ([7, 7, 7, 7, 7, 8, 9], 7, [0, 4], "long sequence at start"),
        ([1, 2, 8, 8, 8, 8, 8], 8, [2, 6], "long sequence at end"),
        
        # Negative numbers
        ([-5, -3, -3, -1, 0, 2], -3, [1, 2], "negative target"),
        ([-10, -5, 0, 5, 10], -5, [1, 1], "single negative"),
        
        # Large range
        ([1, 3, 3, 3, 3, 3, 3, 3, 3, 5], 3, [1, 8], "many duplicates"),
        ([0, 0, 1, 1, 1, 2, 2, 2, 2, 3], 2, [5, 8], "duplicates in larger array"),
        
        # Target not in array (various positions)
        ([1, 3, 5, 7, 9], 4, [-1, -1], "target between elements"),
        ([1, 3, 5, 7, 9], 0, [-1, -1], "target before start"),
        ([1, 3, 5, 7, 9], 10, [-1, -1], "target after end"),
        
        # Dense consecutive
        (list(range(1, 21)), 10, [9, 9], "consecutive 1-20, find 10"),
        (list(range(1, 21)), 1, [0, 0], "consecutive 1-20, find 1"),
        (list(range(1, 21)), 20, [19, 19], "consecutive 1-20, find 20"),
        
        # Alternating pattern
        ([1, 1, 2, 2, 3, 3, 4, 4], 2, [2, 3], "alternating pairs - find 2"),
        ([1, 1, 2, 2, 3, 3, 4, 4], 3, [4, 5], "alternating pairs - find 3"),
        
        # Edge case: very long sequence
        ([5] * 100, 5, [0, 99], "100 identical elements"),
        ([1] + [5] * 50 + [9], 5, [1, 50], "50 identical in middle"),
    ]
    
    approaches = [
        ("Two Binary Searches (Optimal)", search_range_two_binary),
        ("Expand Linearly", search_range_expand),
        ("Python Bisect", search_range_bisect),
    ]
    
    print("=" * 80)
    print("LEETCODE #34: FIND FIRST AND LAST POSITION - TEST SUITE")
    print("=" * 80)
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
                if len(nums) <= 10:
                    nums_str = str(nums)
                else:
                    nums_str = f"len={len(nums)}"
                
                print(f"  [{status}] Test {i:2d}: {description:35s} target={target}, result={result}")
                
            except Exception as e:
                status = "ERROR"
                print(f"  [{status}] Test {i:2d}: {description}")
                print(f"          Exception: {e}")
        
        print(f"  Summary: {passed}/{len(test_cases)} passed")
        print()
    
    print("=" * 80)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed ({len(approaches)} approaches × {len(test_cases)} cases)")
    print("=" * 80)
    
    return total_passed == total_tests


if __name__ == "__main__":
    all_passed = run_tests()
    sys.exit(0 if all_passed else 1)
