from typing import List

# LeetCode #198 - Medium
# ============================================================
def rob(nums: List[int]) -> int:
    """
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, the only constraint stopping you 
    from robbing each of them is that adjacent houses have security systems connected and 
    it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.
    """
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2

# LeetCode #213 - Medium
# ============================================================
def rob_II(nums: List[int]) -> int:
    """
    You are a professional robber planning to rob houses along a street. 
    All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
    Given an integer array nums representing the amount of money of each house, 
    return the maximum amount of money you can rob tonight without alerting the police.
    """
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


def main():
    print("Welcome to Day 27: DP - House Robber Pattern!")
    print("Run `python test_cases.py` to check your implementations.")

if __name__ == "__main__":
    main()
