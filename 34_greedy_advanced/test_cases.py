import unittest
from main import canJump, jump

class TestGreedy(unittest.TestCase):
    def test_canJump(self):
        self.assertTrue(canJump([2, 3, 1, 1, 4]))
        self.assertFalse(canJump([3, 2, 1, 0, 4]))
        self.assertTrue(canJump([0]))
        self.assertTrue(canJump([2, 0, 0]))

    def test_jump(self):
        self.assertEqual(jump([2, 3, 1, 1, 4]), 2)
        self.assertEqual(jump([2, 3, 0, 1, 4]), 2)
        self.assertEqual(jump([1, 1, 1, 1]), 3)
        self.assertEqual(jump([0]), 0)

if __name__ == '__main__':
    unittest.main()
