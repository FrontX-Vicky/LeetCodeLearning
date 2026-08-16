import unittest
from main import CapstoneProblems

class TestCapstone(unittest.TestCase):
    def setUp(self):
        self.solution = CapstoneProblems()

    def test_min_window(self):
        self.assertEqual(self.solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(self.solution.minWindow("a", "a"), "a")
        self.assertEqual(self.solution.minWindow("a", "aa"), "")

    def test_ladder_length(self):
        self.assertEqual(self.solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
        self.assertEqual(self.solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]), 0)

if __name__ == '__main__':
    unittest.main()
