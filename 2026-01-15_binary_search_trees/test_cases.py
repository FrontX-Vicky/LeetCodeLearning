# Test Cases for Binary Search Trees
import sys

# Import from main.py
from main import (
    TreeNode,
    search_bst_recursive,
    search_bst_iterative,
    insert_bst_recursive,
    insert_bst_iterative,
    is_valid_bst,
    find_min_bst,
    find_max_bst,
    kth_smallest,
    build_tree_from_list,
    tree_to_list
)

def run_tests():
    """Comprehensive test suite for BST operations"""
    
    print("=" * 80)
    print("BINARY SEARCH TREE - TEST SUITE")
    print("=" * 80)
    print()
    
    total_passed = 0
    total_tests = 0
    
    # ============================================================
    # TEST 1: SEARCH IN BST
    # ============================================================
    print("=" * 80)
    print("TEST 1: SEARCH IN BST")
    print("=" * 80)
    print()
    
    search_cases = [
        # (tree, target, expected_val_or_none, description)
        ([4, 2, 7, 1, 3], 2, 2, "search existing value in middle"),
        ([4, 2, 7, 1, 3], 5, None, "search non-existing value"),
        ([4, 2, 7, 1, 3], 1, 1, "search leaf node"),
        ([4, 2, 7, 1, 3], 4, 4, "search root"),
        ([5], 5, 5, "single node found"),
        ([5], 3, None, "single node not found"),
        ([], 1, None, "empty tree"),
    ]
    
    for impl_name, func in [("Recursive", search_bst_recursive), ("Iterative", search_bst_iterative)]:
        print(f"Testing {impl_name} Search:")
        passed = 0
        
        for tree_list, target, expected, description in search_cases:
            total_tests += 1
            root = build_tree_from_list(tree_list)
            result = func(root, target)
            
            result_val = result.val if result else None
            
            if result_val == expected:
                status = "PASS"
                passed += 1
                total_passed += 1
                print(f"  [{status}] {description:35s} target={target}, result={result_val}")
            else:
                status = "FAIL"
                print(f"  [{status}] {description:35s}")
                print(f"          Tree: {tree_list}, Target: {target}")
                print(f"          Expected: {expected}, Got: {result_val}")
        
        print(f"  Summary: {passed}/{len(search_cases)} passed\n")
    
    # ============================================================
    # TEST 2: INSERT INTO BST
    # ============================================================
    print("=" * 80)
    print("TEST 2: INSERT INTO BST")
    print("=" * 80)
    print()
    
    insert_cases = [
        # (tree, insert_val, expected_tree, description)
        ([4, 2, 7, 1, 3], 5, [4, 2, 7, 1, 3, 5], "insert in right subtree"),
        ([4, 2, 7], 1, [4, 2, 7, 1], "insert as left child"),
        ([4, 2, 7], 6, [4, 2, 7, None, None, 6], "insert as left child of right"),
        ([5], 3, [5, 3], "insert into single node tree - left"),
        ([5], 7, [5, None, 7], "insert into single node tree - right"),
    ]
    
    for impl_name, func in [("Recursive", insert_bst_recursive), ("Iterative", insert_bst_iterative)]:
        print(f"Testing {impl_name} Insert:")
        passed = 0
        
        for tree_list, val, expected_tree, description in insert_cases:
            total_tests += 1
            root = build_tree_from_list(tree_list)
            result_root = func(root, val)
            result_tree = tree_to_list(result_root)
            
            if result_tree == expected_tree:
                status = "PASS"
                passed += 1
                total_passed += 1
                print(f"  [{status}] {description:40s} → {result_tree}")
            else:
                status = "FAIL"
                print(f"  [{status}] {description:40s}")
                print(f"          Original: {tree_list}, Insert: {val}")
                print(f"          Expected: {expected_tree}")
                print(f"          Got: {result_tree}")
        
        print(f"  Summary: {passed}/{len(insert_cases)} passed\n")
    
    # ============================================================
    # TEST 3: VALIDATE BST
    # ============================================================
    print("=" * 80)
    print("TEST 3: VALIDATE BST")
    print("=" * 80)
    print()
    
    validate_cases = [
        # (tree, expected, description)
        ([2, 1, 3], True, "valid simple BST"),
        ([5, 3, 7, 2, 4, 6, 8], True, "valid complete BST"),
        ([5, 1, 4, None, None, 3, 6], False, "invalid - right child too small"),
        ([10, 5, 15, None, None, 6, 20], False, "invalid - subtree value violates range"),
        ([1, 1], False, "invalid - duplicate values"),
        ([5], True, "single node is valid"),
        ([], True, "empty tree is valid"),
        ([2, 1, 3, None, None, None, 4], False, "invalid - right child of right should be > 3"),
    ]
    
    print("Testing BST Validation:")
    passed = 0
    
    for tree_list, expected, description in validate_cases:
        total_tests += 1
        root = build_tree_from_list(tree_list)
        result = is_valid_bst(root)
        
        if result == expected:
            status = "PASS"
            passed += 1
            total_passed += 1
            print(f"  [{status}] {description:45s} tree={tree_list} → {result}")
        else:
            status = "FAIL"
            print(f"  [{status}] {description:45s}")
            print(f"          Tree: {tree_list}")
            print(f"          Expected: {expected}, Got: {result}")
    
    print(f"  Summary: {passed}/{len(validate_cases)} passed\n")
    
    # ============================================================
    # TEST 4: FIND MIN/MAX
    # ============================================================
    print("=" * 80)
    print("TEST 4: FIND MIN/MAX")
    print("=" * 80)
    print()
    
    minmax_cases = [
        # (tree, min, max, description)
        ([4, 2, 7, 1, 3], 1, 7, "balanced tree"),
        ([5, 3, 8, 2, 4, 6, 9], 2, 9, "complete tree"),
        ([1, None, 2, None, 3], 1, 3, "right skewed"),
        ([3, 2, None, 1], 1, 3, "left skewed"),
        ([5], 5, 5, "single node"),
        ([10, 5, 15], 5, 15, "simple three nodes"),
    ]
    
    print("Testing Find Min:")
    passed_min = 0
    for tree_list, expected_min, _, description in minmax_cases:
        total_tests += 1
        root = build_tree_from_list(tree_list)
        result = find_min_bst(root)
        
        if result == expected_min:
            status = "PASS"
            passed_min += 1
            total_passed += 1
            print(f"  [{status}] {description:30s} tree={tree_list} → min={result}")
        else:
            status = "FAIL"
            print(f"  [{status}] {description:30s}")
            print(f"          Tree: {tree_list}")
            print(f"          Expected: {expected_min}, Got: {result}")
    
    print(f"  Summary: {passed_min}/{len(minmax_cases)} passed\n")
    
    print("Testing Find Max:")
    passed_max = 0
    for tree_list, _, expected_max, description in minmax_cases:
        total_tests += 1
        root = build_tree_from_list(tree_list)
        result = find_max_bst(root)
        
        if result == expected_max:
            status = "PASS"
            passed_max += 1
            total_passed += 1
            print(f"  [{status}] {description:30s} tree={tree_list} → max={result}")
        else:
            status = "FAIL"
            print(f"  [{status}] {description:30s}")
            print(f"          Tree: {tree_list}")
            print(f"          Expected: {expected_max}, Got: {result}")
    
    print(f"  Summary: {passed_max}/{len(minmax_cases)} passed\n")
    
    # ============================================================
    # TEST 5: KTH SMALLEST
    # ============================================================
    print("=" * 80)
    print("TEST 5: KTH SMALLEST ELEMENT")
    print("=" * 80)
    print()
    
    kth_cases = [
        # (tree, k, expected, description)
        ([5, 3, 7, 2, 4], 1, 2, "1st smallest (minimum)"),
        ([5, 3, 7, 2, 4], 2, 3, "2nd smallest"),
        ([5, 3, 7, 2, 4], 3, 4, "3rd smallest (middle)"),
        ([5, 3, 7, 2, 4], 4, 5, "4th smallest"),
        ([5, 3, 7, 2, 4], 5, 7, "5th smallest (maximum)"),
        ([3, 1, 4, None, 2], 1, 1, "complex structure - 1st"),
        ([3, 1, 4, None, 2], 3, 3, "complex structure - 3rd"),
        ([1], 1, 1, "single node"),
    ]
    
    print("Testing Kth Smallest:")
    passed = 0
    
    for tree_list, k, expected, description in kth_cases:
        total_tests += 1
        root = build_tree_from_list(tree_list)
        result = kth_smallest(root, k)
        
        if result == expected:
            status = "PASS"
            passed += 1
            total_passed += 1
            print(f"  [{status}] {description:35s} k={k} → {result}")
        else:
            status = "FAIL"
            print(f"  [{status}] {description:35s}")
            print(f"          Tree: {tree_list}, k={k}")
            print(f"          Expected: {expected}, Got: {result}")
    
    print(f"  Summary: {passed}/{len(kth_cases)} passed\n")
    
    # ============================================================
    # FINAL SUMMARY
    # ============================================================
    print("=" * 80)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed")
    print("=" * 80)
    
    return total_passed == total_tests


if __name__ == "__main__":
    all_passed = run_tests()
    sys.exit(0 if all_passed else 1)
