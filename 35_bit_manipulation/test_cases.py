import unittest
from main import singleNumber, hammingWeight

class TestBitManipulation(unittest.TestCase):
    def test_singleNumber(self):
        self.assertEqual(singleNumber([2, 2, 1]), 1)
        self.assertEqual(singleNumber([4, 1, 2, 1, 2]), 4)
        self.assertEqual(singleNumber([1]), 1)

    def test_hammingWeight(self):
        self.assertEqual(hammingWeight(11), 3)   # 1011 → 3 set bits
        self.assertEqual(hammingWeight(128), 1)  # 10000000 → 1 set bit
        self.assertEqual(hammingWeight(2147483645), 30)  # 30 set bits

if __name__ == '__main__':
    unittest.main()
