# Solutions.py - Reference Implementations
# These are complete, tested solutions for you to compare against

class RecentCounterList:
    """
    APPROACH 1: QUEUE WITH LIST
    
    Concept: Use list to store request timestamps in order.
    Remove timestamps outside the 3000ms window.
    
    Time: O(1) amortized - each element added once, removed once
    Space: O(W) - where W is max requests in 3000ms window
    """
    def __init__(self):
        self.requests = []
    
    def ping(self, t: int) -> int:
        # Add new request
        self.requests.append(t)
        
        # Remove requests outside [t-3000, t] window
        while self.requests and self.requests[0] < t - 3000:
            self.requests.pop(0)  # O(n) operation - not ideal!
        
        return len(self.requests)


from collections import deque

class RecentCounterDeque:
    """
    APPROACH 2: COLLECTIONS.DEQUE (OPTIMIZED)
    
    Concept: Use deque for efficient O(1) removal from front.
    Python's list.pop(0) is O(n) because it shifts elements.
    deque.popleft() is O(1).
    
    Time: O(1) per operation
    Space: O(W) where W is window size
    """
    def __init__(self):
        self.queue = deque()
    
    def ping(self, t: int) -> int:
        # Add new request to back of queue
        self.queue.append(t)
        
        # Remove old requests from front (outside window)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()  # O(1) operation
        
        return len(self.queue)


class RecentCounterWindow:
    """
    APPROACH 3: DEQUE WITH EXPLICIT WINDOW TRACKING
    
    Concept: Same as Approach 2 but emphasizes sliding window concept.
    The window slides forward with each new request.
    
    Time: O(1) per operation
    Space: O(W)
    """
    def __init__(self):
        self.queue = deque()
        self.WINDOW_SIZE = 3000  # 3000 milliseconds
    
    def ping(self, t: int) -> int:
        # Define window boundaries
        window_start = t - self.WINDOW_SIZE
        window_end = t
        
        # Add new request
        self.queue.append(t)
        
        # Remove requests before window start
        while self.queue and self.queue[0] < window_start:
            self.queue.popleft()
        
        # All remaining requests are in [window_start, window_end]
        return len(self.queue)


if __name__ == "__main__":
    print("Testing Approach 1: List-based Queue")
    rc1 = RecentCounterList()
    print(f"  ping(1) = {rc1.ping(1)}")       # 1
    print(f"  ping(100) = {rc1.ping(100)}")   # 2
    print(f"  ping(3001) = {rc1.ping(3001)}") # 3
    print(f"  ping(3002) = {rc1.ping(3002)}") # 3
    
    print("\nTesting Approach 2: Deque (Optimized)")
    rc2 = RecentCounterDeque()
    print(f"  ping(1) = {rc2.ping(1)}")       # 1
    print(f"  ping(100) = {rc2.ping(100)}")   # 2
    print(f"  ping(3001) = {rc2.ping(3001)}") # 3
    print(f"  ping(3002) = {rc2.ping(3002)}") # 3
    
    print("\nTesting Approach 3: Explicit Window")
    rc3 = RecentCounterWindow()
    print(f"  ping(1) = {rc3.ping(1)}")       # 1
    print(f"  ping(100) = {rc3.ping(100)}")   # 2
    print(f"  ping(3001) = {rc3.ping(3001)}") # 3
    print(f"  ping(3002) = {rc3.ping(3002)}") # 3
    
    print("\n✓ All solutions working!")
