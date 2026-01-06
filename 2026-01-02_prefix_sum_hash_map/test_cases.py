# test_cases.py - Sample, edge, and stress tests for Subarray Sum Equals K

from solutions import subarray_sum_prefix_hash, subarray_sum_brute_force, subarray_sum_prefix_array


def run_tests(fn):
    cases = [
        ([1, 1, 1], 2, 2, "basic small"),
        ([1, 2, 3], 3, 2, "multiple subarrays"),
        ([1, -1, 1], 1, 3, "with negatives: [1], [1], [1,-1,1]"),
        ([0, 0, 0], 0, 6, "all zeros"),
        ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4, "mixed positives and negatives"),
        ([], 0, 0, "empty array"),
        ([5], 5, 1, "single element match"),
        ([5], 3, 0, "single element no match"),
    ]

    passed = 0
    failed = 0
    for nums, k, expected, name in cases:
        got = fn(nums, k)
        if got == expected:
            print(f"✅ PASS: {name} -> {got}")
            passed += 1
        else:
            print(f"❌ FAIL: {name} -> got {got}, expected {expected}")
            failed += 1
    print(f"\nSummary: {passed} passed, {failed} failed\n")


if __name__ == "__main__":
    print("Testing subarray_sum_prefix_hash")
    run_tests(subarray_sum_prefix_hash)
    print("Testing subarray_sum_brute_force")
    run_tests(subarray_sum_brute_force)
    print("Testing subarray_sum_prefix_array")
    run_tests(subarray_sum_prefix_array)
