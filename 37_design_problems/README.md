# Day 37: System Design Data Structures

## Overview
Welcome to **Phase 8: System Design & Practice**! In this phase, we move beyond single algorithms and focus on combining data structures to design systems that meet specific performance constraints. 

These are some of the most frequently asked questions in senior-level interviews because they test your ability to synthesize multiple concepts (like Hashing + Linked Lists).

## Problems to Solve

1. [LeetCode #155: Min Stack](https://leetcode.com/problems/min-stack/) (Medium)
   - **Goal**: Build a stack that can `push`, `pop`, `top`, and `getMin()` all in $O(1)$ time.
   - **Key Insight**: How do you know what the minimum was *before* the current minimum got popped? By storing it! Instead of just pushing the `val`, push a tuple containing `(val, current_min)`.

2. [LeetCode #146: LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium)
   - **Goal**: Build a cache that evicts the Least Recently Used item when capacity is reached, supporting $O(1)$ `get` and `put`.
   - **Key Insight**: 
     - A **Hash Map** gives you $O(1)$ lookups.
     - A **Doubly Linked List** gives you $O(1)$ removals and additions (if you have the node reference).
     - Combine them! Store `key -> Node` in the map. When an item is accessed, remove it from its current position in the list and move it to the `head` (most recently used). When capacity is full, pop the `tail`.
     - *Pro-tip*: Use a "dummy" head and "dummy" tail node to avoid writing messy `if node is None:` edge cases during add/remove!

## Instructions
1. Open `main.py` and implement the classes.
2. Run `python test_cases.py` to verify your logic.
3. If you get stuck, check `solutions.py`.
