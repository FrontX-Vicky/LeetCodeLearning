import unittest
from main import fib, climbStairs, minCostClimbingStairs

class TestDPIntroduction(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(10), 55)

    def test_climbStairs(self):
        self.assertEqual(climbStairs(2), 2)
        self.assertEqual(climbStairs(3), 3)
        self.assertEqual(climbStairs(5), 8)
        self.assertEqual(climbStairs(1), 1)

    def test_minCostClimbingStairs(self):
        self.assertEqual(minCostClimbingStairs([10, 15, 20]), 15)
        self.assertEqual(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
        self.assertEqual(minCostClimbingStairs([0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
