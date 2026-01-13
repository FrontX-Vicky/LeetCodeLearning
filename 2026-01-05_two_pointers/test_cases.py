# test_cases.py - Comprehensive tests

from solutions import max_area_two_pointers, max_area_brute_force, max_area_optimized


def run_tests(fn, name):
    cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49, "example from problem"),
        ([1, 1], 1, "equal heights"),
        ([2, 3, 4, 5, 18, 17, 6], 17, "peak in middle"),
        ([], 0, "empty array"),
        ([1], 0, "single element"),
        ([1, 2], 1, "two elements"),
        ([2, 1], 1, "decreasing"),
        ([1, 2, 3, 4, 5], 6, "increasing (4*1 from indices 0,3)"),
    ]

    passed = 0
    failed = 0
    print(f"Testing {name}:")
    for heights, expected, desc in cases:
        result = fn(heights)
        if result == expected:
            print(f"  ✅ {desc:30} -> {result}")
            passed += 1
        else:
            print(f"  ❌ {desc:30} -> got {result}, expected {expected}")
            failed += 1
    
    print(f"  Summary: {passed}/{passed+failed} passed\n")
    return passed, failed


if __name__ == "__main__":
    total_p = 0
    total_f = 0

    p, f = run_tests(max_area_two_pointers, "max_area_two_pointers")
    total_p += p
    total_f += f

    p, f = run_tests(max_area_brute_force, "max_area_brute_force")
    total_p += p
    total_f += f

    p, f = run_tests(max_area_optimized, "max_area_optimized")
    total_p += p
    total_f += f

    print(f"TOTAL: {total_p} passed, {total_f} failed")
