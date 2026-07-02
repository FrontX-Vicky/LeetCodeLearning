from typing import List

def fib_memo(n: int) -> int:
    # Memoization approach (Top-Down)
    memo = {0: 0, 1: 1}
    def helper(x):
        if x in memo:
            return memo[x]
        memo[x] = helper(x - 1) + helper(x - 2)
        return memo[x]
    return helper(n)

def fib_tab(n: int) -> int:
    # Tabulation approach (Bottom-Up with O(1) space)
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def climbStairs(n: int) -> int:
    # Notice this is identical to Fibonacci shifted by 1
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def minCostClimbingStairs(cost: List[int]) -> int:
    # We can mutate the input array to save space
    # cost[i] represents the min cost to GET to step i and PAY the toll
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])
    
    # We can reach the top from either the last or second-to-last step
    return min(cost[-1], cost[-2])
