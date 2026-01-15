# Main.py - Your Working File
# Task: Solve LeetCode #141: Linked List Cycle
# Goal: Write 3 progressive approaches

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TODO 1: Approach 1 - Hash Set (Brute Force)
# - Use a set to track visited nodes
# - If we see a node twice → cycle exists
# - If we reach None → no cycle
# - Time: O(n), Space: O(n)

def has_cycle_hash_set(head):
    """
    APPROACH 1: HASH SET
    """
    if not head:
        return False
    
    visited = set()
    current = head

    while current :
        # print("current:", current.val)
        if current in visited:
            return True
        
        visited.add(current)
        current = current.next
        # print("next:", current.next.val)
        # print("visited size:", visited)

    return False


# TODO 2: Approach 2 - Fast & Slow Pointers (Optimal)
# - Initialize slow and fast pointers at head
# - Move slow by 1 step, fast by 2 steps
# - If they meet → cycle exists
# - If fast reaches None → no cycle
# - Time: O(n), Space: O(1)
# - This is Floyd's Cycle Detection Algorithm

def has_cycle_two_pointers(head):
    """
    APPROACH 2: FAST & SLOW POINTERS (FLOYD'S ALGORITHM)
    """
    if not head or not head.next:
        return False
    
    slow = head 
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False


# TODO 3: Approach 3 - Fast & Slow with Cycle Entry Detection
# - Phase 1: Detect cycle using fast/slow
# - Phase 2: Find cycle entry point
#   - Reset one pointer to head
#   - Move both one step at a time
#   - Where they meet is the cycle start
# - Time: O(n), Space: O(1)
# - Returns: (has_cycle: bool, entry_node: ListNode or None)

def has_cycle_with_entry(head):
    """
    APPROACH 3: FAST & SLOW WITH CYCLE ENTRY DETECTION
    Returns (has_cycle, entry_node)
    """
    if not head or not head.next:
        return(False, None)

    slow = head
    fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return (False, None)

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return (True, slow)   


# Helper function to create a linked list with optional cycle
def create_linked_list(values, pos=-1):
    """
    Creates a linked list from values with optional cycle at position pos.
    pos = -1 means no cycle.
    """
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    
    # Link nodes
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Create cycle if pos is valid
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    
    return nodes[0]


if __name__ == "__main__":
    # Smoke tests
    # Test 1: Cycle at position 1
    head1 = create_linked_list([3, 2, 0, -4], pos=1)
    assert has_cycle_hash_set(head1) == True
    assert has_cycle_two_pointers(head1) == True
    # exit()
    result1 = has_cycle_with_entry(head1)
    assert result1[0] == True  # has cycle
    assert result1[1].val == 2  # cycle starts at node with value 2
    
    # Test 2: Cycle at position 0
    head2 = create_linked_list([1, 2], pos=0)
    assert has_cycle_hash_set(head2) == True
    assert has_cycle_two_pointers(head2) == True
    result2 = has_cycle_with_entry(head2)
    assert result2[0] == True
    assert result2[1].val == 1
    
    # Test 3: No cycle
    head3 = create_linked_list([1], pos=-1)
    assert has_cycle_hash_set(head3) == False
    assert has_cycle_two_pointers(head3) == False
    result3 = has_cycle_with_entry(head3)
    assert result3[0] == False
    assert result3[1] is None
    
    # Test 4: Empty list
    head4 = create_linked_list([], pos=-1)
    assert has_cycle_hash_set(head4) == False
    assert has_cycle_two_pointers(head4) == False
    result4 = has_cycle_with_entry(head4)
    assert result4[0] == False
    assert result4[1] is None
    
    # Test 5: No cycle, multiple nodes
    head5 = create_linked_list([1, 2, 3, 4], pos=-1)
    assert has_cycle_hash_set(head5) == False
    assert has_cycle_two_pointers(head5) == False
    result5 = has_cycle_with_entry(head5)
    assert result5[0] == False
    assert result5[1] is None
    
    print("Quick checks passed. Run test_cases.py for more.")
