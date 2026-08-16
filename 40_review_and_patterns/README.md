# Day 40: The Grand Finale

## Overview
Welcome to Day 40! We made it! Today is the **Grand Finale**, the ultimate review of everything you've learned over the last 39 days. You are no longer just learning patterns; you are applying them to complex, hybrid problems that companies like Google, Meta, and Amazon love to ask.

## Problems to Solve

1. [LeetCode #76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard)
   - **Goal**: Find the shortest substring in `s` that contains all characters in `t`.
   - **Key Insight**: **Sliding Window + Hash Map**. You expand the `right` pointer to find a valid window. Once you have all required characters, you shrink the `left` pointer as much as possible to minimize the window. It's the ultimate test of two-pointer mechanics!

2. [LeetCode #127: Word Ladder](https://leetcode.com/problems/word-ladder/) (Hard)
   - **Goal**: Find the shortest transformation sequence from a start word to an end word, changing one letter at a time.
   - **Key Insight**: **BFS + Graph**. The "shortest path" in an unweighted graph is a dead giveaway for BFS. The hardest part of this problem isn't the traversal; it's building the graph edges efficiently using a wild-card dictionary (e.g., matching "hit" to "*it", "h*t", "hi*").

## Final Instructions
1. Open `main.py` and implement the logic.
2. Run `python test_cases.py` to test your solutions.
3. If you're stuck, check `solutions.py`.
4. Celebrate!
