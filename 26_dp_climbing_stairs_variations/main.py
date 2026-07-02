# LeetCode #1137 - Easy
# ============================================================
def tribonacci(n: int) -> int:
    """
    The Tribonacci sequence Tn is defined as follows: 
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
    Given n, return the value of Tn.
    """
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    t0, t1, t2 = 0, 1, 1

    for _ in range(3, n + 1):
        t0, t1, t2 = t1, t2, t0 + t1 + t2
    
    return t2

# LeetCode #91 - Medium
# ============================================================
def numDecodings(s: str) -> int:
    """
    A message containing letters from A-Z can be encoded into numbers using the mapping:
    'A' -> "1", 'B' -> "2", ... 'Z' -> "26"
    Given a string s containing only digits, return the number of ways to decode it.
    """
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    # dp[i] represents the number of ways to decode s[:i]
    # We only need the last two states for space optimisation (just like climbing stairs)

    prev_prev = 1 # dp[i-2]
    prev = 1      # dp[i-1]

    for i in range(1, n):
        current = 0


        if s[i] != '0':
            current += prev 

        two_digit = int(s[i - 1 : i + 1])
        if 10 <= two_digit <= 26:
            current += prev_prev
        
        prev_prev = prev
        prev = current
    return prev

def main():
    print("Welcome to Day 26: DP - Climbing Stairs Variations!")
    print("Run `python test_cases.py` to check your implementations.")

if __name__ == "__main__":
    main()
