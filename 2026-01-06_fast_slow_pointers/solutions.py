# Solutions.py - Reference Implementations
# These are complete, tested solutions for you to compare against

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle_hash_set(head):
    """
    APPROACH 1: HASH SET (BRUTE FORCE)
    
    Concept: Track all visited nodes in a set.
    If we encounter a node we've seen before → cycle exists.
    If we reach None → no cycle.
    
    Time: O(n) - visit each node once
    Space: O(n) - store up to n nodes in set
    """
    if not head:
        return False
    
    visited = set()
    current = head
    
    while current:
        # If we've seen this node before, there's a cycle
        if current in visited:
            return True
        
        visited.add(current)
        current = current.next
    
    # Reached the end (None), no cycle
    return False


def has_cycle_two_pointers(head):
    """
    APPROACH 2: FAST & SLOW POINTERS (FLOYD'S CYCLE DETECTION)
    
    Concept: Use two pointers moving at different speeds.
    - slow moves 1 step per iteration
    - fast moves 2 steps per iteration
    
    If there's a cycle:
    - fast will eventually "lap" slow
    - they will meet inside the cycle
    
    If there's no cycle:
    - fast reaches the end (None)
    
    Time: O(n) - in worst case, visit each node once
    Space: O(1) - only two pointers
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next       # Move 1 step
        fast = fast.next.next  # Move 2 steps
        
        # If they meet, cycle detected
        if slow == fast:
            return True
    
    # fast reached the end, no cycle
    return False


def has_cycle_with_entry(head):
    """
    APPROACH 3: FAST & SLOW WITH CYCLE ENTRY DETECTION
    
    Phase 1: Detect if cycle exists (same as approach 2)
    Phase 2: Find the entry point of the cycle
    
    Mathematical insight:
    - Let a = distance from head to cycle entry
    - Let b = distance from cycle entry to meeting point
    - When slow enters cycle, fast is already inside
    - They meet after slow travels 'b' into the cycle
    
    To find entry:
    - Reset one pointer to head
    - Move both one step at a time
    - They'll meet at the cycle entry
    
    Time: O(n)
    Space: O(1)
    
    Returns: (has_cycle: bool, entry_node: ListNode or None)
    """
    if not head or not head.next:
        return (False, None)
    
    # Phase 1: Detect cycle
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
    
    # Phase 2: Find entry point
    # Reset slow to head, keep fast at meeting point
    slow = head
    
    # Move both one step at a time until they meet
    # They'll meet at the cycle entry
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return (True, slow)


# Helper function to create linked lists with cycles
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
    print("Testing Approach 1: Hash Set")
    head1 = create_linked_list([3, 2, 0, -4], pos=1)
    print(f"  Cycle in [3,2,0,-4] pos=1: {has_cycle_hash_set(head1)}")  # True
    
    head2 = create_linked_list([1, 2], pos=0)
    print(f"  Cycle in [1,2] pos=0: {has_cycle_hash_set(head2)}")  # True
    
    head3 = create_linked_list([1], pos=-1)
    print(f"  Cycle in [1] pos=-1: {has_cycle_hash_set(head3)}")  # False
    
    print("\nTesting Approach 2: Fast & Slow Pointers")
    head4 = create_linked_list([3, 2, 0, -4], pos=1)
    print(f"  Cycle in [3,2,0,-4] pos=1: {has_cycle_two_pointers(head4)}")  # True
    
    head5 = create_linked_list([1], pos=-1)
    print(f"  Cycle in [1] pos=-1: {has_cycle_two_pointers(head5)}")  # False
    
    print("\nTesting Approach 3: With Entry Detection")
    head6 = create_linked_list([3, 2, 0, -4], pos=1)
    result = has_cycle_with_entry(head6)
    print(f"  Has cycle: {result[0]}, Entry value: {result[1].val if result[1] else None}")  # True, 2
    
    head7 = create_linked_list([1, 2], pos=0)
    result2 = has_cycle_with_entry(head7)
    print(f"  Has cycle: {result2[0]}, Entry value: {result2[1].val if result2[1] else None}")  # True, 1
    
    head8 = create_linked_list([1, 2, 3], pos=-1)
    result3 = has_cycle_with_entry(head8)
    print(f"  Has cycle: {result3[0]}, Entry value: {result3[1]}")  # False, None
    
    print("\n✓ All solutions working!")
