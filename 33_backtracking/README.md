# Day 33: Backtracking (Combinations/Permutations)

## Overview
Welcome to Phase 7: Advanced Algorithms! We kick off this phase with **Backtracking**. 

Backtracking is a recursive algorithmic technique for solving problems incrementally, one piece at a time, and removing those solutions that fail to satisfy the constraints of the problem at any point of time. It's essentially an optimized brute-force search.

The standard template for Backtracking is:
```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # place (choose)
            place(next_candidate)
            # backtrack (explore)
            backtrack(next_candidate)
            # remove (un-choose)
            remove(next_candidate)
```

## Problems to Solve

1. [LeetCode #46: Permutations](https://leetcode.com/problems/permutations/) (Medium)
   - **Key Insight**: We need to build paths by picking an element, recursing, and then un-picking it to try a different element.
   - **Gotcha**: When appending a valid path to your results array, make sure to append a **COPY** of the path (`path[:]` in Python), otherwise future modifications to the `path` list will corrupt the stored results!

2. [LeetCode #39: Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium)
   - **Key Insight**: We can use the same element an unlimited number of times. 
   - **Decision Tree**: At each step, we have two choices:
     1. Include `candidates[i]` (stay on index `i` so we can use it again).
     2. Skip `candidates[i]` (move to index `i + 1`).
   - **Gotcha**: The tree naturally prevents duplicates by only moving *forward* through the candidates (or staying still), never backwards.

## Instructions
1. Open `main.py` and implement the functions.
2. Run `python test_cases.py` to verify your logic.
3. If you get stuck, check `solutions.py`.
