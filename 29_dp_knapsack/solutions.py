from typing import List

def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2

    # dp[j] = True means we can form sum j using elements seen so far.
    # This is the space-optimised 0/1 Knapsack (1D DP).
    dp = {0}   # We can always form sum 0 (empty subset)

    for n in nums:
        # Iterate in reverse to avoid using the same element twice!
        dp = {j + n for j in dp} | dp

    return target in dp

def findTargetSumWays(nums: List[int], target: int) -> int:
    # dp[s] = number of ways to reach sum s
    dp = {0: 1}  # 1 way to reach sum 0 (empty expression)

    for n in nums:
        next_dp = {}
        for s, count in dp.items():
            next_dp[s + n] = next_dp.get(s + n, 0) + count
            next_dp[s - n] = next_dp.get(s - n, 0) + count
        dp = next_dp

    return dp.get(target, 0)
