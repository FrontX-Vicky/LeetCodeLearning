# Day 39: Hard Problems Marathon

## Overview
Welcome to Day 39! Today is the true test of your algorithmic endurance. We are diving into **Hard Problems**. These problems rarely introduce *new* concepts; instead, they require you to combine multiple advanced concepts or find clever, optimized ways to apply them.

## Problems to Solve

1. [LeetCode #42: Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard)
   - **Goal**: Given an array representing an elevation map, compute how much water it can trap.
   - **Key Insight**: The amount of water trapped above any bar `i` is determined by `min(max_height_left, max_height_right) - height[i]`. 
   - *Optimization*: You can solve this in $O(N)$ space using prefix arrays, but the true Hard solution uses **Two Pointers** starting from both ends to solve it in $O(1)$ space.

2. [LeetCode #295: Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) (Hard)
   - **Goal**: Design a data structure that supports adding numbers and finding the median in $O(1)$ time.
   - **Key Insight**: The median splits a sorted array into a "small half" and a "large half". If you maintain a Max-Heap for the small half and a Min-Heap for the large half, you can keep them balanced and find the median instantly!

## Instructions
1. Open `main.py` and implement the logic.
2. Run `python test_cases.py` to test your solutions.
3. If you're stuck, check `solutions.py`.
