# Day 10: Linked List Manipulation - Reverse Linked List

**Date:** January 24, 2026  
**Topic:** Linked List Reversal (Pointer Manipulation)  
**Problem:** LeetCode #206 - Reverse Linked List  
**Difficulty:** Easy

---

## Problem Statement

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

### Example 1:
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Visual:
Before: 1 → 2 → 3 → 4 → 5 → None
After:  5 → 4 → 3 → 2 → 1 → None
```

### Example 2:
```
Input: head = [1,2]
Output: [2,1]
```

### Example 3:
```
Input: head = []
Output: []
```

### Constraints:
- The number of nodes in the list is in the range `[0, 5000]`
- `-5000 <= Node.val <= 5000`

### Follow-up:
A linked list can be reversed either iteratively or recursively. Could you implement both?

---

## Approach 1: Iterative (3-Pointer)

**Concept:** Use three pointers to reverse links one by one as we traverse.

**Algorithm:**
1. Initialize three pointers: `prev = None`, `curr = head`, `next = None`
2. While `curr` is not None:
   - Save next node: `next = curr.next`
   - Reverse link: `curr.next = prev`
   - Move pointers forward: `prev = curr`, `curr = next`
3. Return `prev` (new head)

**Why It Works:**
- We reverse each arrow one at a time
- Need to save `next` before breaking the link
- `prev` becomes the new head after traversal

**Complexity:**
- Time: O(n) - visit each node once
- Space: O(1) - only three pointers

**Pros:** Efficient, no recursion overhead  
**Cons:** Pointer juggling can be tricky

---

## Approach 2: Recursive

**Concept:** Recursively reverse from the end, building reversed list from tail.

**Algorithm:**
1. Base case: if `head` is None or only one node, return head
2. Recursively reverse rest of list
3. Reverse current node's link
4. Set `head.next = None` to avoid cycle
5. Return new head

**Why It Works:**
- Recursion goes to end of list first
- Unwinds back, reversing each link
- Last node becomes new head

**Complexity:**
- Time: O(n) - visit each node once
- Space: O(n) - recursion call stack

**Pros:** Elegant, easier to understand  
**Cons:** Stack space overhead, risk of stack overflow

---

## Approach 3: Stack-Based

**Concept:** Push all nodes onto stack, pop to build reversed list.

**Algorithm:**
1. Push all nodes onto stack
2. Pop nodes one by one, building new list
3. Set last node's next to None

**Complexity:**
- Time: O(n)
- Space: O(n) - stack storage

**Pros:** Straightforward logic  
**Cons:** Extra space, not in-place

---

## Key Learnings

1. **Linked List Reversal:**
   - Fundamental operation in linked list manipulation
   - Requires careful pointer management
   - Three-pointer technique is classic pattern

2. **Iterative vs Recursive:**
   - Iterative: O(1) space, faster in practice
   - Recursive: O(n) space, more elegant code
   - Both O(n) time complexity

3. **Pointer Manipulation:**
   - Always save `next` before breaking links
   - Draw diagrams to visualize pointer changes
   - Edge cases: empty list, single node

4. **Common Mistakes:**
   - Losing reference to rest of list
   - Forgetting to set tail's next to None
   - Not returning correct head

---

## Visual Trace: Iterative Approach

**Input:** `1 → 2 → 3 → None`

```
Initial State:
prev = None
curr = 1 → 2 → 3 → None
next = None

═══════════════════════════════════════════════════════════════════════
Step 1: Process node 1
═══════════════════════════════════════════════════════════════════════
next = curr.next        # next = 2
curr.next = prev        # 1 → None
prev = curr             # prev = 1
curr = next             # curr = 2

State:
prev = 1 → None
curr = 2 → 3 → None
next = 2

═══════════════════════════════════════════════════════════════════════
Step 2: Process node 2
═══════════════════════════════════════════════════════════════════════
next = curr.next        # next = 3
curr.next = prev        # 2 → 1 → None
prev = curr             # prev = 2
curr = next             # curr = 3

