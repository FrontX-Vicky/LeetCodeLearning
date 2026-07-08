# Day 32: DP - Advanced Patterns

## Overview
Day 32 is the **final day of Phase 6 (Dynamic Programming)**. We wrap up with two classic problems that each represent a distinct advanced DP pattern:

1. **Unbounded Knapsack** — Unlike the 0/1 Knapsack (where each item can be used once), here each coin can be reused unlimited times.
2. **Conditional State DP** — Where the DP transition depends on validation of the current input character(s).

## Problems to Solve

1. [LeetCode #322: Coin Change](https://leetcode.com/problems/coin-change/) (Medium)
   - **Key Insight**: This is the classic **Unbounded Knapsack** pattern.
   - **DP Definition**: `dp[a]` = minimum number of coins to make amount `a`.
   - **Transition**: For each amount `a`, try every coin `c`. If `a - c >= 0`, then `dp[a] = min(dp[a], 1 + dp[a-c])`.
   - **Base Case**: `dp[0] = 0` (0 coins to make amount 0).
   - **Result**: `dp[amount]` (or `-1` if it's still `inf`).
   - ⚠️ **Key Difference from 0/1 Knapsack**: The outer loop is over `amounts`, not `coins`. This allows the same coin to be reused freely!

2. [LeetCode #91: Decode Ways](https://leetcode.com/problems/decode-ways/) (Medium)
   - **Key Insight**: This is a **conditional** 1D DP, similar to Climbing Stairs but with hard validation gates.
   - **DP Definition**: `dp[i]` = number of ways to decode the first `i` characters.
   - **Transition**: At each step `i`, you try to decode the last 1 character AND the last 2 characters. You only add `dp[i-1]` or `dp[i-2]` to `dp[i]` if those decodings are *valid* (e.g., no leading zeros, two-digit value must be in [10..26]).

## Instructions
1. Open `main.py` and implement the functions.
2. Run `python test_cases.py` to verify your logic.
3. If you get stuck, check `solutions.py`.
