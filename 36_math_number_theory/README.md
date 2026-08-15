# Day 36: Math & Number Theory

## Overview
Math and Number Theory problems often seem like they require you to just "know a trick", but they rely on core concepts that appear frequently in algorithms and cryptography: primes, factors, and searching for roots.

Today we tackle two foundational math algorithms.

## Key Mathematical Principles

1. **Factors always appear in pairs**: 
   If `x * y = N`, then one of the factors must be $\le \sqrt{N}$ and the other must be $\ge \sqrt{N}$. 
   *Why this matters*: When checking if a number is prime, or looking for factors, you NEVER need to check past $\sqrt{N}$.

2. **The Sieve of Eratosthenes**:
   The most efficient way to find all primes up to $N$. Instead of checking if each number is prime (which is slow), you assume all numbers are prime, and then systematically cross out all the multiples of each prime you find.

## Problems to Solve

1. [LeetCode #204: Count Primes](https://leetcode.com/problems/count-primes/) (Medium)
   - **Key Insight**: Use the **Sieve of Eratosthenes**. Create a boolean array `is_prime` of size $N$, initially all `True`. 
   - Starting from $p=2$, if `is_prime[p]` is true, then $p$ is a prime. Cross out all multiples of $p$ starting from $p \times p$.
   - You only need to loop $p$ up to $\sqrt{N}$.

2. [LeetCode #69: Sqrt(x)](https://leetcode.com/problems/sqrtx/) (Easy)
   - **Key Insight**: This is a **Binary Search** problem in disguise!
   - You know the square root of $x$ must be somewhere between 2 and $x/2$ (for $x \ge 4$). 
   - Simply binary search that range, checking if `pivot * pivot == x`.

## Instructions
1. Open `main.py` and implement the functions.
2. Run `python test_cases.py` to verify your logic.
3. If you get stuck, check `solutions.py`.
