# Test Cases for Binary Tree Traversals
import sys

# Import from main.py
from main import (
    TreeNode,
    preorder_recursive,
    preorder_iterative,
    inorder_recursive,
    inorder_iterative,
    postorder_recursive,
    postorder_iterative,
    build_tree_from_list
)

def run_tests():
    """Comprehensive test suite for tree traversals"""
    
    # Test cases: (tree_list, preorder, inorder, postorder, description)
    test_cases = [
        # Basic cases
        ([], [], [], [], "empty tree"),
        ([1], [1], [1], [1], "single node"),
        ([1, 2], [1, 2], [2, 1], [2, 1], "root with left child only"),
        ([1, None, 2], [1, 2], [1, 2], [2, 1], "root with right child only"),
        
        # Two-level trees
        ([1, 2, 3], [1, 2, 3], [2, 1, 3], [2, 3, 1], "complete 2-level tree"),
        ([1, 2, 3, 4], [1, 2, 4, 3], [4, 2, 1, 3], [4, 2, 3, 1], "left subtree has child"),
        ([1, 2, 3, None, None, 5], [1, 2, 3, 5], [2, 1, 5, 3], [2, 5, 3, 1], "right subtree has child"),
        
        # Three-level trees
        ([1, 2, 3, 4, 5], [1, 2, 4, 5, 3], [4, 2, 5, 1, 3], [4, 5, 2, 3, 1], "classic example"),
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7], [4, 5, 2, 6, 7, 3, 1], "complete binary tree"),
        
        # Skewed trees (worst case for balance)
        ([1, 2, None, 3, None, 4], [1, 2, 3, 4], [4, 3, 2, 1], [4, 3, 2, 1], "left skewed"),
        ([1, None, 2, None, 3], [1, 2, 3], [1, 2, 3], [3, 2, 1], "right skewed"),
        
        # Different values
        ([5, 3, 7, 2, 4, 6, 8], [5, 3, 2, 4, 7, 6, 8], [2, 3, 4, 5, 6, 7, 8], [2, 4, 3, 6, 8, 7, 5], "BST structure"),
        ([10, 5, 15, 3, 7], [10, 5, 3, 7, 15], [3, 5, 7, 10, 15], [3, 7, 5, 15, 10], "another BST"),
        
        # Negative values
        ([-1, -2, -3], [-1, -2, -3], [-2, -1, -3], [-2, -3, -1], "negative values"),
        ([0, -1, 1], [0, -1, 1], [-1, 0, 1], [-1, 1, 0], "mixed with zero"),
        
        # Larger trees
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 
         [1, 2, 4, 8, 9, 5, 3, 6, 7],
         [8, 4, 9, 2, 5, 1, 6, 3, 7],
         [8, 9, 4, 5, 2, 6, 7, 3, 1],
         "larger complete tree"),
    ]
    
    traversal_approaches = [
        ("Preorder", [
            ("Recursive", preorder_recursive),
            ("Iterative", preorder_iterative)
        ], 1),  # index 1 = preorder expected
        ("Inorder", [
            ("Recursive", inorder_recursive),
            ("Iterative", inorder_iterative)
        ], 2),  # index 2 = inorder expected
        ("Postorder", [
            ("Recursive", postorder_recursive),
            ("Iterative", postorder_iterative)
        ], 3),  # index 3 = postorder expected
    ]
    
    print("=" * 80)
    print("BINARY TREE TRAVERSALS - TEST SUITE")
    print("=" * 80)
    print()
    
    total_passed = 0
    total_tests = 0
    
    for traversal_name, implementations, expected_idx in traversal_approaches:
        print("=" * 80)
        print(f"{traversal_name.upper()} TRAVERSAL")
        print("=" * 80)
        print()
        
        for impl_name, func in implementations:
            print(f"Testing {traversal_name} - {impl_name}:")
            passed = 0
            
            for tree_list, pre_exp, in_exp, post_exp, description in test_cases:
                total_tests += 1
                
                # Select correct expected result based on traversal type
                if expected_idx == 1:
                    expected = pre_exp
                elif expected_idx == 2:
                    expected = in_exp
                else:
                    expected = post_exp
                
                try:
                    root = build_tree_from_list(tree_list)
                    result = func(root)
                    
                    if result == expected:
                        status = "PASS"
                        passed += 1
                        total_passed += 1
                    else:
                        status = "FAIL"
                        print(f"  [{status}] {description:30s}")
                        print(f"          Tree: {tree_list}")
                        print(f"          Expected: {expected}")
                        print(f"          Got: {result}")
                        continue
                    
                    # Show brief summary for passed tests
                    tree_str = str(tree_list) if len(tree_list) <= 7 else f"[{len(tree_list)} nodes]"
                    print(f"  [{status}] {description:30s} tree={tree_str:20s} → {result}")
                    
                except Exception as e:
                    status = "ERROR"
                    print(f"  [{status}] {description:30s}")
                    print(f"          Tree: {tree_list}")
                    print(f"          Exception: {e}")
            
            print(f"  Summary: {passed}/{len(test_cases)} passed")
            print()
    
    print("=" * 80)
    print(f"TOTAL: {total_passed}/{total_tests} tests passed")
    print(f"({len(traversal_approaches)} traversals × 2 implementations × {len(test_cases)} cases)")
    print("=" * 80)
    
    return total_passed == total_tests


if __name__ == "__main__":
    all_passed = run_tests()
    sys.exit(0 if all_passed else 1)
