import unittest
from main import HardMarathon, MedianFinder

class TestHardMarathon(unittest.TestCase):
    def test_trap(self):
        solution = HardMarathon()
        self.assertEqual(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
        self.assertEqual(solution.trap([4,2,0,3,2,5]), 9)
        self.assertEqual(solution.trap([1]), 0)

    def test_median_finder(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertEqual(mf.findMedian(), 2.0)

if __name__ == '__main__':
    unittest.main()
