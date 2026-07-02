import unittest
from main import rob, rob_II

class TestHouseRobber(unittest.TestCase):

    def test_rob(self):
        self.assertEqual(rob([1, 2, 3, 1]), 4)
        self.assertEqual(rob([2, 7, 9, 3, 1]), 12)
        self.assertEqual(rob([0]), 0)
        self.assertEqual(rob([2, 1, 1, 2]), 4)

    def test_rob_II(self):
        self.assertEqual(rob_II([2, 3, 2]), 3)
        self.assertEqual(rob_II([1, 2, 3, 1]), 4)
        self.assertEqual(rob_II([1, 2, 3]), 3)
        self.assertEqual(rob_II([0]), 0)
        self.assertEqual(rob_II([2]), 2)

if __name__ == '__main__':
    unittest.main()
