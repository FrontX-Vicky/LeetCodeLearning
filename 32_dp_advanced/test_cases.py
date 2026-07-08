import unittest
from main import coinChange, numDecodings

class TestAdvancedDP(unittest.TestCase):
    def test_coinChange(self):
        self.assertEqual(coinChange([1, 5, 10, 25], 36), 3)  # 25+10+1
        self.assertEqual(coinChange([1, 5, 10], 11), 2)       # 10+1
        self.assertEqual(coinChange([2], 3), -1)              # impossible
        self.assertEqual(coinChange([1], 0), 0)               # base case

    def test_numDecodings(self):
        self.assertEqual(numDecodings("12"), 2)   # "AB" or "L"
        self.assertEqual(numDecodings("226"), 3)  # "BZ", "VF", "BBF"
        self.assertEqual(numDecodings("06"), 0)   # leading zero → invalid
        self.assertEqual(numDecodings("10"), 1)   # "J" only

if __name__ == '__main__':
    unittest.main()
