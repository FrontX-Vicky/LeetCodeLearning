# Day 34: Greedy Algorithms Advanced

## Overview
Today we explore **Advanced Greedy Algorithms**. A greedy algorithm builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit (the "greedy" choice).

While many problems that *seem* greedy actually require Dynamic Programming (to check all overlapping subproblems), certain problems have a mathematical property where the locally optimal choice *guarantees* a globally optimal solution.

Today's focus is on the famous "Jump Game" series.

## Problems to Solve

1. [LeetCode #55: Jump Game](https://leetcode.com/problems/jump-game/) (Medium)
   - **Key Insight**: You don't need to actually simulate the jumps. You just need to keep track of the `max_reach` (the furthest index you can possibly reach at any given moment). 
   - **Greedy Choice**: If you are at index `i`, you can reach up to `i + nums[i]`. So continuously update `max_reach = max(max_reach, i + nums[i])`. 
   - **Gotcha**: If you ever reach an index `i` that is *greater* than your `max_reach`, it means you are stuck and cannot jump any further. Return `False`!

2. [LeetCode #45: Jump Game II](https://leetcode.com/problems/jump-game-ii/) (Medium)
   - **Key Insight**: Instead of just boolean reachability, we want the *minimum number of jumps*. We can use an implicit BFS (Breadth-First Search) approach using a greedy strategy.
   - **Greedy Choice**: Keep track of the `current_end` of the jump you just made, and the `farthest` point you can reach with an additional jump. When your loop reaches `current_end`, it means you *must* take another jump, so you increment your jump counter and update `current_end = farthest`.

## Instructions
1. Open `main.py` and implement the functions.
2. Run `python test_cases.py` to verify your logic.
3. If you get stuck, check `solutions.py`.
