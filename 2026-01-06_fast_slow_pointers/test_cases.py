# Test Cases for Linked List Cycle Detection

from main import has_cycle_hash_set, has_cycle_two_pointers, has_cycle_with_entry, create_linked_list

# Test data: (values, pos, expected_has_cycle, expected_entry_val)
test_cases = [
    # Basic cycles
    ([3, 2, 0, -4], 1, True, 2),           # Cycle starts at node with value 2
    ([1, 2], 0, True, 1),                   # Cycle at head
    ([1], -1, False, None),                 # Single node, no cycle
    ([], -1, False, None),                  # Empty list
    
    # No cycle cases
    ([1, 2, 3, 4], -1, False, None),       # Multiple nodes, no cycle
    ([1, 2], -1, False, None),             # Two nodes, no cycle
    ([5], -1, False, None),                # Single node, no cycle
    
    # Cycles at different positions
    ([1, 2, 3, 4, 5], 2, True, 3),         # Cycle starts at middle
    ([1, 2, 3], 0, True, 1),               # Cycle at head
    ([10, 20, 30, 40], 3, True, 40),       # Cycle to last node (self-loop)
    
    # Edge cases
    ([1, 1], 0, True, 1),                  # Duplicate values with cycle
    ([-1, -2, -3], 1, True, -2),           # Negative values
    ([0], -1, False, None),                # Zero value
]


def run_tests():
    print("Testing has_cycle_hash_set:")
    passed = 0
    for i, (values, pos, expected_cycle, expected_entry_val) in enumerate(test_cases, 1):
        head = create_linked_list(values, pos)
        result = has_cycle_hash_set(head)
        status = "✅" if result == expected_cycle else "❌"
        print(f"  {status} Test {i:2d}: {values} pos={pos:2d} -> {result}")
        if result == expected_cycle:
            passed += 1
    print(f"  Summary: {passed}/{len(test_cases)} passed\n")
    
    print("Testing has_cycle_two_pointers:")
    passed = 0
    for i, (values, pos, expected_cycle, expected_entry_val) in enumerate(test_cases, 1):
        head = create_linked_list(values, pos)
        result = has_cycle_two_pointers(head)
        status = "✅" if result == expected_cycle else "❌"
        print(f"  {status} Test {i:2d}: {values} pos={pos:2d} -> {result}")
        if result == expected_cycle:
            passed += 1
    print(f"  Summary: {passed}/{len(test_cases)} passed\n")
    
    print("Testing has_cycle_with_entry:")
    passed = 0
    for i, (values, pos, expected_cycle, expected_entry_val) in enumerate(test_cases, 1):
        head = create_linked_list(values, pos)
        result = has_cycle_with_entry(head)
        has_cycle, entry_node = result
        entry_val = entry_node.val if entry_node else None
        
        # Check both cycle detection and entry point
        cycle_correct = has_cycle == expected_cycle
        entry_correct = entry_val == expected_entry_val
        all_correct = cycle_correct and entry_correct
        
        status = "✅" if all_correct else "❌"
        print(f"  {status} Test {i:2d}: {values} pos={pos:2d} -> cycle={has_cycle}, entry={entry_val}")
        if all_correct:
            passed += 1
    print(f"  Summary: {passed}/{len(test_cases)} passed\n")
    
    total_tests = len(test_cases) * 3
    total_passed = passed
    print(f"TOTAL: {total_passed} tests need to pass")


if __name__ == "__main__":
    run_tests()
