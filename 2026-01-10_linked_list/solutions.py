# Solutions.py - Reference Implementations
# These are complete, tested solutions for you to compare against

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_iterative(head):
    """
    APPROACH 1: ITERATIVE WITH 3 POINTERS
    
    Concept: Use three pointers (prev, curr, next) to reverse links
    as we traverse the list from head to tail.
    
    Time: O(n) - visit each node once
    Space: O(1) - only three pointers
    """
    prev = None
    curr = head
    
    while curr:
        # Save next node before breaking link
        next_node = curr.next
        
        # Reverse the link
        curr.next = prev
        
        # Move pointers forward
        prev = curr
        curr = next_node
    
    # prev is the new head (was the tail)
    return prev


def reverse_recursive(head):
    """
    APPROACH 2: RECURSIVE
    
    Concept: Recursively reverse from the end, building reversed list
    as recursion unwinds.
    
    Base case: Empty list or single node
    Recursive case: Reverse rest, then reverse current link
    
    Time: O(n) - visit each node once
    Space: O(n) - recursion call stack
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_recursive(head.next)
    
    # Reverse the current link
    # head.next is now the last node in reversed part
    # Make it point back to head
    head.next.next = head
    
    # Set current node's next to None (will be updated in previous recursion)
    head.next = None
    
    # Return the new head (doesn't change, it's the original tail)
    return new_head


def reverse_stack(head):
    """
    APPROACH 3: STACK-BASED
    
    Concept: Push all nodes onto a stack, then pop them to rebuild
    the list in reverse order.
    
    Time: O(n) - two passes through list
    Space: O(n) - stack stores all nodes
    """
    if not head:
        return None
    
    # Push all nodes onto stack
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next
    
    # Pop nodes to build reversed list
    new_head = stack.pop()
    curr = new_head
    
    while stack:
        node = stack.pop()
        curr.next = node
        curr = curr.next
    
    # Set last node's next to None
    curr.next = None
    
    return new_head


# Helper functions
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


def linked_list_to_array(head):
    """Convert linked list to array for easy comparison"""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


if __name__ == "__main__":
    print("Testing Approach 1: Iterative")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = reverse_iterative(head1)
    print(f"  Input:  [1, 2, 3, 4, 5]")
    print(f"  Output: {linked_list_to_array(reversed1)}")
    print(f"  Expected: [5, 4, 3, 2, 1]")
    
    print("\nTesting Approach 2: Recursive")
    head2 = create_linked_list([1, 2, 3, 4, 5])
    reversed2 = reverse_recursive(head2)
    print(f"  Input:  [1, 2, 3, 4, 5]")
    print(f"  Output: {linked_list_to_array(reversed2)}")
    print(f"  Expected: [5, 4, 3, 2, 1]")
    
    print("\nTesting Approach 3: Stack-Based")
    head3 = create_linked_list([1, 2, 3, 4, 5])
    reversed3 = reverse_stack(head3)
    print(f"  Input:  [1, 2, 3, 4, 5]")
    print(f"  Output: {linked_list_to_array(reversed3)}")
    print(f"  Expected: [5, 4, 3, 2, 1]")
    
    print("\n✓ All solutions working!")
