# Main.py - Your Working File
# Task: Solve LeetCode #933: Number of Recent Calls
# Goal: Implement RecentCounter using Queue (FIFO)

# TODO 1: Approach 1 - Queue with List
# - Use list to store timestamps
# - On ping: append new timestamp, remove old ones
# - Return length of list
# - Time: O(1) amortized, Space: O(W) where W is window size

class RecentCounterList:
    """
    APPROACH 1: QUEUE WITH LIST
    """
    def __init__(self):
        pass
    
    def ping(self, t: int) -> int:
        pass


# TODO 2: Approach 2 - Collections.deque (Optimized)
# - Use deque for O(1) popleft()
# - On ping: append to right, popleft() old timestamps
# - Return len(deque)
# - Time: O(1) per operation, Space: O(W)

from collections import deque

class RecentCounterDeque:
    """
    APPROACH 2: COLLECTIONS.DEQUE (OPTIMIZED)
    """
    def __init__(self):
        pass
    
    def ping(self, t: int) -> int:
        pass


# TODO 3: Approach 3 - Deque with Explicit Window
# - Same as Approach 2 but with clear window tracking
# - Emphasize sliding window concept
# - Time: O(1), Space: O(W)

class RecentCounterWindow:
    """
    APPROACH 3: DEQUE WITH EXPLICIT WINDOW TRACKING
    """
    def __init__(self):
        pass
    
    def ping(self, t: int) -> int:
        pass


if __name__ == "__main__":
    # Smoke tests
    
    # Test Approach 1: List
    print("Testing RecentCounterList:")
    rc1 = RecentCounterList()
    assert rc1.ping(1) == 1
    assert rc1.ping(100) == 2
    assert rc1.ping(3001) == 3
    assert rc1.ping(3002) == 3
    print("  Basic tests passed!")
    
    # Test Approach 2: Deque
    print("\nTesting RecentCounterDeque:")
    rc2 = RecentCounterDeque()
    assert rc2.ping(1) == 1
    assert rc2.ping(100) == 2
    assert rc2.ping(3001) == 3
    assert rc2.ping(3002) == 3
    print("  Basic tests passed!")
    
    # Test Approach 3: Window
    print("\nTesting RecentCounterWindow:")
    rc3 = RecentCounterWindow()
    assert rc3.ping(1) == 1
    assert rc3.ping(100) == 2
    assert rc3.ping(3001) == 3
    assert rc3.ping(3002) == 3
    print("  Basic tests passed!")
    
    print("\nQuick checks passed. Run test_cases.py for comprehensive tests.")
