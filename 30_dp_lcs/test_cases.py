import unittest
from main import longestCommonSubsequence, lengthOfLIS

class TestLCS(unittest.TestCase):
    def test_longestCommonSubsequence(self):
        self.assertEqual(longestCommonSubsequence("abcde", "ace"), 3)
        self.assertEqual(longestCommonSubsequence("abc", "abc"), 3)
        self.assertEqual(longestCommonSubsequence("abc", "def"), 0)
        self.assertEqual(longestCommonSubsequence("bsbininm", "jmjkbkjkv"), 1)

    def test_lengthOfLIS(self):
        self.assertEqual(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)
        self.assertEqual(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1)

if __name__ == '__main__':
    unittest.main()
