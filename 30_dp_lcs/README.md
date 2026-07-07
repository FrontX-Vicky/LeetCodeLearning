# Day 30: DP - Longest Common Subsequence

## Overview
Today we cover one of the most famous patterns in Dynamic Programming: **Longest Common Subsequence (LCS)**, alongside its closely related cousin **Longest Increasing Subsequence (LIS)**. 

These problems ask us to find the longest subsequence (elements in relative order, but not necessarily contiguous) that satisfies a specific condition.

## Problems to Solve

1. [LeetCode #1143: Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) (Medium)
   - **Key Insight**: We use a 2D DP table where `dp[r][c]` represents the LCS of `text1[:r]` and `text2[:c]`.
   - **State Transition**: 
     - If characters match: `dp[r][c] = 1 + dp[r-1][c-1]` (extend the previous LCS)
     - If they don't match: `dp[r][c] = max(dp[r-1][c], dp[r][c-1])` (drop one character and take the best result)

2. [LeetCode #300: Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) (Medium)
   - **Key Insight**: We use a 1D DP array where `dp[i]` is the length of the LIS that *must* end at `nums[i]`.
   - **State Transition**: To compute `dp[i]`, we look back at all previous elements `j < i`. If `nums[i] > nums[j]`, we can extend the sequence ending at `j`. So `dp[i] = max(dp[i], 1 + dp[j])`.

## Instructions
1. Open `main.py` and implement the functions.
2. Run `python test_cases.py` to verify your logic.
3. If you get stuck, check `solutions.py`.
