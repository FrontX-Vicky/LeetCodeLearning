# Day 31: DP - String Problems (Palindromes)

## Overview
Today we explore Dynamic Programming as applied to Strings — specifically focusing on **Palindromic Substrings**.

A palindrome is a string that reads the same forwards and backwards. Finding them is a classic DP problem. The core DP relation for palindromes is:
`dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]`
(A string is a palindrome if its outer characters match, AND the inner string is also a palindrome).

**Wait, what about space optimization?**
While the 2D DP table works (`O(N^2)` time, `O(N^2)` space), the most popular and strictly better pattern for these problems is the **"Expand from Center"** approach. It achieves the exact same mathematical subproblem overlapping, but uses `O(1)` space by treating each character (and each gap between characters) as the center of a potential palindrome, expanding outwards.

We will focus on the "Expand from Center" approach as it is the optimal and expected interview answer.

## Problems to Solve

1. [LeetCode #5: Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) (Medium)
   - **Key Insight**: Iterate through the string. For each index `i`, expand outwards `(l, r)` as far as possible while `s[l] == s[r]`.
   - **Gotcha**: Palindromes can be odd-length (centered at `i`, so `l=i, r=i`) OR even-length (centered between `i` and `i+1`, so `l=i, r=i+1`). You must check both!
   - **Goal**: Track the longest valid expansion you find.

2. [LeetCode #647: Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) (Medium)
   - **Key Insight**: Exact same logic as above! But instead of keeping track of the *longest* length, you just increment a counter every time `s[l] == s[r]`.

## Instructions
1. Open `main.py` and implement the functions using the Expand from Center pattern.
2. Run `python test_cases.py` to verify your logic.
3. If you get stuck, check `solutions.py`.
