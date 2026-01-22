# Test Cases for Reverse Linked List

from main import (
    reverse_iterative, 
    reverse_recursive, 
    reverse_stack,
    create_linked_list,
    linked_list_to_array
)

# Test data: (input_array, expected_output, description)
test_cases = [
    # Basic cases
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], "basic 5-node list"),
    ([1, 2], [2, 1], "two nodes"),
    ([1], [1], "single node"),
    ([], [], "empty list"),
    
    # Different lengths
    ([1, 2, 3], [3, 2, 1], "three nodes"),
    ([1, 2, 3, 4], [4, 3, 2, 1], "four nodes"),
    ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], "six nodes"),
    
    # Different values
    ([10, 20, 30], [30, 20, 10], "multiples of 10"),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], "already reversed"),
    ([1, 1, 1, 1], [1, 1, 1, 1], "all same values"),
    
    # Negative numbers
    ([-1, -2, -3], [-3, -2, -1], "negative values"),
    ([1, -1, 2, -2], [-2, 2, -1, 1], "mixed pos/neg"),
    
    # Large values
    ([100, 200, 300, 400, 500], [500, 400, 300, 200, 100], "large values"),
    ([1000, 2000], [2000, 1000], "very large values"),
    
    # Longer lists
    (list(range(1, 11)), list(range(10, 0, -1)), "ten nodes (1-10)"),
    (list(range(1, 21)), list(range(20, 0, -1)), "twenty nodes (1-20)"),
]


def test_approach(func, name):
    """Test a reverse linked list implementation"""
    print(f"Testing {name}:")
    passed = 0
    
    for i, (input_arr, expected, description) in enumerate(test_cases, 1):
        # Create linked list from array
        head = create_linked_list(input_arr)
        
        # Reverse it
        reversed_head = func(head)
        
        # Convert back to array
        result = linked_list_to_array(reversed_head)
        
        status = "PASS" if result == expected else "FAIL"
        
        # Format for display
        if len(input_arr) <= 6:
            input_str = str(input_arr)
            result_str = str(result)
        else:
            input_str = f"[{input_arr[0]}...{input_arr[-1]}] (len={len(input_arr)})"
            result_str = f"[{result[0]}...{result[-1]}] (len={len(result)})" if result else "[]"
        
        print(f"  [{status}] Test {i:2d}: {description:25s} {input_str} -> {result_str}")
        
        if status == "FAIL":
            print(f"         Expected: {expected}")
            print(f"         Got:      {result}")
        
        if result == expected:
            passed += 1
    
    print(f"  Summary: {passed}/{len(test_cases)} passed\n")
    return passed


def run_all_tests():
    print("=" * 70)
    print("LEETCODE #206: REVERSE LINKED LIST - TEST SUITE")
    print("=" * 70)
    print()
    
    total_passed = 0
    
    total_passed += test_approach(reverse_iterative, "Iterative (3-Pointer)")
    total_passed += test_approach(reverse_recursive, "Recursive")
    total_passed += test_approach(reverse_stack, "Stack-Based")
    
    total_tests = len(test_cases) * 3
    print("=" * 70)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed (3 approaches × {len(test_cases)} cases)")
    print("=" * 70)


if __name__ == "__main__":
    run_all_tests()
