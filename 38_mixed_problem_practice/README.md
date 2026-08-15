# Day 38: Mixed Problem Practice

## Overview
Welcome to Day 38! In this phase, we are combining different patterns to test your ability to recognize what a problem requires without explicitly being told "this is a Graph problem" or "this is a Two Pointer problem."

## Problems to Solve

1. [LeetCode #200: Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium)
   - **Goal**: Count the number of connected components (islands of '1's) in a 2D grid.
   - **Key Insight**: Whenever you see "connected components" on a grid, think Graph Traversal. You can iterate through every cell in the grid. If you find a '1' that hasn't been visited, increment your island count, and launch a DFS/BFS from that cell to mark all connected '1's as visited (or just change them to '0').

2. [LeetCode #15: 3Sum](https://leetcode.com/problems/3sum/) (Medium)
   - **Goal**: Find all unique triplets in an array that sum up to 0.
   - **Key Insight**: We already know how to solve 2Sum efficiently. If you **sort** the array, you can iterate through it, pinning the first number `nums[i]`. Then, the problem reduces to finding a 2Sum of `-nums[i]` in the remaining subarray. You can use the Two Pointers technique on the sorted subarray to find it in $O(N)$ time per pinned number.
   - *Pro-tip*: Because the array is sorted, skipping duplicates is very easy! If `nums[i] == nums[i-1]`, just `continue`.

## Instructions
1. Open `main.py` and implement the logic.
2. Run `python test_cases.py` to test your solutions.
3. If you're stuck, check `solutions.py`.
