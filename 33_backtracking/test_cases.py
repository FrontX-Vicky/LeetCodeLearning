import unittest
from main import permute, combinationSum

class TestBacktracking(unittest.TestCase):
    def test_permute(self):
        res1 = permute([1, 2, 3])
        self.assertEqual(len(res1), 6)
        expected1 = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
        for p in expected1:
            self.assertIn(p, res1)
            
        res2 = permute([0, 1])
        self.assertEqual(len(res2), 2)
        self.assertIn([0, 1], res2)
        self.assertIn([1, 0], res2)

    def test_combinationSum(self):
        res1 = combinationSum([2, 3, 6, 7], 7)
        self.assertEqual(len(res1), 2)
        
        # Sort inner lists to ensure safe comparison
        res1_sorted = [sorted(r) for r in res1]
        self.assertIn([7], res1_sorted)
        self.assertIn([2, 2, 3], res1_sorted)
        
        res2 = combinationSum([2, 3, 5], 8)
        self.assertEqual(len(res2), 3)
        res2_sorted = [sorted(r) for r in res2]
        self.assertIn([2, 2, 2, 2], res2_sorted)
        self.assertIn([2, 3, 3], res2_sorted)
        self.assertIn([3, 5], res2_sorted)

if __name__ == '__main__':
    unittest.main()
