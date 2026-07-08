def coinChange(coins: list[int], amount: int) -> int:
    # Unbounded Knapsack (each coin can be used unlimited times)
    # dp[a] = min coins to make amount a
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # base case: 0 coins to make amount 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != float('inf') else -1

def numDecodings(s: str) -> int:
    # 1D DP: dp[i] = number of ways to decode s[:i]
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # empty string has 1 decoding (base case)
    dp[1] = 0 if s[0] == '0' else 1  # single digit

    for i in range(2, n + 1):
        # Check single digit decode (s[i-1])
        one_digit = int(s[i - 1])
        if one_digit != 0:
            dp[i] += dp[i - 1]

        # Check two digit decode (s[i-2:i])
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]
