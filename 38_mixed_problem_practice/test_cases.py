import unittest
from main import MixedPractice

class TestMixedPractice(unittest.TestCase):
    def setUp(self):
        self.solution = MixedPractice()

    def test_num_islands(self):
        grid1 = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid1), 1)

        grid2 = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid2), 3)

    def test_three_sum(self):
        self.assertEqual(sorted(self.solution.threeSum([-1,0,1,2,-1,-4])), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(self.solution.threeSum([0,1,1]), [])
        self.assertEqual(self.solution.threeSum([0,0,0]), [[0,0,0]])

if __name__ == '__main__':
    unittest.main()
