# Day 35: Bit Manipulation

## Overview
Bit Manipulation is the technique of directly operating on binary representations of integers using **bitwise operators**. It produces some of the most elegant, O(1)-space, O(n)-time solutions in computer science.

## Essential Bitwise Operators

| Operator | Symbol | Description | Example |
|---|---|---|---|
| AND | `&` | 1 only if both bits are 1 | `5 & 3 = 1` (101 & 011 = 001) |
| OR | `\|` | 1 if either bit is 1 | `5 \| 3 = 7` (101 \| 011 = 111) |
| XOR | `^` | 1 if bits are **different** | `5 ^ 3 = 6` (101 ^ 011 = 110) |
| NOT | `~` | Flip all bits | `~5 = -6` |
| Left Shift | `<<` | Shift bits left (multiply by 2) | `5 << 1 = 10` |
| Right Shift | `>>` | Shift bits right (divide by 2) | `5 >> 1 = 2` |

## Key Bit Tricks to Know

- **`x ^ x = 0`** — Any number XOR'd with itself is 0.
- **`x ^ 0 = x`** — Any number XOR'd with 0 is itself.
- **`n & (n-1)`** — Clears the **lowest set bit** of `n`. Used in Brian Kernighan's popcount algorithm.
- **`n & 1`** — Checks if `n` is odd (checks the last bit).
- **`n & (-n)`** — Isolates the lowest set bit of `n`.

## Problems to Solve

1. [LeetCode #136: Single Number](https://leetcode.com/problems/single-number/) (Easy)
   - **Key Insight**: Use XOR. Every number that appears **twice** will cancel itself out (`x ^ x = 0`). The lone number will be the only one left since `x ^ 0 = x`.
   - **Pattern**: `result = 0; for n in nums: result ^= n; return result`
   - **Why it's O(1) space**: No hash map, no sorting — just one integer!

2. [LeetCode #191: Number of 1 Bits (Hamming Weight)](https://leetcode.com/problems/number-of-1-bits/) (Easy)
   - **Key Insight**: Use **Brian Kernighan's Algorithm**. The trick `n & (n-1)` drops the *lowest* set bit of `n` in a single operation.
   - **Pattern**: Loop while `n != 0`, count each iteration, and do `n = n & (n-1)` each step.
   - **Why it's better than checking each bit**: The loop only runs **as many times as there are set bits**, not 32 times for every number.

## Instructions
1. Open `main.py` and implement the functions.
2. Run `python test_cases.py` to verify your logic.
3. If you get stuck, check `solutions.py`.
