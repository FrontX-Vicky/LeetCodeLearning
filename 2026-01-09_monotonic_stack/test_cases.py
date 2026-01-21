# Test Cases for Daily Temperatures (Monotonic Stack)

from main import daily_temperatures_brute, daily_temperatures_stack, daily_temperatures_stack_tuples

# Test data: (input_temperatures, expected_output, description)
test_cases = [
    # Basic cases
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0], "example from problem"),
    ([30, 40, 50, 60], [1, 1, 1, 0], "strictly increasing"),
    ([30, 60, 90], [1, 1, 0], "large jumps"),
    ([90, 60, 30], [0, 0, 0], "strictly decreasing"),
    
    # Edge cases
    ([30], [0], "single element"),
    ([50, 50], [0, 0], "all same temperature"),
    ([50, 50, 50, 50], [0, 0, 0, 0], "all same (longer)"),
    
    # Complex patterns
    ([70, 75, 70, 75], [1, 0, 1, 0], "alternating pattern"),
    ([75, 71, 69, 72, 76, 73], [4, 2, 1, 1, 0, 0], "dip then rise"),
    ([89, 62, 70, 58, 47, 47, 46, 76, 100, 70], [8, 1, 5, 4, 3, 2, 1, 1, 0, 0], "complex pattern"),
    
    # Stress patterns
    ([100, 99, 98, 97, 96], [0, 0, 0, 0, 0], "long decreasing"),
    ([30, 31, 32, 33, 34], [1, 1, 1, 1, 0], "long increasing"),
    ([50, 60, 40, 70, 30, 80], [1, 2, 1, 2, 1, 0], "zigzag pattern"),
    ([73, 74, 75, 71, 69, 68, 72, 76, 73], [1, 1, 5, 3, 2, 1, 1, 0, 0], "longer example"),
    
    # Boundary values
    ([30, 100], [1, 0], "min to max"),
    ([100, 30], [0, 0], "max to min"),
    ([30, 30, 100], [2, 1, 0], "duplicate then spike"),
    
    # Multiple plateaus
    ([40, 40, 40, 50, 50, 50], [3, 3, 1, 0, 0, 0], "two plateaus"),
    ([50, 40, 50, 40, 50], [0, 1, 0, 1, 0], "peaks and valleys"),
]


def test_approach(func, name):
    """Test a daily temperatures implementation"""
    print(f"Testing {name}:")
    passed = 0
    
    for i, (temps, expected, description) in enumerate(test_cases, 1):
        result = func(temps)
        status = "PASS" if result == expected else "FAIL"
        
        # Format input for display
        if len(temps) <= 10:
            temps_str = str(temps)
        else:
            temps_str = f"{temps[:3]}...{temps[-2:]}"
        
        # Format output for display
        if len(result) <= 10:
            result_str = str(result)
        else:
            result_str = f"{result[:3]}...{result[-2:]}"
        
        print(f"  [{status}] Test {i:2d}: {description:25s} -> {result_str}")
        
        if status == "FAIL":
            print(f"         Input: {temps}")
            print(f"         Expected: {expected}")
            print(f"         Got:      {result}")
        
        if result == expected:
            passed += 1
    
    print(f"  Summary: {passed}/{len(test_cases)} passed\n")
    return passed


def run_all_tests():
    print("=" * 70)
    print("LEETCODE #739: DAILY TEMPERATURES - TEST SUITE")
    print("=" * 70)
    print()
    
    total_passed = 0
    
    total_passed += test_approach(daily_temperatures_brute, "Brute Force (O(n²))")
    total_passed += test_approach(daily_temperatures_stack, "Monotonic Stack (O(n))")
    total_passed += test_approach(daily_temperatures_stack_tuples, "Stack with Tuples (O(n))")
    
    total_tests = len(test_cases) * 3
    print("=" * 70)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed (3 approaches × {len(test_cases)} cases)")
    print("=" * 70)


if __name__ == "__main__":
    run_all_tests()
