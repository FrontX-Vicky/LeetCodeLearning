# Test Cases - Comprehensive Testing for Two Sum

def run_tests(solution_func):
    """
    Run all test cases against a solution function
    
    Args:
        solution_func: The function to test (e.g., two_sum_hash_map)
    """

    print(solution_func)
    test_cases = [
        # (nums, target, expected_output, description)
        
        # BASIC CASES
        ([2, 7, 11, 15], 9, [0, 1], "Basic example from problem"),
        ([3, 2, 4], 6, [1, 2], "Different indices"),
        
        # EDGE CASES
        ([3, 3], 6, [0, 1], "Duplicate numbers - same value"),
        ([0, 0], 0, [0, 1], "Zeros as solution"),
        
        # NEGATIVE NUMBERS
        ([-1, -2, -3, 5, 10], 7, [3, 4], "Mix of negative and positive"),
        ([-10, -8, -6, 0, 5], -16, [0, 1], "Negative numbers only"),
        ([-1, 0, 1, 2, -1, -4], 0, [0, 2], "Multiple zeros and negatives"),
        
        # LARGER ARRAYS
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 17, [8, 8], "Larger array - wait, can't use same element"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 17, [7, 8], "Larger array - 8 + 9 = 17"),
        
        # STRESS CASE
        (list(range(1000)), 1998, [999, 999], "Wait, 999 + 999 = 1998 but can't repeat"),
        (list(range(1000)), 1999, [999, 1000], "Wait, 1000 is out of range"),
        (list(range(1000)), 1997, [998, 999], "Large array - 998 + 999 = 1997"),
    ]
    
    passed = 0
    failed = 0
    
    for nums, target, expected, description in test_cases:
        try:
            result = solution_func(nums, target)
            
            # Check if result is valid (both indices exist and sum to target)
            if (len(result) == 2 and 
                0 <= result[0] < len(nums) and 
                0 <= result[1] < len(nums) and
                result[0] != result[1] and
                nums[result[0]] + nums[result[1]] == target):
                
                print(f"✅ PASS: {description}")
                print(f"   Input: {nums}, target={target}")
                print(f"   Output: {result}")
                passed += 1
            else:
                print(f"❌ FAIL: {description}")
                print(f"   Input: {nums}, target={target}")
                print(f"   Expected valid indices that sum to {target}")
                print(f"   Got: {result}")
                failed += 1
                
        except Exception as e:
            print(f"❌ ERROR: {description}")
            print(f"   Exception: {e}")
            failed += 1
        
        print()
    
    print(f"\n{'='*60}")
    print(f"Results: {passed} passed, {failed} failed out of {passed + failed} tests")
    print(f"{'='*60}\n")
    
    return passed, failed


# ============================================================================
# HOW TO USE
# ============================================================================
"""
After you've written your solution in main.py, test it like this:

from main import two_sum_hash_map
from test_cases import run_tests

run_tests(two_sum_hash_map)
"""


if __name__ == "__main__":
    # Import your solution from main.py
    # Uncomment when you're ready:
    from main import two_sum_hash_map, two_sum_brute_force, two_sum_two_pointers
    run_tests(two_sum_hash_map)
    run_tests(two_sum_brute_force)
    run_tests(two_sum_two_pointers)
    
    print("Test file ready! Write your solution in main.py, then uncomment the code above.")
