from typing import List

def uniquePaths(m: int, n: int) -> int:
    # 2D DP table initialized to 1s.
    # The first row and first column will naturally stay 1, 
    # since there's only 1 way to travel in a straight line.
    dp = [[1] * n for _ in range(m)]
    
    for r in range(1, m):
        for c in range(1, n):
            # The number of ways to reach a cell is the sum of ways 
            # to reach the cell above it and the cell to its left.
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
            
    return dp[m-1][n-1]

def minPathSum(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    
    # We can modify the grid in-place to save space (O(1) auxiliary space)
    
    # 1. Fill the first row (can only come from the left)
    for c in range(1, cols):
        grid[0][c] += grid[0][c-1]
        
    # 2. Fill the first column (can only come from above)
    for r in range(1, rows):
        grid[r][0] += grid[r-1][0]
        
    # 3. Fill the rest of the grid
    for r in range(1, rows):
        for c in range(1, cols):
            # The min cost to reach this cell is its own cost PLUS 
            # the minimum of the cost to reach the cell above or to the left.
            grid[r][c] += min(grid[r-1][c], grid[r][c-1])
            
    return grid[-1][-1]
