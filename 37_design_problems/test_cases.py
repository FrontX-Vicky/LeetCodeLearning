import unittest
from main import MinStack, LRUCache

class TestDesign(unittest.TestCase):
    def test_min_stack(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(minStack.getMin(), -3)
        minStack.pop()
        self.assertEqual(minStack.top(), 0)
        self.assertEqual(minStack.getMin(), -2)

    def test_lru_cache(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        self.assertEqual(lRUCache.get(1), 1)    # return 1
        lRUCache.put(3, 3)                      # evicts key 2
        self.assertEqual(lRUCache.get(2), -1)   # returns -1 (not found)
        lRUCache.put(4, 4)                      # evicts key 1
        self.assertEqual(lRUCache.get(1), -1)   # return -1 (not found)
        self.assertEqual(lRUCache.get(3), 3)    # return 3
        self.assertEqual(lRUCache.get(4), 4)    # return 4

if __name__ == '__main__':
    unittest.main()
