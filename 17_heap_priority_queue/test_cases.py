# Test Cases - Comprehensive Test Suite
# Day 17: Heap & Priority Queue

from main import (
    find_kth_largest,
    top_k_frequent,
    merge_k_lists,
    MedianFinder,
    last_stone_weight,
    k_closest,
    list_to_linked_list,
    linked_list_to_list
)


# ============================================================
# TEST UTILITIES
# ============================================================

class TestRunner:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.test_results = []
    
    def test(self, func, args, expected, description):
        """Run a single test case"""
        try:
            if isinstance(args, tuple):
                result = func(*args)
            else:
                result = func(args)
            
            # Handle list comparison (order may not matter for some problems)
            if isinstance(result, list) and isinstance(expected, list):
                if "order" in description.lower() or "any order" in description.lower():
                    result_sorted = sorted(result) if result and not isinstance(result[0], list) else sorted([sorted(x) if isinstance(x, list) else x for x in result])
                    expected_sorted = sorted(expected) if expected and not isinstance(expected[0], list) else sorted([sorted(x) if isinstance(x, list) else x for x in expected])
                    passed = result_sorted == expected_sorted
                else:
                    passed = result == expected
            else:
                passed = result == expected
            
            if passed:
                print(f"✓ {description}")
                self.passed += 1
            else:
                print(f"✗ {description}")
                print(f"  Expected: {expected}, Got: {result}")
                self.failed += 1
            
            self.test_results.append((description, passed))
        
        except Exception as e:
            print(f"✗ {description}")
            print(f"  Error: {str(e)}")
            self.failed += 1
            self.test_results.append((description, False))
    
    def summary(self):
        """Print test summary"""
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        total = self.passed + self.failed
        print(f"Total Tests:  {total}")
        print(f"Passed:       {self.passed}")
        print(f"Failed:       {self.failed}")
        if total > 0:
            percentage = (self.passed / total) * 100
            print(f"Success Rate: {percentage:.1f}%")
        print("=" * 60)
        
        if self.failed > 0:
            return 1
        return 0


# ============================================================
# TEST CASES
# ============================================================

