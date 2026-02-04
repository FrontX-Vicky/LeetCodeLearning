# Solutions.py - Reference Implementations
# Day 17: Heap & Priority Queue

import heapq
from typing import List, Optional


# Definition for singly-linked list
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
    
    APPROACH 1: Min Heap of Size K (Optimal)
    
    VISUALIZATION:
    nums = [3,2,1,5,6,4], k = 2
    
    Want 2nd largest:
    Sorted: [6,5,4,3,2,1]
              ^
              2nd largest = 5
    
    ALGORITHM:
    Keep min heap of size k with k largest elements
    Heap top = kth largest
    
    Step-by-step:
    heap = []
    
    Process 3: heap = [3]
    Process 2: heap = [2, 3]
    Process 1: heap = [1, 2, 3] → size > k, pop 1 → [2, 3]
    Process 5: heap = [2, 3, 5] → size > k, pop 2 → [3, 5]
    Process 6: heap = [3, 5, 6] → size > k, pop 3 → [5, 6]
    Process 4: heap = [4, 5, 6] → size > k, pop 4 → [5, 6]
    
    Final heap: [5, 6]
    Min of heap (heap[0]) = 5 = 2nd largest ✓
    
    WHY IT WORKS:
    - Min heap keeps smallest element at top
    - By limiting size to k, we keep k largest elements
    - Smallest of k largest = kth largest!
    
    Time: O(n log k)
    Space: O(k)
    """
    # Build min heap of first k elements
    heap = nums[:k]
    heapq.heapify(heap)
    
    # Process remaining elements
    for num in nums[k:]:
        if num > heap[0]:  # If larger than smallest in heap
            heapq.heapreplace(heap, num)  # Replace and heapify
    
    return heap[0]  # Kth largest is at top


def find_kth_largest_approach2(nums: List[int], k: int) -> int:
    """
    APPROACH 2: Max Heap (Simpler but more space)
    
    - Build max heap from all elements
    - Pop k times
    - Last popped = kth largest
    
    Time: O(n + k log n)
    Space: O(n)
    """
    # Python heapq is min heap, negate for max heap
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)
    
    # Pop k times
    for _ in range(k - 1):
        heapq.heappop(max_heap)
    
    return -heapq.heappop(max_heap)


# ============================================================
# PROBLEM 2: TOP K FREQUENT ELEMENTS
# ============================================================

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Return k most frequent elements.
    
    VISUALIZATION:
    nums = [1,1,1,2,2,3], k = 2
    
    STEP 1: Count frequencies
    {1: 3, 2: 2, 3: 1}
    
    STEP 2: Use min heap of size k with (freq, num)
    
    Process (3, 1): heap = [(3, 1)]
    Process (2, 2): heap = [(2, 2), (3, 1)]
    Process (1, 3): heap = [(1, 3), (3, 1), (2, 2)] → pop (1,3) → [(2, 2), (3, 1)]
    
    STEP 3: Extract numbers from heap
    Result: [2, 1] (or [1, 2], order doesn't matter)
    
    WHY MIN HEAP OF SIZE K:
    - Keep k most frequent elements
    - Pop least frequent when size exceeds k
    - More efficient than sorting all frequencies
    
    Time: O(n log k)
    Space: O(n) for hash map
    """
    # Count frequencies
    from collections import Counter
    count = Counter(nums)
    
    # Use min heap of size k with (frequency, number)
    heap = []
    
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Extract numbers from heap
    return [num for freq, num in heap]


def top_k_frequent_approach2(nums: List[int], k: int) -> List[int]:
    """
    APPROACH 2: Using heapq.nlargest (Cleaner)
    
    Time: O(n log k)
    Space: O(n)
    """
    from collections import Counter
    count = Counter(nums)
    
    # Get k elements with largest frequencies
    return heapq.nlargest(k, count.keys(), key=count.get)


# ============================================================
# PROBLEM 3: MERGE K SORTED LISTS
# ============================================================

