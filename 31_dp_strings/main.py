def longestPalindrome(s: str) -> str:
    """
    Given a string s, return the longest palindromic substring in s.
    """
    res = ""
    res_len = 0

    for i in range(len(s)):

        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1
            l -= 1
            r += 1
        
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1
            l -= 1
            r += 1
    
    return res

def countSubstrings(s: str) -> int:
    """
    Given a string s, return the number of palindromic substrings in it.
    """
    pass

def main():
    print("Welcome to Day 31: DP - String Problems (Palindromes)!")
    print("Run `python test_cases.py` to check your implementations.")

if __name__ == "__main__":
    main()
