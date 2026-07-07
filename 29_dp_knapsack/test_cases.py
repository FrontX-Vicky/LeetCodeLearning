import unittest
from main import canPartition, findTargetSumWays

class TestKnapsack(unittest.TestCase):

    def test_canPartition(self):
        self.assertEqual(canPartition([1, 5, 11, 5]), True)
        self.assertEqual(canPartition([1, 2, 3, 5]), False)
        self.assertEqual(canPartition([2, 2, 1, 1]), True)
        self.assertEqual(canPartition([1, 2, 5]), False)

    def test_findTargetSumWays(self):
        self.assertEqual(findTargetSumWays([1, 1, 1, 1, 1], 3), 5)
        self.assertEqual(findTargetSumWays([1], 1), 1)
        self.assertEqual(findTargetSumWays([1, 0], 1), 2)

if __name__ == '__main__':
    unittest.main()
