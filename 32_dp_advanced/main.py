def coinChange(coins: list[int], amount: int) -> int:
    """
    You are given an integer array coins representing coins of different denominations
    and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    
    return dp[amount] if dp[amount] != float('inf') else -1

def numDecodings(s: str) -> int:
    """
    Given a string s containing only digits, return the number of ways to decode it.
    'A' -> 1, 'B' -> 2, ..., 'Z' -> 26.
    """
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, n + 1):
        one_digit = int(s[i - 1])
        if one_digit != 0:
            dp[i] += dp[i - 1]

        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    
    return dp[n]

def main():
    print("Welcome to Day 32: DP - Advanced Patterns!")
    print("Run `python test_cases.py` to check your implementations.")

if __name__ == "__main__":
    main()
