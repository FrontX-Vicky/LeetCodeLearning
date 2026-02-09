# Solutions.py - Reference Implementations with Visualizations
# Graph BFS & DFS Problems

from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ============================================================
# PROBLEM 1: NUMBER OF ISLANDS
# ============================================================

def num_islands_dfs(grid: List[List[str]]) -> int:
    """
    DFS Approach: Sink island technique
    
    Algorithm:
    1. Iterate through each cell
    2. When finding '1', increment count and sink entire island
    3. Sinking = DFS marking all connected '1's as '0'
    
    Time: O(m * n) - visit each cell once
    Space: O(m * n) - recursion depth in worst case
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        # Base cases: out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
        # Mark as visited by sinking it
        grid[r][c] = '0'
        
        # Explore 4 directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left
    
    # Scan entire grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)  # Sink entire island
    
    return islands


def num_islands_bfs(grid: List[List[str]]) -> int:
    """
    BFS Approach: Level-by-level exploration
    
    Algorithm:
    1. Find '1', start BFS from it
    2. Add to queue, mark visited
    3. Process neighbors level by level
    
    Time: O(m * n)
    Space: O(min(m, n)) - queue size
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'  # Mark visited
        
        while queue:
            row, col = queue.popleft()
            
            # Check 4 directions
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
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
    DFS Approach with HashMap
    
    Algorithm:
    1. Use hash map: original → clone
    2. For each node, create clone if not exists
    3. Recursively clone neighbors
    
    Time: O(V + E) - visit each node and edge once
    Space: O(V) - hash map and recursion
    """
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
        
        # Clone neighbors
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)


def clone_graph_bfs(node: Optional[Node]) -> Optional[Node]:
    """
    BFS Approach with Queue
    
    Algorithm:
    1. Clone starting node, add to queue
    2. For each node in queue, clone its neighbors
    3. Use hash map to track cloned nodes
    
    Time: O(V + E)
    Space: O(V)
    """
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
    Reverse DFS from Oceans
    
    Algorithm:
    1. DFS from Pacific edges (top, left)
    2. DFS from Atlantic edges (bottom, right)
    3. Return cells reachable from both
    
    Key Insight: Reverse the flow direction!
    Water flows from high to low
    So DFS from low (ocean) to high (cells)
    
    Time: O(m * n)
    Space: O(m * n)
    """
    if not heights or not heights[0]:
        return []
    
    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()
    
    def dfs(r, c, visited):
        visited.add((r, c))
        
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and 
                (nr, nc) not in visited and
                heights[nr][nc] >= heights[r][c]):  # Can flow UP
                dfs(nr, nc, visited)
    
    # DFS from Pacific edges
    for c in range(cols):
        dfs(0, c, pacific)  # Top row
    for r in range(rows):
        dfs(r, 0, pacific)  # Left column
    
    # DFS from Atlantic edges
    for c in range(cols):
        dfs(rows - 1, c, atlantic)  # Bottom row
    for r in range(rows):
        dfs(r, cols - 1, atlantic)  # Right column
    
    # Return intersection
    return list(pacific & atlantic)


# ============================================================
# PROBLEM 4: COURSE SCHEDULE
# ============================================================

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Cycle Detection using DFS
    
    States:
    - 0 (unvisited): Not processed
    - 1 (visiting): Currently in DFS path
    - 2 (visited): Fully processed
    
    Algorithm:
    1. Build adjacency list
    2. For each course, run DFS
    3. If encounter "visiting" node → cycle detected
    
    Time: O(V + E)
    Space: O(V + E)
    """
    # Build adjacency list
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * num_courses
    
    def has_cycle(course):
        if state[course] == 1:  # Visiting → cycle!
            return True
        if state[course] == 2:  # Already visited
            return False
        
        state[course] = 1  # Mark visiting
        
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True
        
        state[course] = 2  # Mark visited
        return False
    
    # Check each course
    for course in range(num_courses):
        if has_cycle(course):
            return False
    
    return True


def can_finish_bfs(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Topological Sort using Kahn's Algorithm (BFS)
    
    Algorithm:
    1. Calculate in-degree for each course
    2. Start with courses having 0 in-degree
    3. Remove edges, update in-degrees
    4. If process all courses → no cycle
    
    Time: O(V + E)
    Space: O(V + E)
    """
    # Build graph and in-degree
    graph = {i: [] for i in range(num_courses)}
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Start with 0 in-degree courses
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    processed = 0
    
    while queue:
        course = queue.popleft()
        processed += 1
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return processed == num_courses


