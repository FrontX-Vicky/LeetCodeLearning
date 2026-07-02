from typing import List

def rob(nums: List[int]) -> int:
    # Rob 1 is a classic 1D DP with state transition:
    # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    rob1, rob2 = 0, 0
    
    for n in nums:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp
        
    return rob2

def rob_II(nums: List[int]) -> int:
    # For a circular array, we can't rob both the first and last house.
    # Therefore, we just run the standard House Robber algorithm twice:
    # 1. From house 0 to n-2 (skip the last house)
    # 2. From house 1 to n-1 (skip the first house)
    # Return the max of those two (plus the edge case of a single house).
    
    if len(nums) == 1:
        return nums[0]
        
    def helper(sub_nums):
        rob1, rob2 = 0, 0
        for n in sub_nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        
    return max(helper(nums[:-1]), helper(nums[1:]))
