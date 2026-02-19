# Main.py - Your Working File
# Task: Implement Graph BFS & DFS Algorithms
# Goal: Master graph traversal techniques

from collections import deque
from typing import List, Optional


# Definition for graph node (for Problem 2)
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ============================================================
# PROBLEM 1: NUMBER OF ISLANDS
# ============================================================

def num_islands_dfs(grid: List[List[str]]) -> int:
    """
    Count number of islands in a 2D grid.
    
    Island = connected group of '1's (land)
    '0' = water
    
    Example:
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3
    
    Approach: DFS/BFS
    - For each unvisited '1', start DFS/BFS
    - Mark all connected '1's as visited
    - Increment island count
    
    Time: O(m * n)
    Space: O(m * n) for visited set or recursion
    """
    # TODO: Implement island counting
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        # Base case: out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        # mark as visited by sinking it 
        grid[r][c] = '0'

        # Explore 4 directions 
        dfs(r + 1, c) # down
        dfs(r - 1, c) # up
        dfs(r, c + 1) # right
        dfs(r, c - 1) # left

    # scan entire grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c) # Sink entire island

def num_island_bfs(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0' # Mark visited

        while queue:
            row, col = queue.popleft()

            # Check 4 directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))
    
    # Scan grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                bfs(r, c)
    
    return islands

# ============================================================
# PROBLEM 2: CLONE GRAPH
# ============================================================

def clone_graph_dfs(node: Optional[Node]) -> Optional[Node]:
    """
    Return a deep copy of an undirected graph.
    
    Example:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Node 1: neighbors [2, 4]
    Node 2: neighbors [1, 3]
    Node 3: neighbors [2, 4]
    Node 4: neighbors [1, 3]
    
    Approach: DFS/BFS with hash map
    - Map original nodes to cloned nodes
    - For each node, clone it and its neighbors
    - Use hash map to track already cloned nodes
    
    Time: O(V + E) where V = vertices, E = edges
    Space: O(V) for hash map
    """
    # TODO: Implement graph cloning
    if not node:
        return None
    
    old_to_new = {}

    def dfs(node):
        # If already cloned, return clone
        if node in old_to_new:
            return old_to_new[node]
        
        # Create clone
        clone = Node(node.val)
        old_to_new[node] = clone

        # clone neighbors
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)