# ============================================================
# PROBLEM 5: SURROUNDED REGIONS
# ============================================================

def solve(board: List[List[str]]) -> None:
    """
    Reverse Marking Approach
    
    Algorithm:
    1. DFS from border 'O's, mark as safe (temporary marker)
    2. Convert all remaining 'O's to 'X' (they're surrounded)
    3. Restore safe 'O's
    
    Time: O(m * n)
    Space: O(m * n)
    """
    if not board or not board[0]:
        return
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        
        board[r][c] = 'S'  # Mark as safe
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    # Mark border-connected 'O's as safe
    for r in range(rows):
        dfs(r, 0)           # Left border
        dfs(r, cols - 1)    # Right border
    for c in range(cols):
        dfs(0, c)           # Top border
        dfs(rows - 1, c)    # Bottom border
    
    # Capture surrounded regions and restore safe ones
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'  # Surrounded
            elif board[r][c] == 'S':
                board[r][c] = 'O'  # Safe, restore


# ============================================================
# PROBLEM 6: ROTTING ORANGES
# ============================================================

def oranges_rotting(grid: List[List[int]]) -> int:
    """
    Multi-Source BFS
    
    Algorithm:
    1. Find all rotten oranges, add to queue
    2. Count fresh oranges
    3. BFS level by level (each level = 1 minute)
    4. Rot adjacent fresh oranges
    5. If fresh oranges remain → return -1
    
    Time: O(m * n)
    Space: O(m * n)
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    
    # Initialize: find rotten oranges and count fresh
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    
    # No fresh oranges → done
    if fresh == 0:
        return 0
    
    minutes = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # Multi-source BFS
    while queue:
        minutes += 1
        
        # Process all rotten oranges at current minute
        for _ in range(len(queue)):
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Rot it
                    fresh -= 1
                    queue.append((nr, nc))
    
    # Check if all oranges rotted
    return minutes - 1 if fresh == 0 else -1


# ============================================================
# VISUALIZATION HELPERS
# ============================================================

def visualize_island_search():
    """
    Visualize island detection process
    
    Example Grid:
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1
    
    Process:
    Step 1: Find (0,0)='1' → Island 1, DFS
      - Visit (0,0), (0,1), (1,0), (1,1)
      - Mark all as visited
    
    Step 2: Find (2,2)='1' → Island 2, DFS
      - Visit (2,2)
      - Mark as visited
    
    Step 3: Find (3,3)='1' → Island 3, DFS
      - Visit (3,3), (3,4)
      - Mark all as visited
    
    Result: 3 islands
    """
    print("Island Detection Visualization")
    print("Grid: 1=land, 0=water")
    print("DFS marks all connected 1's as visited")


def visualize_graph_clone():
    """
    Visualize graph cloning
    
    Original Graph:
      1 --- 2
      |     |
      4 --- 3
    
    Adjacency List:
      1: [2, 4]
      2: [1, 3]
      3: [2, 4]
      4: [1, 3]
    
    Cloning Process (DFS):
      Step 1: Clone node 1
      Step 2: Clone neighbor 2 (recursively)
      Step 3: Clone neighbor 3 of 2
      Step 4: Clone neighbor 4 of 3
      Step 5: Link back to cloned 1 (from hashmap)
    
    Result: New graph with same structure but different objects
    """
    print("Graph Cloning Visualization")
    print("Use HashMap to track original → clone mapping")


def visualize_water_flow():
    """
    Visualize Pacific Atlantic water flow
    
    Grid:
      1 2 2 3 5
      3 2 3 4 4
      2 4 5 3 1
      6 7 1 4 5
      5 1 1 2 4
    
    Pacific (top/left):
      P P P P P
      P . . . .
      P . . . .
      P . . . .
      P . . . .
    
    Atlantic (bottom/right):
      . . . . A
      . . . . A
      . . . . A
      . . . . A
      A A A A A
    
    DFS from Pacific edges → find reachable cells
    DFS from Atlantic edges → find reachable cells
    Intersection → cells reaching both oceans
    """
    print("Water Flow Visualization")
    print("Reverse DFS: Start from ocean, flow upward")


if __name__ == "__main__":
    print("Graph BFS & DFS - Reference Solutions")
    print("=" * 60)
    
    # Test visualizations
    visualize_island_search()
    print()
    visualize_graph_clone()
    print()
    visualize_water_flow()