def run_all_tests():
    runner = TestRunner()
    
    # ========================================
    # PROBLEM 1: KTH LARGEST ELEMENT
    # ========================================
    print("=" * 60)
    print("KTH LARGEST ELEMENT TESTS")
    print("=" * 60)
    
    runner.test(find_kth_largest, ([3,2,1,5,6,4], 2), 5, "find_kth_largest: basic case k=2")
    runner.test(find_kth_largest, ([3,2,3,1,2,4,5,5,6], 4), 4, "find_kth_largest: duplicates k=4")
    runner.test(find_kth_largest, ([1], 1), 1, "find_kth_largest: single element")
    runner.test(find_kth_largest, ([5,4,3,2,1], 1), 5, "find_kth_largest: k=1 (max)")
    runner.test(find_kth_largest, ([5,4,3,2,1], 5), 1, "find_kth_largest: k=n (min)")
    runner.test(find_kth_largest, ([7,6,5,4,3,2,1], 3), 5, "find_kth_largest: sorted desc")
    runner.test(find_kth_largest, ([1,2,3,4,5,6,7], 3), 5, "find_kth_largest: sorted asc")
    runner.test(find_kth_largest, ([-1,-2,-3,-4,-5], 2), -2, "find_kth_largest: negative numbers")
    runner.test(find_kth_largest, ([99,99], 1), 99, "find_kth_largest: all same")
    runner.test(find_kth_largest, ([3,2,1,5,6,4,7,8,9,10], 5), 6, "find_kth_largest: larger array")
    
    # ========================================
    # PROBLEM 2: TOP K FREQUENT
    # ========================================
    print("\n" + "=" * 60)
    print("TOP K FREQUENT TESTS")
    print("=" * 60)
    
    runner.test(top_k_frequent, ([1,1,1,2,2,3], 2), [1,2], "top_k_frequent: basic case (any order)")
    runner.test(top_k_frequent, ([1], 1), [1], "top_k_frequent: single element")
    runner.test(top_k_frequent, ([1,2], 2), [1,2], "top_k_frequent: all unique (any order)")
    runner.test(top_k_frequent, ([4,1,-1,2,-1,2,3], 2), [-1,2], "top_k_frequent: negatives (any order)")
    runner.test(top_k_frequent, ([1,1,1,2,2,3,3,3], 2), [1,3], "top_k_frequent: tie frequencies (any order)")
    runner.test(top_k_frequent, ([5,5,5,5,5], 1), [5], "top_k_frequent: all same")
    runner.test(top_k_frequent, ([1,2,3,4,5,6,7,8,9,1,2,1], 3), [1,2,3], "top_k_frequent: mixed (any order)")
    
    # ========================================
    # PROBLEM 3: MERGE K SORTED LISTS
    # ========================================
    print("\n" + "=" * 60)
    print("MERGE K SORTED LISTS TESTS")
    print("=" * 60)
    
    def test_merge(lists_arrays, expected_array, desc):
        lists = [list_to_linked_list(arr) for arr in lists_arrays]
        result_head = merge_k_lists(lists)
        result = linked_list_to_list(result_head)
        runner.test(lambda: result, None, expected_array, desc)
    
    test_merge([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6], "merge_k_lists: standard case")
    test_merge([], [], "merge_k_lists: empty input")
    test_merge([[]], [], "merge_k_lists: single empty list")
    test_merge([[1]], [1], "merge_k_lists: single element list")
    test_merge([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,4,5,6,7,8,9], "merge_k_lists: non-overlapping")
    test_merge([[1,1,1],[1,1,1]], [1,1,1,1,1,1], "merge_k_lists: all same values")
    test_merge([[-2,-1,0],[1,2,3]], [-2,-1,0,1,2,3], "merge_k_lists: negative and positive")
    test_merge([[1,3,5,7],[2,4,6,8]], [1,2,3,4,5,6,7,8], "merge_k_lists: alternating")
    
    # ========================================
    # PROBLEM 4: MEDIAN FINDER
    # ========================================
    print("\n" + "=" * 60)
    print("MEDIAN FINDER TESTS")
    print("=" * 60)
    
    # Test case 1
    mf1 = MedianFinder()
    mf1.addNum(1)
    mf1.addNum(2)
    runner.test(mf1.findMedian, None, 1.5, "median_finder: [1,2] = 1.5")
    mf1.addNum(3)
    runner.test(mf1.findMedian, None, 2.0, "median_finder: [1,2,3] = 2.0")
    
    # Test case 2
    mf2 = MedianFinder()
    mf2.addNum(6)
    runner.test(mf2.findMedian, None, 6.0, "median_finder: [6] = 6.0")
    mf2.addNum(10)
    runner.test(mf2.findMedian, None, 8.0, "median_finder: [6,10] = 8.0")
    mf2.addNum(2)
    runner.test(mf2.findMedian, None, 6.0, "median_finder: [2,6,10] = 6.0")
    mf2.addNum(6)
    runner.test(mf2.findMedian, None, 6.0, "median_finder: [2,6,6,10] = 6.0")
    mf2.addNum(5)
    runner.test(mf2.findMedian, None, 6.0, "median_finder: [2,5,6,6,10] = 6.0")
    
    # Test case 3: Negatives
    mf3 = MedianFinder()
    mf3.addNum(-1)
    mf3.addNum(-2)
    runner.test(mf3.findMedian, None, -1.5, "median_finder: [-2,-1] = -1.5")
    mf3.addNum(-3)
    runner.test(mf3.findMedian, None, -2.0, "median_finder: [-3,-2,-1] = -2.0")
    
    # Test case 4: Large numbers
    mf4 = MedianFinder()
    for num in [12, 10, 13, 11, 5, 15, 1, 11, 6, 17, 14, 8, 17, 6, 4]:
        mf4.addNum(num)
    runner.test(mf4.findMedian, None, 11.0, "median_finder: large sequence")
    
    # ========================================
    # PROBLEM 5: LAST STONE WEIGHT
    # ========================================
    print("\n" + "=" * 60)
    print("LAST STONE WEIGHT TESTS")
    print("=" * 60)
    
    runner.test(last_stone_weight, [2,7,4,1,8,1], 1, "last_stone_weight: standard case")
    runner.test(last_stone_weight, [1], 1, "last_stone_weight: single stone")
    runner.test(last_stone_weight, [2,2], 0, "last_stone_weight: two equal stones")
    runner.test(last_stone_weight, [1,3], 2, "last_stone_weight: two different stones")
    runner.test(last_stone_weight, [3,7,2], 2, "last_stone_weight: three stones")
    runner.test(last_stone_weight, [1,1,1,1], 0, "last_stone_weight: all equal")
    runner.test(last_stone_weight, [10,4,2,10], 0, "last_stone_weight: pairs cancel")
    runner.test(last_stone_weight, [9,3,2,10], 0, "last_stone_weight: complex cancellation")
    runner.test(last_stone_weight, [5,4,3,2,1], 1, "last_stone_weight: descending order")
    runner.test(last_stone_weight, [1,2,3,4,5], 1, "last_stone_weight: ascending order")
    
    # ========================================
    # PROBLEM 6: K CLOSEST POINTS
    # ========================================
    print("\n" + "=" * 60)
    print("K CLOSEST POINTS TESTS")
    print("=" * 60)
    
    runner.test(k_closest, ([[1,3],[-2,2]], 1), [[-2,2]], "k_closest: k=1 closest")
    runner.test(k_closest, ([[3,3],[5,-1],[-2,4]], 2), [[3,3],[-2,4]], "k_closest: k=2 (any order)")
    runner.test(k_closest, ([[0,1],[1,0]], 2), [[0,1],[1,0]], "k_closest: all points (any order)")
    runner.test(k_closest, ([[1,1]], 1), [[1,1]], "k_closest: single point")
    runner.test(k_closest, ([[0,0],[1,1],[2,2]], 2), [[0,0],[1,1]], "k_closest: including origin (any order)")
    runner.test(k_closest, ([[-5,4],[-6,-5],[4,6]], 2), [[-5,4],[-6,-5]], "k_closest: negatives (any order)")
    runner.test(k_closest, ([[1,0],[0,1],[-1,0],[0,-1]], 3), [[1,0],[0,1],[-1,0]], "k_closest: equidistant (any order)")
    runner.test(k_closest, ([[10,10],[1,1],[2,2]], 1), [[1,1]], "k_closest: large differences")
    runner.test(k_closest, ([[68,97],[34,-84],[60,100],[2,31],[-27,-38]], 3), [[2,31],[-27,-38],[34,-84]], "k_closest: complex (any order)")
    
    # ========================================
    # EDGE CASES
    # ========================================
    print("\n" + "=" * 60)
    print("EDGE CASE TESTS")
    print("=" * 60)
    
    # Large k values
    runner.test(find_kth_largest, ([1,2,3,4,5,6,7,8,9,10], 10), 1, "edge: k equals array length")
    
    # All duplicates
    runner.test(top_k_frequent, ([1,1,1,1,1], 1), [1], "edge: all same elements")
    
    # Empty stone pile
    runner.test(last_stone_weight, [1,1], 0, "edge: stones destroy each other")
    
    # Points at origin
    runner.test(k_closest, ([[0,0],[1,1]], 1), [[0,0]], "edge: point at origin")
    
    return runner.summary()


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    exit_code = run_all_tests()
    
    if exit_code == 0:
        print("\n" + "🎉 " * 20)
        print("ALL TESTS PASSED! Great work!")
        print("🎉 " * 20)
    else:
        print("\n" + "⚠️  " * 20)
        print(f"{exit_code} test(s) failed.")
        print("Review the failed test cases and check your logic.")
        print("\nCommon pitfalls:")
        print("  • Kth largest: Use min heap of size k, not max heap")
        print("  • Top k frequent: Keep k most frequent, not k largest")
        print("  • Merge k lists: Handle empty lists and None nodes")
        print("  • Median finder: Balance heaps correctly (left size ≥ right size)")
        print("  • Stone weight: Use max heap (negate values in Python)")
        print("  • K closest: Can use squared distance (no sqrt needed)")
        print("⚠️  " * 20)
    
    exit(exit_code)
