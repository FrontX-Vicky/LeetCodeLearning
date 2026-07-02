# Test Cases - Day 16: Tree DFS & BFS
# Run: python test_cases.py

import sys
from main import (
    max_depth_recursive, max_depth_bfs,
    min_depth_recursive, min_depth_bfs,
    has_path_sum,
    level_order,
    right_side_view,
    is_symmetric,
    build_tree_from_list
)

def run_tests():
    """Run all test cases"""
    
    total_tests = 0
    passed_tests = 0
    
    # ============================================================
    # MAXIMUM DEPTH TESTS (18 tests)
    # ============================================================
    
    print("=" * 60)
    print("MAXIMUM DEPTH TESTS")
    print("=" * 60)
    
    max_depth_tests = [
        # (tree_list, expected_depth, description)
        ([3, 9, 20, None, None, 15, 7], 3, "balanced tree"),
        ([1, None, 2], 2, "right skewed tree"),
        ([1, 2], 2, "left skewed tree"),
        ([1], 1, "single node"),
        ([], 0, "empty tree"),
        ([1, 2, 3, 4, 5], 3, "complete binary tree"),
        ([1, 2, 3, 4, None, None, 5], 3, "mixed tree"),
        ([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, None, None], 4, "perfect binary tree"),
        ([1, 2, None, 3, None, 4, None, 5], 5, "left skewed long path"),
    ]
    
    for tree_list, expected, desc in max_depth_tests:
        tree = build_tree_from_list(tree_list)
        
        # Test recursive
        result = max_depth_recursive(tree)
        total_tests += 1
        if result == expected:
            passed_tests += 1
            print(f"✓ max_depth_recursive: {desc}")
        else:
            print(f"✗ max_depth_recursive: {desc}")
            print(f"  Expected: {expected}, Got: {result}")
        
        # Test BFS
        result = max_depth_bfs(tree)
        total_tests += 1
        if result == expected:
            passed_tests += 1
            print(f"✓ max_depth_bfs: {desc}")
        else:
            print(f"✗ max_depth_bfs: {desc}")
            print(f"  Expected: {expected}, Got: {result}")
    
    # ============================================================
    # MINIMUM DEPTH TESTS (18 tests)
    # ============================================================
    
    print("\n" + "=" * 60)
    print("MINIMUM DEPTH TESTS")
    print("=" * 60)
    
    min_depth_tests = [
        # (tree_list, expected_depth, description)
        ([3, 9, 20, None, None, 15, 7], 2, "leaf at depth 2"),
        ([1, None, 2], 2, "right skewed - must go to leaf"),
        ([1, 2], 2, "left skewed - must go to leaf"),
        ([1], 1, "single node is a leaf"),
        ([], 0, "empty tree"),
        ([1, 2, 3, 4, 5], 2, "leaf at depth 2"),
        ([1, 2, 3, None, None, 4, 5], 3, "leaves at depth 3"),
        ([1, 2, 2, 3, None, None, 3], 3, "unbalanced tree"),
        ([1, 2, None, 3, None, 4], 4, "left skewed path"),
    ]
    
    for tree_list, expected, desc in min_depth_tests:
        tree = build_tree_from_list(tree_list)
        
        # Test recursive
        result = min_depth_recursive(tree)
        total_tests += 1
        if result == expected:
            passed_tests += 1
            print(f"✓ min_depth_recursive: {desc}")
        else:
            print(f"✗ min_depth_recursive: {desc}")
            print(f"  Expected: {expected}, Got: {result}")
        
        # Test BFS
        result = min_depth_bfs(tree)
        total_tests += 1
        if result == expected:
            passed_tests += 1
            print(f"✓ min_depth_bfs: {desc}")
        else:
            print(f"✗ min_depth_bfs: {desc}")
            print(f"  Expected: {expected}, Got: {result}")
    
    # ============================================================
    # PATH SUM TESTS (12 tests)
    # ============================================================
    
    print("\n" + "=" * 60)
    print("PATH SUM TESTS")
    print("=" * 60)
    
    path_sum_tests = [
        # (tree_list, target_sum, expected_result, description)
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True, "path exists: 5→4→11→2"),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 27, True, "path exists: 5→8→13"),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 100, False, "no such path"),
        ([1, 2, 3], 5, False, "sum to non-leaf"),
        ([1, 2], 1, False, "target is root but not leaf"),
        ([1], 1, True, "single node matches"),
        ([], 0, False, "empty tree"),
        ([1, 2, 3], 4, True, "path: 1→3"),
        ([1, -2, -3, 1, 3, -2, None, -1], -1, True, "negative values"),
        ([1, 2, None, 3, None, 4, None, 5], 15, True, "left skewed path"),
        ([1, None, 2, None, 3, None, 4], 10, True, "right skewed path"),
        ([-2, None, -3], -5, True, "all negative"),
    ]
    
    for tree_list, target, expected, desc in path_sum_tests:
        tree = build_tree_from_list(tree_list)
        result = has_path_sum(tree, target)
        total_tests += 1
        if result == expected:
            passed_tests += 1
            print(f"✓ has_path_sum: {desc}")
        else:
            print(f"✗ has_path_sum: {desc}")
            print(f"  Expected: {expected}, Got: {result}")
    
    # ============================================================
    # LEVEL ORDER TRAVERSAL TESTS (10 tests)
    # ============================================================
    
    print("\n" + "=" * 60)
    print("LEVEL ORDER TRAVERSAL TESTS")
    print("=" * 60)
    
    level_order_tests = [
        # (tree_list, expected_result, description)
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]], "standard tree"),
        ([1], [[1]], "single node"),
        ([], [], "empty tree"),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]], "complete tree"),
        ([1, 2, None, 3, None, 4, None, 5], [[1], [2], [3], [4], [5]], "left skewed"),
        ([1, None, 2, None, 3, None, 4, None, 5], [[1], [2], [3], [4], [5]], "right skewed"),
        ([1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]], "mixed tree"),
        ([1, 2, 2, 3, 4, 4, 3], [[1], [2, 2], [3, 4, 4, 3]], "symmetric tree"),
        ([1, 2, 3, None, 4, None, 5], [[1], [2, 3], [4, 5]], "sparse tree"),
        ([5, 4, 7, 3, None, 2, None, -1, None, 9], [[5], [4, 7], [3, 2], [-1, 9]], "mixed values"),
    ]
    
    for tree_list, expected, desc in level_order_tests:
        tree = build_tree_from_list(tree_list)
        result = level_order(tree)
        total_tests += 1
        if result == expected:
            passed_tests += 1
            print(f"✓ level_order: {desc}")
        else:
            print(f"✗ level_order: {desc}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
    
    # ============================================================
    # RIGHT SIDE VIEW TESTS (10 tests)
    # ============================================================
    
    print("\n" + "=" * 60)
    print("RIGHT SIDE VIEW TESTS")
    print("=" * 60)
    
    right_view_tests = [
        # (tree_list, expected_result, description)
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4], "standard case"),
        ([1, None, 3], [1, 3], "right skewed"),
        ([1, 2], [1, 2], "left skewed - still visible"),
        ([1], [1], "single node"),
        ([], [], "empty tree"),
        ([1, 2, 3], [1, 3], "two levels"),
        ([1, 2, 3, 4, 5, 6, 7], [1, 3, 7], "complete tree"),
        ([1, 2, 3, 4, None, None, 5, 6], [1, 3, 5, 6], "mixed visibility"),
        ([1, 2, None, 3, None, 4], [1, 2, 3, 4], "left chain visible"),
        ([1, 2, 3, None, 5, None, 4, None, 6], [1, 3, 4, 6], "deep tree"),
    ]
    
    for tree_list, expected, desc in right_view_tests:
        tree = build_tree_from_list(tree_list)
        result = right_side_view(tree)
        total_tests += 1
        if result == expected:
            passed_tests += 1
            print(f"✓ right_side_view: {desc}")
        else:
            print(f"✗ right_side_view: {desc}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
    
    # ============================================================
    # SYMMETRIC TREE TESTS (14 tests)
    # ============================================================
    
    print("\n" + "=" * 60)
    print("SYMMETRIC TREE TESTS")
    print("=" * 60)
    
    symmetric_tests = [
        # (tree_list, expected_result, description)
        ([1, 2, 2, 3, 4, 4, 3], True, "perfect symmetric"),
        ([1, 2, 2, None, 3, None, 3], False, "asymmetric children"),
        ([1], True, "single node"),
        ([], True, "empty tree"),
        ([1, 2, 2], True, "two level symmetric"),
        ([1, 2, 2, 3, None, None, 3], True, "symmetric with None"),
        ([1, 2, 3], False, "different children"),
        ([1, 2, 2, 3, None, 3, None], False, "mirror positions wrong"),
        ([1, 2, 2, None, 3, 3, None], True, "inner children symmetric"),
        ([1, 0, 0], True, "symmetric with zero"),
        ([1, 2, 2, 2, None, 2], False, "asymmetric depth"),
        ([1, 2, 2, None, 3, None, 3], False, "wrong mirror positions"),
        ([5, 4, 4, None, 1, 1, None], True, "symmetric with gaps"),
        ([1, 2, 2, 3, 4, 4, 3, 5, 6, 7, 8, 8, 7, 6, 5], True, "deep symmetric tree"),
    ]
    
    for tree_list, expected, desc in symmetric_tests:
        tree = build_tree_from_list(tree_list)
        result = is_symmetric(tree)
        total_tests += 1
        if result == expected:
            passed_tests += 1
            print(f"✓ is_symmetric: {desc}")
        else:
            print(f"✗ is_symmetric: {desc}")
            print(f"  Expected: {expected}, Got: {result}")
    
    # ============================================================
    # SUMMARY
    # ============================================================
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total Tests:  {total_tests}")
    print(f"Passed:       {passed_tests}")
    print(f"Failed:       {total_tests - passed_tests}")
    print(f"Success Rate: {passed_tests / total_tests * 100:.1f}%")
    print("=" * 60)
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! 🎉")
        print("You've mastered DFS and BFS traversals!")
        print("\nKey concepts you've learned:")
        print("  ✓ DFS vs BFS (stack vs queue)")
        print("  ✓ Recursive tree traversal")
        print("  ✓ Level-order processing")
        print("  ✓ Path finding algorithms")
        print("  ✓ Tree symmetry checking")
        print("  ✓ Space complexity trade-offs: O(h) vs O(w)")
        return 0
    else:
        print(f"\n{total_tests - passed_tests} test(s) failed.")
        print("Review the failed test cases and check your logic.")
        print("\nCommon pitfalls:")
        print("  • Min depth: Must reach a LEAF node (both children None)")
        print("  • Path sum: Only count paths to leaves")
        print("  • Level order: Track level_size before processing")
        print("  • Right view: Last node at each level")
        print("  • Symmetric: Compare left.left with right.right")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())
