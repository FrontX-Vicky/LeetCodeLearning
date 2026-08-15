class MinStack:
    def __init__(self):
        # We store tuples of (value, current_minimum)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            # The new minimum is the min of the new value and the previous minimum
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Map key -> Node
        
        # Dummy head and tail to avoid edge cases when adding/removing nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Remove an existing node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node: Node) -> None:
        """Add a new node right after the head (most recently used)."""
        next_node = self.head.next
        
        self.head.next = node
        node.prev = self.head
        
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move to front (most recently used)
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node value and move to front
            node = self.cache[key]
            self._remove(node)
            node.val = value
            self._add(node)
        else:
            # Add new node
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)
            
            # Evict LRU if capacity exceeded
            if len(self.cache) > self.capacity:
                # The LRU node is right before the tail
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
