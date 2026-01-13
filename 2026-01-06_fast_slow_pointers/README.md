# Day 6: Fast & Slow Pointers - Linked List Cycle Detection

**Date:** January 14, 2026  
**Topic:** Fast & Slow Pointers (Floyd's Cycle Detection)  
**Problem:** LeetCode #141 - Linked List Cycle  
**Difficulty:** Easy (Conceptually Medium)

---

## Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter.**

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Example 1:
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

### Example 2:
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

### Example 3:
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

### Constraints:
- The number of nodes in the list is in the range `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked-list

---

## Approach 1: Hash Set (Brute Force)

**Concept:** Track visited nodes in a set. If we revisit a node, there's a cycle.

**Algorithm:**
1. Create a set to store visited nodes
2. Traverse the list
3. For each node:
   - If node is in set → cycle detected
   - Otherwise, add to set
4. If we reach `None` → no cycle

**Complexity:**
- Time: O(n) - visit each node once
- Space: O(n) - store up to n nodes in set

**Pros:** Simple and intuitive  
**Cons:** Uses O(n) extra space

---

## Approach 2: Fast & Slow Pointers (Floyd's Cycle Detection)

**Concept:** Use two pointers moving at different speeds. If there's a cycle, they'll eventually meet.

**Algorithm:**
1. Initialize `slow` and `fast` pointers at head
2. Move `slow` one step at a time
3. Move `fast` two steps at a time
4. If they meet → cycle exists
5. If `fast` reaches `None` → no cycle

**Why it works:**
- If there's a cycle, fast eventually "laps" slow
- Think of it like runners on a circular track
- Fast gains 1 position per iteration, guaranteed to catch slow

**Complexity:**
- Time: O(n) - worst case visits each node once
- Space: O(1) - only two pointers

**Pros:** Optimal space, elegant  
**Cons:** Slightly less intuitive than hash set

---

## Approach 3: Fast & Slow with Cycle Entry Detection

**Concept:** Not only detect the cycle, but also find WHERE the cycle begins.

**Algorithm:**
1. Phase 1: Detect cycle using fast/slow (same as Approach 2)
2. Phase 2: If cycle found:
   - Reset one pointer to head
   - Move both one step at a time
   - Where they meet is the cycle entry point

**Mathematical Proof:**
- Let distance to cycle entry = `a`
- Let distance from entry to meeting point = `b`
- When slow enters cycle, fast is `b` steps ahead
- They meet after slow travels `b` more steps
- Moving slow back to head and advancing both → meet at entry

**Complexity:**
- Time: O(n)
- Space: O(1)

**Pros:** Provides additional information (cycle entry)  
**Cons:** More complex, overkill for simple detection

---

## Key Learnings

1. **Fast/Slow Pattern:** Core technique for linked list problems (cycle detection, middle finding, palindrome check)
2. **Space-Time Tradeoff:** Hash set is O(n) space but simpler; two pointers is O(1) space but requires understanding
3. **Floyd's Algorithm:** A classic CS algorithm worth memorizing
4. **When to Use:**
   - Any linked list cycle problem
   - Finding middle of linked list
   - Checking for palindromes in linked lists
   - Detecting duplicates in arrays (with index jumping)

---

## Common Mistakes

1. **Not checking for null:** Always check `fast and fast.next` before moving
2. **Off-by-one in initialization:** Both pointers should start at head
3. **Wrong movement pattern:** Slow moves 1, fast moves 2 (not 3!)
4. **Forgetting edge cases:** Empty list, single node, two nodes

---

## Follow-up Variations

- **LeetCode #142:** Linked List Cycle II (find entry point)
- **LeetCode #876:** Middle of Linked List
- **LeetCode #234:** Palindrome Linked List
- **LeetCode #287:** Find Duplicate Number (uses cycle detection on array indices)

---

## Visual Trace Example

```
List: 1 → 2 → 3 → 4 → 5
              ↑_______|

Initial:     slow=1, fast=1
Iteration 1: slow=2, fast=3
Iteration 2: slow=3, fast=5
Iteration 3: slow=4, fast=4  ← MEET! Cycle detected
```
