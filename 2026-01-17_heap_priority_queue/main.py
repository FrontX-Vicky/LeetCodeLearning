# Main.py - Your Working File
# Task: Implement Heap & Priority Queue Algorithms
# Goal: Master heap operations and priority queue patterns

import heapq
from typing import List, Optional


# Definition for singly-linked list (for Problem 3)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================
# PROBLEM 1: KTH LARGEST ELEMENT IN ARRAY
# ============================================================

def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Find the kth largest element in an unsorted array.
    
    Example:
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5
    Explanation: 2nd largest is 5
    
    Approach 1: Min heap of size k
    - Keep k largest elements in heap
    - Heap top = kth largest
    
    Time: O(n log k)
    Space: O(k)
    """
    # TODO: Implement kth largest using heap
    pass


# ============================================================
# PROBLEM 2: TOP K FREQUENT ELEMENTS
# ============================================================

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Return k most frequent elements.
    
    Example:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
    Explanation: 1 appears 3 times, 2 appears 2 times
    
    Approach: Hash map frequency + heap
    1. Count frequencies
    2. Use min heap of size k with (freq, num)
    3. Return top k
    
    Time: O(n log k)
    Space: O(n)
    """
    # TODO: Implement top k frequent
    pass


# ============================================================
# PROBLEM 3: MERGE K SORTED LISTS
# ============================================================

def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists into one sorted list.
    
    Example:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    
    Approach: Min heap
    1. Push (val, list_index, node) for each list
    2. Pop min, add to result
    3. Push next node from same list
    
    Note: Python 3.10+ allows tuple comparison by first element only
    Use (val, index, node) format
    
    Time: O(N log k) where N = total nodes, k = number of lists
    Space: O(k) for heap
    """
    # TODO: Implement merge k sorted lists
    pass


# ============================================================
# PROBLEM 4: MEDIAN FINDER (DATA STREAM)
# ============================================================

class MedianFinder:
    """
    Find median from a data stream.
    
    Example:
    MedianFinder mf = new MedianFinder()
    mf.addNum(1)    # [1]
    mf.addNum(2)    # [1, 2]
    mf.findMedian() # 1.5
    mf.addNum(3)    # [1, 2, 3]
    mf.findMedian() # 2.0
    
    Approach: Two heaps
    - Max heap (left half): smaller values
    - Min heap (right half): larger values
    - Keep balanced: |left| - |right| ≤ 1
    
    Median:
    - If sizes equal: (max(left) + min(right)) / 2
    - Otherwise: max(left)
    
    Time: addNum O(log n), findMedian O(1)
    Space: O(n)
    """
    
    def __init__(self):
        """Initialize data structure."""
        # TODO: Initialize two heaps
        pass
    
    def addNum(self, num: int) -> None:
        """Add a number to the data structure."""
        # TODO: Add to appropriate heap and balance
        pass
    
    def findMedian(self) -> float:
        """Return median of all elements."""
        # TODO: Calculate median from heap tops
        pass


# ============================================================
# PROBLEM 5: LAST STONE WEIGHT
# ============================================================

def last_stone_weight(stones: List[int]) -> int:
    """
    Simulate stone smashing game.
    
    Rules:
    - Take two heaviest stones (y ≥ x)
    - If x == y: both destroyed
    - If x < y: stone of weight (y - x) remains
    - Continue until ≤ 1 stone left
    
    Example:
    Input: stones = [2,7,4,1,8,1]
    Process:
    [2,7,4,1,8,1] → smash 8,7 → [2,4,1,1,1]
    [2,4,1,1,1]   → smash 4,2 → [2,1,1,1]
    [2,1,1,1]     → smash 2,1 → [1,1,1]
    [1,1,1]       → smash 1,1 → [1]
    Output: 1
    
    Approach: Max heap
    - Python heapq is min heap, so negate values
    - Pop two, push difference if needed
    
    Time: O(n log n)
    Space: O(n)
    """
    # TODO: Implement stone smashing
    pass


# ============================================================
# PROBLEM 6: K CLOSEST POINTS TO ORIGIN
# ============================================================

def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Find k closest points to origin (0, 0).
    
    Distance = sqrt(x² + y²)
    (Can use x² + y² without sqrt for comparison)
    
    Example:
    Input: points = [[1,3],[-2,2]], k = 1
    Distances: 
    [1,3]: sqrt(1² + 3²) = sqrt(10) ≈ 3.16
    [-2,2]: sqrt(4 + 4) = sqrt(8) ≈ 2.83
    Output: [[-2,2]]
    
    Approach 1: Min heap with all distances
    - Push (distance, point) for all
    - Pop k times
    
    Approach 2: Max heap of size k (more efficient)
    - Keep k closest
    - Heap top = kth closest
    
    Time: O(n log k)
    Space: O(k)
    """
    # TODO: Implement k closest points
    pass


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    """Helper: Convert list to linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper: Convert linked list to list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    print("=" * 60)
    print("HEAP & PRIORITY QUEUE - SMOKE TEST")
    print("=" * 60)
    
    # Test 1: Kth Largest
    print("\n" + "-" * 60)
    print("PROBLEM 1: KTH LARGEST ELEMENT")
    print("-" * 60)
    result = find_kth_largest([3, 2, 1, 5, 6, 4], 2)
    print(f"Kth largest in [3,2,1,5,6,4], k=2: {result}")
    print(f"Expected: 5")
    
    # Test 2: Top K Frequent
    print("\n" + "-" * 60)
    print("PROBLEM 2: TOP K FREQUENT ELEMENTS")
    print("-" * 60)
    result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    print(f"Top 2 frequent in [1,1,1,2,2,3]: {result}")
    print(f"Expected: [1, 2] (any order)")
    
    # Test 3: Merge K Lists
    print("\n" + "-" * 60)
    print("PROBLEM 3: MERGE K SORTED LISTS")
    print("-" * 60)
    lists = [
        list_to_linked_list([1, 4, 5]),
        list_to_linked_list([1, 3, 4]),
        list_to_linked_list([2, 6])
    ]
    merged = merge_k_lists(lists)
    result = linked_list_to_list(merged)
    print(f"Merged lists: {result}")
    print(f"Expected: [1, 1, 2, 3, 4, 4, 5, 6]")
    
    # Test 4: Median Finder
    print("\n" + "-" * 60)
    print("PROBLEM 4: FIND MEDIAN FROM DATA STREAM")
    print("-" * 60)
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(f"After adding [1, 2], median: {mf.findMedian()}")
    print(f"Expected: 1.5")
    mf.addNum(3)
    print(f"After adding 3, median: {mf.findMedian()}")
    print(f"Expected: 2.0")
    
    # Test 5: Last Stone Weight
    print("\n" + "-" * 60)
    print("PROBLEM 5: LAST STONE WEIGHT")
    print("-" * 60)
    result = last_stone_weight([2, 7, 4, 1, 8, 1])
    print(f"Last stone weight: {result}")
    print(f"Expected: 1")
    
    # Test 6: K Closest Points
    print("\n" + "-" * 60)
    print("PROBLEM 6: K CLOSEST POINTS TO ORIGIN")
    print("-" * 60)
    result = k_closest([[1, 3], [-2, 2]], 1)
    print(f"1 closest point: {result}")
    print(f"Expected: [[-2, 2]]")
    
    print("\n" + "=" * 60)
    print("Run 'python test_cases.py' for full test suite!")
    print("=" * 60)
