# Dynamic Programming (DP) Summary & Cheatsheet

Congratulations on finishing Phase 6! Dynamic Programming is often considered the hardest algorithmic topic to master. This document summarizes everything you've learned.

---

## 1. The Core Principle of DP

At its heart, Dynamic Programming is just **smart brute force**. It is an optimization technique used to solve problems by breaking them down into smaller subproblems. 

For a problem to be solvable by DP, it **must** have two properties:
1. **Optimal Substructure**: The optimal solution to the main problem can be constructed from the optimal solutions of its subproblems. *(e.g., The shortest path from A to C via B is the shortest path from A to B + the shortest path from B to C).*
2. **Overlapping Subproblems**: The algorithm asks for the answer to the *exact same subproblem* multiple times. 

**The DP Solution:** Instead of calculating the same subproblem over and over (which takes exponential time, $O(2^N)$), you calculate it **once**, store the result in memory (an array or hash map), and simply look it up the next time you need it. This reduces exponential time to polynomial time (e.g., $O(N)$ or $O(N^2)$).

> [!TIP]
> **Memoization (Top-Down)** = Recursion + Caching.
> **Tabulation (Bottom-Up)** = Iteration + Array building. (This is what you've mostly been doing!)

---

## 2. Why are these problems categorized as DP?

You might wonder: *"Why is Climbing Stairs in the same category as Knapsack?"*

They are categorized together because **their mathematical base is the same**: they all require a **State Transition Equation**.

In every single DP problem you solved, the core challenge was figuring out how state `N` relates to previous states. If you can define the mathematical relationship between the current step and the past steps, it's a DP problem.

*   **Climbing Stairs**: `dp[i] = dp[i-1] + dp[i-2]`
*   **House Robber**: `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`
*   **Unique Paths**: `dp[r][c] = dp[r-1][c] + dp[r][c-1]`
*   **0/1 Knapsack**: `dp[w] = max(dp[w], value + dp[w - weight])`

Once you find that equation, the code practically writes itself.

---

## 3. Common Patterns from Phase 6

Here is a summary of the 5 major DP patterns you mastered over the last 8 days:

### A. 1D DP / Fibonacci Sequence
*   **Examples**: Climbing Stairs, Min Cost Climbing Stairs, Decode Ways.
*   **Pattern**: The current state depends on the immediate 1 or 2 previous states. 
*   **Space Optimization**: Since you only ever look back 1 or 2 steps, you don't need a whole array. You can just use two variables (`prev1`, `prev2`) to achieve $O(1)$ space.

### B. "Take it or Leave it" (Conditional 1D DP)
*   **Examples**: House Robber I & II.
*   **Pattern**: At every step, you make a strict choice: Do I include this item (and add it to `dp[i-2]`), or do I skip it (and just take `dp[i-1]`)?

### C. 2D Grid DP
*   **Examples**: Unique Paths, Minimum Path Sum.
*   **Pattern**: You are moving through a matrix, usually right and down. The value of any cell `dp[r][c]` depends strictly on the cell above it `dp[r-1][c]` and the cell to its left `dp[r][c-1]`.

### D. Knapsack DP (Target Sum / Partition)
*   **Examples**: Partition Equal Subset Sum, Target Sum (0/1 Knapsack), Coin Change (Unbounded).
*   **Pattern**: You have a list of items and a target capacity/amount.
    *   **0/1 Knapsack**: Items can be used *once*. Loop items first, loop capacities *backwards*.
    *   **Unbounded**: Items can be used *unlimited* times. Loop capacities first, loop items *forwards*.

### E. Two-Sequence DP
*   **Examples**: Longest Common Subsequence (LCS).
*   **Pattern**: You are comparing two strings. You build a 2D matrix where rows represent string A and columns represent string B. If characters match, you look diagonally up-left. If they don't, you look up and left.

---

## 4. Real World Uses of DP

Dynamic programming isn't just for LeetCode; it runs the modern world. Here is where these exact patterns are used in real life:

1. **`git diff` and Plagiarism Detection (LCS Pattern)**
   When you run `git diff` to see what code changed, Git uses the **Longest Common Subsequence** algorithm to find the lines that stayed the same, and marks the remaining lines as additions (+) or deletions (-).

2. **Network Routing Protocols (Grid / Path DP Pattern)**
   How does a packet of data get from your router to a server in Japan? Protocols like OSPF and BGP use algorithms (like Dijkstra's or Bellman-Ford, which are forms of DP) to calculate the shortest, cheapest, or fastest path through a web of thousands of routers.

3. **Financial Portfolio Optimization (Knapsack Pattern)**
   Investment banks use the **Knapsack problem**. If you have \$100,000 to invest (the knapsack capacity) and 500 different stocks/bonds with varying costs and predicted returns (the items and values), DP finds the exact combination that maximizes profit.

4. **Video Compression (Decision / Target DP)**
   When you stream Netflix, the video is compressed. The compressor has to decide for every single frame: "Do I store this entire image, or do I just store the *differences* from the last frame?" It uses DP to find the sequence of compression choices that minimizes file size while maintaining visual quality.

5. **Spell Checkers / Auto-correct (String DP)**
   When you type "definetly" and it corrects to "definitely", the system uses the **Edit Distance (Levenshtein Distance)** algorithm — a classic 2D DP problem that calculates the minimum number of character insertions, deletions, or replacements needed to turn word A into word B.
