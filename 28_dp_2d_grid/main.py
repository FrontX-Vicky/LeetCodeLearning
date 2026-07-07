from typing import List

# LeetCode #62 - Medium
# ============================================================
def uniquePaths(m: int, n: int) -> int:
    """
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
    The robot can only move either down or right at any point in time.
    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    """
    
    dp = [[1] * n for _ in range(m)]

    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]

    
    return dp[m - 1][n - 1]



# LeetCode #64 - Medium
# ============================================================
def minPathSum(grid: List[List[int]]) -> int:
    """
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
    which minimizes the sum of all numbers along its path.
    Note: You can only move either down or right at any point in time.
    """
    rows, cols = len(grid), len(grid[0])

    for c in range(1, cols):
        grid[0][c] += grid[0][c-1]
    
    for r in range(1, rows):
        grid[r][0] += grid[r-1][0]
    
    for r in range(1, rows):
        for c in range(1, cols):
            grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        
    return grid[-1][-1]


def main():
    print("Welcome to Day 28: DP - 2D Grid Problems!")
    print("Run `python test_cases.py` to check your implementations.")

if __name__ == "__main__":
    main()
