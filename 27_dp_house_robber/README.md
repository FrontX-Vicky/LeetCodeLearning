# Day 27: DP - House Robber Pattern

## Overview
We've spent the last two days heavily working with 1D DP optimizations that take the form `dp[i] = dp[i-1] + dp[i-2]` and space-optimizing them down to `t0, t1, t2` or `prev_prev, prev`.

Today we are going to look at the **House Robber Pattern**. This is arguably the most famous DP pattern on LeetCode. Instead of adding the two previous states together, we are faced with a `max()` decision:
*Do I rob this house and add its loot to my stash from two houses ago, OR do I skip this house and keep my stash from the previous house?*

The state transition equation becomes: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.
Because it only relies on the last two variables, you can implement this with O(1) space!

## Problems to Solve

1. [LeetCode #198: House Robber](https://leetcode.com/problems/house-robber/) (Medium)
   - **Concept**: The classic 1D array DP where adjacent elements cannot be selected.
   - **Goal**: Implement the space-optimized O(1) tabulation by shifting a sliding window of `rob1` and `rob2`.

2. [LeetCode #213: House Robber II](https://leetcode.com/problems/house-robber-ii/) (Medium)
   - **Concept**: The houses are arranged in a circle! This means house 0 and house `n-1` are adjacent.
   - **Goal**: Figure out how to reuse the exact same linear logic from part 1 to solve the circular array constraint. *(Hint: You can't pick both the first and the last house simultaneously...)*

## Instructions
1. Open `main.py` and implement the two functions.
2. Run `python test_cases.py` to verify your logic.
3. If you get stuck, check `solutions.py` for the optimal O(1) space implementations.
