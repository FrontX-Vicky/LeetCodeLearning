# test_cases.py - Comprehensive tests

from solutions import longest_substring_sliding_window, longest_substring_brute_force, longest_substring_with_indices


def run_tests(fn, name):
    cases = [
        ("abcabcbb", 3, "repeated pattern"),
        ("bbbbb", 1, "all same char"),
        ("pwwkew", 3, "complex mix"),
        ("", 0, "empty string"),
        ("au", 2, "all unique"),
        ("dvdf", 3, "overlap scenario"),
        ("a", 1, "single char"),
        ("aab", 2, "duplicate at end"),
    ]

    passed = 0
    failed = 0
    print(f"Testing {name}:")
    for s, expected, desc in cases:
        result = fn(s)
        if result == expected:
            print(f"  ✅ {desc:20} -> {result}")
            passed += 1
        else:
            print(f"  ❌ {desc:20} -> got {result}, expected {expected}")
            failed += 1
    
    print(f"  Summary: {passed}/{passed+failed} passed\n")
    return passed, failed


if __name__ == "__main__":
    total_p = 0
    total_f = 0

    p, f = run_tests(longest_substring_sliding_window, "longest_substring_sliding_window")
    total_p += p
    total_f += f

    p, f = run_tests(longest_substring_brute_force, "longest_substring_brute_force")
    total_p += p
    total_f += f

    p, f = run_tests(longest_substring_with_indices, "longest_substring_with_indices")
    total_p += p
    total_f += f

    print(f"TOTAL: {total_p} passed, {total_f} failed")
