# Main.py - Your Working File
# Task: Solve LeetCode #206: Reverse Linked List
# Goal: Reverse a singly linked list (iterative and recursive)

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# TODO 1: Approach 1 - Iterative (3-Pointer)
# - Use prev, curr, next pointers
# - Reverse links one by one
# - Time: O(n), Space: O(1)

def reverse_iterative(head):
    """
    APPROACH 1: ITERATIVE WITH 3 POINTERS
    """
    curr = head
    prev = None

    while curr:
        # save next node before breaking link
        next_node = curr.next

        # reverse the link
        curr.next = prev

        # move pointers forward
        prev = curr
        curr = next_node

    # prev is the new head 
    return prev



# TODO 2: Approach 2 - Recursive
# - Base case: None or single node
# - Recursively reverse rest
# - Reverse current link
# - Time: O(n), Space: O(n) for call stack

def reverse_recursive(head):
    """
    APPROACH 2: RECURSIVE
    """
    # base case : empty node or single node
    if not head or not head.next:
        return head
    
    new_head = reverse_recursive(head.next)

    # reverse the current link
    # head.next is now the last node in reversed part
    # make it point back to head
    head.next.next = head

    # set current nodes next to None (will be updated in previous recursion)
    head.next = None

    # return the new head (doen't change, its the original tail)
    return new_head


# TODO 3: Approach 3 - Stack-Based
# - Push all nodes onto stack
# - Pop to rebuild reversed list
# - Time: O(n), Space: O(n)

def reverse_stack(head):
    """
    APPROACH 3: STACK-BASED
    """
    if not head:
        return None
    
    # push all node onto stack
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next
    
    # pop nodes to build reversed list 
    new_head = stack.pop()
    curr = new_head

    while stack:
        node = stack.pop()
        curr.next = node
        curr = curr.next

    # set last node's next to None
    curr.next = None

    return new_head

# Helper function: Create linked list from array
def create_linked_list(arr):
    """Create a linked list from an array"""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


# Helper function: Convert linked list to array
def linked_list_to_array(head):
    """Convert linked list to array for easy comparison"""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


if __name__ == "__main__":
    # Smoke tests
    
    # Test 1: Basic reversal
    print("Testing Approach 1: Iterative")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = reverse_iterative(head1)
    result1 = linked_list_to_array(reversed1)
    expected = [5, 4, 3, 2, 1]
    assert result1 == expected, f"Expected {expected}, got {result1}"
    print(f"  Input:  [1, 2, 3, 4, 5]")
    print(f"  Output: {result1}")
    print("  ✓ Passed!")
    
    # Test 2: Recursive
    print("\nTesting Approach 2: Recursive")
    head2 = create_linked_list([1, 2, 3, 4, 5])
    reversed2 = reverse_recursive(head2)
    result2 = linked_list_to_array(reversed2)
    assert result2 == expected, f"Expected {expected}, got {result2}"
    print(f"  Input:  [1, 2, 3, 4, 5]")
    print(f"  Output: {result2}")
    print("  ✓ Passed!")
    
    # Test 3: Stack-based
    print("\nTesting Approach 3: Stack-Based")
    head3 = create_linked_list([1, 2, 3, 4, 5])
    reversed3 = reverse_stack(head3)
    result3 = linked_list_to_array(reversed3)
    assert result3 == expected, f"Expected {expected}, got {result3}"
    print(f"  Input:  [1, 2, 3, 4, 5]")
    print(f"  Output: {result3}")
    print("  ✓ Passed!")
    
    # Test edge cases
    assert linked_list_to_array(reverse_iterative(None)) == []
    assert linked_list_to_array(reverse_recursive(None)) == []
    assert linked_list_to_array(reverse_stack(None)) == []
    
    assert linked_list_to_array(reverse_iterative(create_linked_list([1]))) == [1]
    assert linked_list_to_array(reverse_recursive(create_linked_list([1]))) == [1]
    assert linked_list_to_array(reverse_stack(create_linked_list([1]))) == [1]
    
    print("\nAll smoke tests passed! Run test_cases.py for comprehensive tests.")
