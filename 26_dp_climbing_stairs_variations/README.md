# Day 26: DP - Climbing Stairs Variations

## Overview
Yesterday, we learned the foundational concepts of 1D Dynamic Programming Tabulation. The core mechanism is transitioning from overlapping subproblems (e.g., `dp[i] = dp[i-1] + dp[i-2]`) and optimizing space by only storing the necessary window of variables.

Today, we will apply that exact same skeletal framework to two incredibly common variations. Both of these problems follow the "Climbing Stairs" pattern but introduce slightly different mathematical definitions or complex conditional transitions.

## Problems to Solve

1. [LeetCode #1137: N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) (Easy)
   - **Concept**: A simple mathematical variation. Instead of the sum of the last two numbers, you sum the last three numbers (`T0 + T1 + T2`).
   - **Goal**: Implement the space-optimized O(1) tabulation by shifting a sliding window of size 3.

2. [LeetCode #91: Decode Ways](https://leetcode.com/problems/decode-ways/) (Medium)
   - **Concept**: The ultimate Climbing Stairs variation. You are still deciding whether to take a 1-step (single digit decode) or a 2-step (two-digit decode), but with complex edge cases involving `0`s and invalid alphabetic encodings.
   - **Goal**: Implement O(n) time and O(1) space DP by conditionally adding `prev` and `prev_prev` values based on whether the digits are valid mappings.

## Instructions
1. Open `main.py` and implement the two functions.
2. Run `python test_cases.py` to verify your logic against edge cases (especially for `0` in Decode Ways).
3. If you get stuck, check `solutions.py` for the optimal O(1) space implementations.
