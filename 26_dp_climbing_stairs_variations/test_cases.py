import unittest
from main import tribonacci, numDecodings

class TestClimbingStairsVariations(unittest.TestCase):

    def test_tribonacci(self):
        self.assertEqual(tribonacci(4), 4)
        self.assertEqual(tribonacci(25), 1389537)
        self.assertEqual(tribonacci(0), 0)
        self.assertEqual(tribonacci(1), 1)

    def test_numDecodings(self):
        self.assertEqual(numDecodings("12"), 2)
        self.assertEqual(numDecodings("226"), 3)
        self.assertEqual(numDecodings("06"), 0)
        self.assertEqual(numDecodings("10"), 1)
        self.assertEqual(numDecodings("27"), 1)
        self.assertEqual(numDecodings("111111111111111111111111111111111111111111111"), 1836311903) # Large test case

if __name__ == '__main__':
    unittest.main()
