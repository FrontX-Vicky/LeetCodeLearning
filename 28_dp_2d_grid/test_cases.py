import unittest
from main import uniquePaths, minPathSum

class Test2DGrid(unittest.TestCase):

    def test_uniquePaths(self):
        self.assertEqual(uniquePaths(3, 7), 28)
        self.assertEqual(uniquePaths(3, 2), 3)
        self.assertEqual(uniquePaths(1, 1), 1)

    def test_minPathSum(self):
        self.assertEqual(minPathSum([[1,3,1],[1,5,1],[4,2,1]]), 7)
        self.assertEqual(minPathSum([[1,2,3],[4,5,6]]), 12)
        self.assertEqual(minPathSum([[1]]), 1)

if __name__ == '__main__':
    unittest.main()
