def longestPalindrome(s: str) -> str:
    # Expand from center approach (technically O(N^2) time, O(1) space)
    # A true DP approach uses O(N^2) space, but expand-from-center is strictly better.
    # DP relation: dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
    
    res = ""
    res_len = 0
    
    for i in range(len(s)):
        # Odd length palindromes (centered at i)
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1
            l -= 1
            r += 1
            
        # Even length palindromes (centered between i and i+1)
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1
            l -= 1
            r += 1
            
    return res

def countSubstrings(s: str) -> int:
    # Similar expand from center approach
    res = 0
    
    for i in range(len(s)):
        # Odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
            
        # Even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
            
    return res
