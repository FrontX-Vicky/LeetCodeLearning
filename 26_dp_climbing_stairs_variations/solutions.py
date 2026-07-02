def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    t0, t1, t2 = 0, 1, 1
    for _ in range(3, n + 1):
        t0, t1, t2 = t1, t2, t0 + t1 + t2
    
    return t2

def numDecodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0
        
    n = len(s)
    # dp[i] represents the number of ways to decode s[:i]
    # We only need the last two states for space optimization (just like climbing stairs)
    
    prev_prev = 1 # dp[i-2]
    prev = 1      # dp[i-1]
    
    for i in range(1, n):
        current = 0
        
        # Single digit decode (if it's not '0')
        if s[i] != '0':
            current += prev
            
        # Two digit decode (if it's between 10 and 26)
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            current += prev_prev
            
        prev_prev = prev
        prev = current
        
    return prev
