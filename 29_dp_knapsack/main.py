from typing import List

# LeetCode #416 - Medium
# ============================================================
def canPartition(nums: List[int]) -> bool:
    """
    Given an integer array nums, return true if you can partition the array into two subsets 
    such that the sum of the elements in both subsets is equal, or false otherwise.
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2

    dp = {0}

    for n in nums:
        dp ={j + n for j in dp} | dp
    
    return target in dp

# LeetCode #494 - Medium
# ============================================================
def findTargetSumWays(nums: List[int], target: int) -> int:
    """
    You are given an integer array nums and an integer target.
    You want to build an expression out of nums by adding one of the symbols '+' and '-' 
    before each integer in nums and then concatenate all the integers.
    Return the number of different expressions that you can build, which evaluates to target.
    """
    dp = {0 : 1} 

    for n in nums:
        next_dp = {}
        for s, count in dp.items():
            next_dp[s + n] = next_dp.get(s + n, 0) + count
            next_dp[s - n] = next_dp.get(s - n, 0) + count
        
        dp = next_dp

    return dp.get(target, 0)

def main():
    print("Welcome to Day 29: DP - Knapsack Problems!")
    print("Run `python test_cases.py` to check your implementations.")

if __name__ == "__main__":
    main()
