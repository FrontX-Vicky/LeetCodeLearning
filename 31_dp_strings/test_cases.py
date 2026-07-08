import unittest
from main import longestPalindrome, countSubstrings

class TestStringDP(unittest.TestCase):
    def test_longestPalindrome(self):
        # Valid answers for "babad" are "bab" or "aba".
        res = longestPalindrome("babad")
        self.assertIn(res, ["bab", "aba"])
        
        self.assertEqual(longestPalindrome("cbbd"), "bb")
        self.assertEqual(longestPalindrome("a"), "a")
        self.assertEqual(longestPalindrome("ac"), "a") # or "c", but "a" is usually first

    def test_countSubstrings(self):
        self.assertEqual(countSubstrings("abc"), 3) # "a", "b", "c"
        self.assertEqual(countSubstrings("aaa"), 6) # "a", "a", "a", "aa", "aa", "aaa"

if __name__ == '__main__':
    unittest.main()
