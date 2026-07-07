def longestCommonSubsequence(text1: str, text2: str) -> int:
    # 2D DP tabulation
    # dp[r][c] = length of LCS of text1[:r] and text2[:c]
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for r in range(1, m + 1):
        for c in range(1, n + 1):
            if text1[r - 1] == text2[c - 1]:
                # Characters match: add 1 to the result of excluding both
                dp[r][c] = 1 + dp[r - 1][c - 1]
            else:
                # Characters differ: take the max of excluding one or the other
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

    return dp[m][n]

def lengthOfLIS(nums: list[int]) -> int:
    # 1D DP tabulation
    # dp[i] = length of LIS ending exactly at nums[i]
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
                
    return max(dp)
