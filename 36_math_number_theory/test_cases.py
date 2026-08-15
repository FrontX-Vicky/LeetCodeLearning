import unittest
from main import countPrimes, mySqrt

class TestMath(unittest.TestCase):
    def test_countPrimes(self):
        self.assertEqual(countPrimes(10), 4) # 2, 3, 5, 7
        self.assertEqual(countPrimes(0), 0)
        self.assertEqual(countPrimes(1), 0)
        self.assertEqual(countPrimes(2), 0) # strictly less than 2
        self.assertEqual(countPrimes(3), 1) # 2

    def test_mySqrt(self):
        self.assertEqual(mySqrt(4), 2)
        self.assertEqual(mySqrt(8), 2)
        self.assertEqual(mySqrt(0), 0)
        self.assertEqual(mySqrt(1), 1)
        self.assertEqual(mySqrt(2), 1)
        self.assertEqual(mySqrt(2147395599), 46339)

if __name__ == '__main__':
    unittest.main()
