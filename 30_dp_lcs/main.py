def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    Given two strings text1 and text2, return the length of their longest common subsequence.
    If there is no common subsequence, return 0.
    """
    m, n = len(text1), len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for r in range(1, m + 1):
        for c in range(1, n + 1):
            if text1[r - 1] == text2[c - 1]:
                dp[r][c] = 1 + dp[r - 1][c - 1]
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
    
    return dp[m][n]


def lengthOfLIS(nums: list[int]) -> int:
    """
    Given an integer array nums, return the length of the longest strictly increasing subsequence.
    """
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
            
    return max(dp)
    

def main():
    print("Welcome to Day 30: DP - Longest Common Subsequence!")
    print("Run `python test_cases.py` to check your implementations.")

if __name__ == "__main__":
    main()
