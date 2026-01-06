# test_cases.py - Comprehensive tests

from solutions import min_window_sliding, min_window_brute_force, min_window_counter


def run_tests(fn, name):
    cases = [
        ("ADOBECODEBANC", "ABC", "ADOBEC", "basic example"),
        ("a", "aa", "", "t longer than s"),
        ("a", "a", "a", "single char match"),
        ("ab", "b", "b", "single char in t"),
        ("", "a", "", "empty s"),
        ("aab", "aa", "aa", "duplicates in t"),
        ("aaaaaaaaaaaabbbbbcdd", "abcdd", "abbbbbcdd", "complex"),
        ("ab", "a", "a", "s contains t"),
    ]

    passed = 0
    failed = 0
    print(f"Testing {name}:")
    for s, t, expected, desc in cases:
        result = fn(s, t)
        if result == expected:
            print(f"  ✅ {desc:25} -> '{result}'")
            passed += 1
        else:
            print(f"  ❌ {desc:25} -> got '{result}', expected '{expected}'")
            failed += 1
    
    print(f"  Summary: {passed}/{passed+failed} passed\n")
    return passed, failed


if __name__ == "__main__":
    total_p = 0
    total_f = 0

    p, f = run_tests(min_window_sliding, "min_window_sliding")
    total_p += p
    total_f += f

    p, f = run_tests(min_window_brute_force, "min_window_brute_force")
    total_p += p
    total_f += f

    p, f = run_tests(min_window_counter, "min_window_counter")
    total_p += p
    total_f += f

    print(f"TOTAL: {total_p} passed, {total_f} failed")
