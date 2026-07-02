# Day 25: DP Introduction (1D Problems)

## Overview
Dynamic Programming (DP) is a technique for solving complex problems by breaking them down into simpler, overlapping subproblems. 

The two main approaches are:
1. **Top-Down (Memoization)**: Start from the target state and recursively break it down. Cache results of subproblems to avoid redundant calculations.
2. **Bottom-Up (Tabulation)**: Start from the base cases and iteratively build up to the target state. This often saves space complexity since we only need to store the previous states.

## Problems to Solve
1. [LeetCode #509: Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) (Easy) - The absolute classic. Perfect for contrasting top-down vs bottom-up.
2. [LeetCode #70: Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (Easy) - Conceptually identical to Fibonacci, but framed as a combinatorics problem.
3. [LeetCode #746: Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) (Easy) - Introduces the concept of choosing the `min()` or `max()` transition from previous states.

## Instructions
1. Open `main.py` and implement the missing functions.
2. Run `python test_cases.py` to check your solutions.
3. Compare your implementation with the reference solutions in `solutions.py`.