def clone_graph_bfs(node: Optional[Node]) -> Optional[Node]:
    if not node:
        return None
    
    old_to_new = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        for neighbor in curr.neighbors:
            if neighbor not in old_to_new:

                # Clone neighbor
                old_to_new[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            
            # Add neighbor to current clone
            old_to_new[curr].neighbors.append(old_to_new[neighbor])
        
    return old_to_new[node]

# ============================================================
# PROBLEM 3: PACIFIC ATLANTIC WATER FLOW
# ============================================================

def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    Find cells where water can flow to both Pacific and Atlantic oceans.
    
    Water flows from higher or equal height cells.
    Pacific touches top and left edges.
    Atlantic touches bottom and right edges.
    
    Example:
    heights = [
      [1,2,2,3,5],
      [3,2,3,4,4],
      [2,4,5,3,1],
      [6,7,1,4,5],
      [5,1,1,2,4]
    ]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    
    Approach: Reverse DFS/BFS
    - Start from Pacific edges, mark reachable cells
    - Start from Atlantic edges, mark reachable cells
    - Return cells reachable from both
    
    Time: O(m * n)
    Space: O(m * n)
    """
    # TODO: Implement water flow
    if not heights or not heights[0]:
        return []
    
    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(r, c, visited):
        visited.add((r, c))

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]):
                dfs(nr, nc, visited)
    
    # DFS from pacific edges
    for c in range(cols):
        dfs(0, c, pacific) # Top row
    for r in range(rows):
        dfs(r, 0, pacific) # Left column
    
    # DFS from Atlantic edges
    for c in range(cols):
        dfs(rows - 1, c, atlantic) # Bottom row
    
    for r in range(rows):
        dfs(r, cols - 1, atlantic) # Right column
    
    # return intersections 
    return list(pacific & atlantic)


# ============================================================
# PROBLEM 4: COURSE SCHEDULE
# ============================================================

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determine if you can finish all courses given prerequisites.
    
    Example:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: True
    Explanation: Take course 0, then course 1
    
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: False
    Explanation: Circular dependency
    
    Approach: Cycle detection in directed graph
    - Build adjacency list
    - Use DFS with visiting/visited states
    - If encounter "visiting" node → cycle exists
    
    Time: O(V + E)
    Space: O(V + E)
    """
    # TODO: Implement course schedule
    # Build adjacency list
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * num_courses

    def has_cycle(course):
        if state[course] == 1: # Visiting -> cycle!
            return True
        if state[course] == 2: # Already visited
            return False

        state[course] = 1 # Mark visiting

        for prereq in graph[course]:
            if has_cycle(prereq):
                return True
        
        state[course] = 2 # Mark visited
        return False

    # check each course
    for course in range(num_courses):
        if has_cycle(course):
            return False
    
    return True

# ============================================================
# PROBLEM 5: SURROUNDED REGIONS
# ============================================================

def solve(board: List[List[str]]) -> None:
    """
    Capture surrounded regions on a board.
    
    'O' cells surrounded by 'X' → flip to 'X'
    'O' cells on border or connected to border → keep 'O'
    
    Example:
    Input:
    X X X X
    X O O X
    X X O X
    X O X X
    
    Output:
    X X X X
    X X X X
    X X X X
    X O X X
    
    Approach: Reverse marking
    - DFS/BFS from border 'O's, mark them as safe
    - All unmarked 'O's are surrounded → flip to 'X'
    - Restore safe 'O's
    
    Time: O(m * n)
    Space: O(m * n)
    
    Note: Modifies board in-place
    """
    # TODO: Implement surrounded regions
    pass


# ============================================================
# PROBLEM 6: ROTTING ORANGES
# ============================================================

def oranges_rotting(grid: List[List[int]]) -> int:
    """
    Find minimum time for all oranges to rot.
    
    0 = empty cell
    1 = fresh orange
    2 = rotten orange
    
    Each minute, rotten oranges rot adjacent fresh oranges
    (4-directional: up, down, left, right)
    
    Example:
    grid = [
      [2,1,1],
      [1,1,0],
      [0,1,1]
    ]
    Output: 4
    
    Explanation:
    Minute 0: [2,1,1],[1,1,0],[0,1,1]
    Minute 1: [2,2,1],[2,1,0],[0,1,1]
    Minute 2: [2,2,2],[2,2,0],[0,1,1]
    Minute 3: [2,2,2],[2,2,0],[0,2,1]
    Minute 4: [2,2,2],[2,2,0],[0,2,2]
    
    Return -1 if impossible to rot all oranges.
    
    Approach: Multi-source BFS
    - Start with all rotten oranges in queue
    - Process level by level (each level = 1 minute)
    - Track minutes and fresh orange count
    
    Time: O(m * n)
    Space: O(m * n)
    """
    # TODO: Implement rotting oranges
    pass


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_grid(grid: List[List[str]]) -> None:
    """Helper: Print 2D grid"""
    for row in grid:
        print(" ".join(row))


if __name__ == "__main__":
    print("=" * 60)
    print("GRAPHS BFS & DFS - SMOKE TEST")
    print("=" * 60)
    
    # Test 1: Number of Islands
    print("\n" + "-" * 60)
    print("PROBLEM 1: NUMBER OF ISLANDS")
    print("-" * 60)
    grid1 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    result = num_islands_dfs(grid1)
    print(f"Number of islands: {result}")
    print(f"Expected: 3")

    result = num_islands_dfs(grid1)
    print(f"Number of islands: {result}")
    print(f"Expected: 3")
    
    # Test 2: Clone Graph
    print("\n" + "-" * 60)
    print("PROBLEM 2: CLONE GRAPH")
    print("-" * 60)
    # Create sample graph: [[2,4],[1,3],[2,4],[1,3]]
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    cloned = clone_graph_dfs(node1)
    cloned = clone_graph_bfs(node1)
    print(f"Cloned graph: {cloned is not None and cloned is not node1}")
    print(f"Expected: True (different object)")
    
    # Test 3: Pacific Atlantic
    print("\n" + "-" * 60)
    print("PROBLEM 3: PACIFIC ATLANTIC WATER FLOW")
    print("-" * 60)
    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    result = pacific_atlantic(heights)
    print(f"Cells reaching both oceans: {len(result)} cells")
    print(f"Expected: 7 cells")
    
    # Test 4: Course Schedule
    print("\n" + "-" * 60)
    print("PROBLEM 4: COURSE SCHEDULE")
    print("-" * 60)
    result = can_finish(2, [[1,0]])
    print(f"Can finish courses [1,0]: {result}")
    print(f"Expected: True")
    result = can_finish(2, [[1,0],[0,1]])
    print(f"Can finish courses [1,0],[0,1]: {result}")
    print(f"Expected: False")
    
    # Test 5: Surrounded Regions
    print("\n" + "-" * 60)
    print("PROBLEM 5: SURROUNDED REGIONS")
    print("-" * 60)
    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    solve(board)
    print("After solving:")
    print_grid(board)
    print("Expected: Middle O's captured, border O kept")
    
    # Test 6: Rotting Oranges
    print("\n" + "-" * 60)
    print("PROBLEM 6: ROTTING ORANGES")
    print("-" * 60)
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    result = oranges_rotting(grid)
    print(f"Minutes to rot all oranges: {result}")
    print(f"Expected: 4")
    
    print("\n" + "=" * 60)
    print("Run 'python test_cases.py' for full test suite!")
    print("=" * 60)
