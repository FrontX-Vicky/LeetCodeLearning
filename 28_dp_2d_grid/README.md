# Day 28: DP - 2D Grid Problems

## Overview
Welcome to the second dimension! We've mastered 1D DP arrays; now it's time to extend our tabulation to 2D matrices.

Many DP problems involve moving through a grid, often with constraints like "you can only move right or down". These problems are classic examples of overlapping subproblems. 

The core intuition for 2D Grid DP is:
To find the optimal path or number of ways to reach cell `(r, c)`, you only need to look at the cells you could have come from (usually `(r-1, c)` and `(r, c-1)`).

The state transition equation often looks like:
`dp[r][c] = dp[r-1][c] + dp[r][c-1]` (for counting paths)
*OR*
`dp[r][c] = cost[r][c] + min(dp[r-1][c], dp[r][c-1])` (for min path sums)

## Problems to Solve

1. [LeetCode #62: Unique Paths](https://leetcode.com/problems/unique-paths/) (Medium)
   - **Concept**: Combinatorics on a grid. How many unique ways exist to reach the bottom-right corner?
   - **Goal**: Build a 2D `dp` array where each cell stores the sum of paths from its top and left neighbors.

2. [LeetCode #64: Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) (Medium)
   - **Concept**: Pathfinding with weighted costs.
   - **Goal**: Instead of counting ways, find the path that minimizes the sum of cell values.
   - **Bonus Challenge**: Can you do this in **O(1) extra space** by modifying the input `grid` directly instead of allocating a new `dp` matrix?

## Instructions
1. Open `main.py` and implement the functions.
2. Run `python test_cases.py` to verify your logic.
3. If you get stuck, check `solutions.py` for the optimal 2D and O(1) space implementations.