def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists into one sorted list.
    
    VISUALIZATION:
    lists = [
        1 → 4 → 5
        1 → 3 → 4
        2 → 6
    ]
    
    ALGORITHM: Min heap with (value, list_index, node)
    
    INITIAL HEAP:
    Push first node from each list:
    [(1, 0, node1), (1, 1, node1'), (2, 2, node2)]
    
    ITERATION 1:
    Pop (1, 0, node1) → add to result → push node1.next (4)
    Heap: [(1, 1, node1'), (2, 2, node2), (4, 0, node4)]
    Result: 1 →
    
    ITERATION 2:
    Pop (1, 1, node1') → add to result → push node1'.next (3)
    Heap: [(2, 2, node2), (3, 1, node3), (4, 0, node4)]
    Result: 1 → 1 →
    
    ITERATION 3:
    Pop (2, 2, node2) → add to result → push node2.next (6)
    Heap: [(3, 1, node3), (4, 0, node4), (6, 2, node6)]
    Result: 1 → 1 → 2 →
    
    ... continue until heap empty
    
    Final: 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
    
    WHY HEAP:
    - Always get minimum among all list heads
    - Efficiently select next smallest element
    - Better than comparing all k lists repeatedly
    
    Time: O(N log k) where N = total nodes, k = number of lists
    Space: O(k) for heap
    """
    heap = []
    
    # Initialize heap with first node from each list
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))
    
    # Dummy head for result
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        
        # Add to result
        current.next = node
        current = current.next
        
        # Push next node from same list
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next


# ============================================================
# PROBLEM 4: MEDIAN FINDER (DATA STREAM)
# ============================================================

class MedianFinder:
    """
    Find median from a data stream.
    
    APPROACH: Two Heaps
    
    VISUALIZATION:
    
    Stream: [1, 2, 3, 4, 5]
    
    TWO HEAP STRUCTURE:
    ┌─────────────┬─────────────┐
    │  Max Heap   │  Min Heap   │
    │  (left)     │  (right)    │
    │  smaller    │  larger     │
    │  values     │  values     │
    └─────────────┴─────────────┘
    
    INVARIANTS:
    1. All elements in left ≤ all elements in right
    2. |left| = |right| OR |left| = |right| + 1
    
    EXAMPLE:
    
    Add 1: left = [1], right = []
           Median = 1
    
    Add 2: left = [1], right = [2]
           Median = (1 + 2) / 2 = 1.5
    
    Add 3: left = [1, 2], right = [3]
           Median = 2 (middle of left)
    
    Add 4: left = [1, 2], right = [3, 4]
           Median = (2 + 3) / 2 = 2.5
    
    Add 5: left = [1, 2, 3], right = [4, 5]
           Median = 3
    
    ALGORITHM:
    
    addNum(num):
    1. Add to left (max heap)
    2. Move largest from left to right
    3. Balance: if right larger, move back to left
    
    findMedian():
    - If sizes equal: (max(left) + min(right)) / 2
    - Otherwise: max(left)
    
    Time: addNum O(log n), findMedian O(1)
    Space: O(n)
    """
    
    def __init__(self):
        # Max heap (negate values for Python's min heap)
        self.left = []   # Smaller half
        # Min heap
        self.right = []  # Larger half
    
    def addNum(self, num: int) -> None:
        # Always add to left first (as negative for max heap)
        heapq.heappush(self.left, -num)
        
        # Move largest from left to right (to maintain invariant)
        heapq.heappush(self.right, -heapq.heappop(self.left))
        
        # Balance: if right is larger, move back to left
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))
    
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]  # Negate to get actual value
        else:
            return (-self.left[0] + self.right[0]) / 2.0


# ============================================================
# PROBLEM 5: LAST STONE WEIGHT
# ============================================================

def last_stone_weight(stones: List[int]) -> int:
    """
    Simulate stone smashing game.
    
    VISUALIZATION:
    stones = [2,7,4,1,8,1]
    
    Max heap: [-8, -7, -4, -2, -1, -1]  (negated)
    
    ROUND 1: Smash 8 and 7
    Pop -8, -7 → difference = 8-7 = 1
    Push -1 → heap = [-4, -2, -1, -1, -1]
    
    ROUND 2: Smash 4 and 2
    Pop -4, -2 → difference = 4-2 = 2
    Push -2 → heap = [-2, -1, -1, -1]
    
    ROUND 3: Smash 2 and 1
    Pop -2, -1 → difference = 2-1 = 1
    Push -1 → heap = [-1, -1, -1]
    
    ROUND 4: Smash 1 and 1
    Pop -1, -1 → difference = 1-1 = 0
    Don't push → heap = [-1]
    
    RESULT: 1 stone left with weight 1
    
    Time: O(n log n)
    Space: O(n)
    """
    # Create max heap (negate values)
    heap = [-stone for stone in stones]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        # Get two heaviest stones
        first = -heapq.heappop(heap)   # Heaviest
        second = -heapq.heappop(heap)  # Second heaviest
        
        # If different, push difference back
        if first != second:
            heapq.heappush(heap, -(first - second))
    
    # Return last stone weight, or 0 if none left
    return -heap[0] if heap else 0


# ============================================================
# PROBLEM 6: K CLOSEST POINTS TO ORIGIN
# ============================================================

def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Find k closest points to origin (0, 0).
    
    APPROACH 1: Min Heap with All Points
    
    VISUALIZATION:
    points = [[1,3], [-2,2], [5,8], [0,1]], k = 2
    
    Calculate distances (x² + y²):
    [1,3]: 1² + 3² = 10
    [-2,2]: 4 + 4 = 8
    [5,8]: 25 + 64 = 89
    [0,1]: 0 + 1 = 1
    
    Build heap: [(1, [0,1]), (8, [-2,2]), (10, [1,3]), (89, [5,8])]
    
    Pop k=2 times:
    1st: (1, [0,1])
    2nd: (8, [-2,2])
    
    Result: [[0,1], [-2,2]]
    
    Time: O(n log n)
    Space: O(n)
    """
    # Build heap with (distance, point)
    heap = []
    for point in points:
        x, y = point
        dist = x * x + y * y  # No need for sqrt
        heapq.heappush(heap, (dist, point))
    
    # Extract k closest
    result = []
    for _ in range(k):
        dist, point = heapq.heappop(heap)
        result.append(point)
    
    return result


def k_closest_approach2(points: List[List[int]], k: int) -> List[List[int]]:
    """
    APPROACH 2: Max Heap of Size K (More Efficient)
    
    Keep only k closest points in heap.
    Use max heap so we can remove farthest point when needed.
    
    Time: O(n log k)
    Space: O(k)
    """
    heap = []
    
    for point in points:
        x, y = point
        dist = -(x * x + y * y)  # Negate for max heap
        
        if len(heap) < k:
            heapq.heappush(heap, (dist, point))
        elif dist > heap[0][0]:  # If closer than farthest in heap
            heapq.heapreplace(heap, (dist, point))
    
    return [point for dist, point in heap]


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
