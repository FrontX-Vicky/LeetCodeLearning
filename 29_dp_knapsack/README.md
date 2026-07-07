# Day 29: DP - Knapsack Problems

## Overview
Today we tackle the **0/1 Knapsack Pattern** — arguably one of the most important DP problem classes in computer science. Instead of navigating a grid, we're now deciding for each item: **include it or exclude it?**

The classic Knapsack DP table is:
`dp[i][w]` = max value achievable using the first `i` items with weight capacity `w`.
The transition: `dp[i][w] = max(dp[i-1][w], val[i] + dp[i-1][w-wt[i]])`.

However, both problems today use a **space-optimised 1D DP** approach, collapsing the `i` dimension:
- **`canPartition`**: Uses a `set` of reachable sums. The question "can we form sum `target`?" becomes "is `target` in our set after processing all items?"
- **`findTargetSumWays`**: Uses a `dict` mapping reachable sums to their count of ways. Instead of just tracking *if* a sum is reachable, we track *how many ways* to reach it.

## Problems to Solve

1. [LeetCode #416: Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) (Medium)
   - **Key Insight**: If we can find a subset that sums to `total // 2`, then the remaining elements automatically form the other equal half.
   - **Goal**: Build a set of reachable sums using the space-optimised Knapsack pattern.
   - ⚠️ **Gotcha**: When iterating, you must build a **new** set at each step (or iterate in reverse) to avoid using the same element twice!

2. [LeetCode #494: Target Sum](https://leetcode.com/problems/target-sum/) (Medium)
   - **Key Insight**: Instead of `True/False`, the DP tracks **a count of ways** for each reachable sum.
   - **Goal**: Use a `dict` as the DP state. At each step, expand the dict by adding and subtracting the current number from all previously reachable sums.

## Instructions
1. Open `main.py` and implement the functions.
2. Run `python test_cases.py` to verify your logic.
3. If you get stuck, check `solutions.py`.