State:
prev = 2 → 1 → None
curr = 3 → None
next = 3

═══════════════════════════════════════════════════════════════════════
Step 3: Process node 3
═══════════════════════════════════════════════════════════════════════
next = curr.next        # next = None
curr.next = prev        # 3 → 2 → 1 → None
prev = curr             # prev = 3
curr = next             # curr = None

State:
prev = 3 → 2 → 1 → None
curr = None
next = None

═══════════════════════════════════════════════════════════════════════
End: curr is None, return prev
═══════════════════════════════════════════════════════════════════════
Result: 3 → 2 → 1 → None ✓
```

---

## Visual: Pointer Changes

```
Original List:
1 → 2 → 3 → 4 → None

Step 1: Reverse first link
None ← 1    2 → 3 → 4 → None
       ↑    ↑
      prev curr

Step 2: Reverse second link
None ← 1 ← 2    3 → 4 → None
            ↑    ↑
           prev curr

Step 3: Reverse third link
None ← 1 ← 2 ← 3    4 → None
                ↑    ↑
               prev curr

Step 4: Reverse fourth link
None ← 1 ← 2 ← 3 ← 4
                    ↑
                   prev (new head)
```

---

## Common Mistakes

1. **Losing reference to rest of list:**
   ```python
   # ❌ WRONG
   curr.next = prev  # Lost reference to curr.next!
   curr = curr.next  # curr is now prev, not the original next!
   
   # ✅ CORRECT
   next = curr.next  # Save next first
   curr.next = prev
   curr = next       # Use saved reference
   ```

2. **Not handling empty list:**
   ```python
   # ❌ WRONG
   def reverseList(head):
       # Crashes if head is None
       curr = head.next
   
   # ✅ CORRECT
   def reverseList(head):
       if not head:
           return None
   ```

3. **Forgetting to initialize prev as None:**
   ```python
   # ❌ WRONG
   prev = head  # Wrong start, should be None
   
   # ✅ CORRECT
   prev = None  # New tail points to None
   ```

4. **Returning wrong head:**
   ```python
   # ❌ WRONG
   return head  # Still points to original head!
   
   # ✅ CORRECT
   return prev  # Points to new head (was tail)
   ```

---

## Recursive Approach Visualization

```
reverseList(1 → 2 → 3 → None)
    ↓
    reverseList(2 → 3 → None)
        ↓
        reverseList(3 → None)
            ↓
            reverseList(None)  # Base case: return None
            ↑
        # Now reverse: 3 ← None, return 3
        3 → None
        ↑
    # Now reverse: 2 ← 3, return 3
    3 → 2 → None
    ↑
# Now reverse: 1 ← 2, return 3
3 → 2 → 1 → None ✓

Each recursion level reverses ONE link, then passes new head up.
```

---

## Template: Linked List Node

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## Follow-up Variations

- **LeetCode #92:** Reverse Linked List II (reverse between positions)
- **LeetCode #25:** Reverse Nodes in k-Group
- **LeetCode #24:** Swap Nodes in Pairs
- **LeetCode #234:** Palindrome Linked List (uses reversal)

---

## When to Use Linked List Reversal?

✅ **Use When:**
- Reversing entire list or sublist
- Detecting palindromes (reverse half, compare)
- Reordering nodes
- Building other linked list operations

❌ **Don't Use When:**
- Need random access (use array)
- Need to preserve original order
- Space is unlimited (can just copy to new list)

---

## Connection to Previous Days

- **Day 6 (Fast/Slow Pointers):** Both manipulate linked list pointers
- **Day 7 (Stack):** Stack-based reversal uses LIFO (similar to Day 7)
- **Day 9 (Monotonic Stack):** Both require careful state management

**Key Difference:**
- Reversal changes structure (pointers)
- Fast/slow traverses without modification
