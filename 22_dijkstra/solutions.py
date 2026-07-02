# Solutions.py - Reference Implementations
# Day 22: Dijkstra's Shortest Path

import heapq
from collections import defaultdict
from typing import List


# ============================================================
# PROBLEM 1: NETWORK DELAY TIME
# ============================================================

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    """
    Classic Dijkstra from source k.

    Build adjacency list, run Dijkstra, return max dist.
    If any node unreachable return -1.
    """
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]

    while heap:
        cost, node = heapq.heappop(heap)

        if cost > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1


# ============================================================
# PROBLEM 2: CHEAPEST FLIGHTS WITHIN K STOPS
# ============================================================

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """
    Bellman-Ford with k+1 relaxation rounds.

    Each round represents one additional hop (stop).
    Copy prices before each round to prevent chaining within a round.
    """
    prices = [float('inf')] * n
    prices[src] = 0

    for _ in range(k + 1):
        temp = prices[:]
        for u, v, w in flights:
            if prices[u] != float('inf') and prices[u] + w < temp[v]:
                temp[v] = prices[u] + w
        prices = temp

    return prices[dst] if prices[dst] < float('inf') else -1


# ============================================================
# PROBLEM 3: PATH WITH MINIMUM EFFORT
# ============================================================

def minimumEffortPath(heights: List[List[int]]) -> int:
    """
    Dijkstra where edge weight = |heights[r1][c1] - heights[r2][c2]|.
    dist[r][c] = minimum effort (max diff along path) to reach (r, c).
    Heap key = current max effort so far.
    """
    rows, cols = len(heights), len(heights[0]) # here we are getting the actual count of rows and columns
    dist = [[float('inf')] * cols for _ in range(rows)] # here we are creating a grid for distance calculation initially they are ♾️
    dist[0][0] = 0 # marking the first node distance as 0
    heap = [(0, 0, 0)]  # (effort, row, col) initiating a heap to perform iterations 

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # directions referenced to current node
                #  right   left    bottom   top
    while heap:
        effort, r, c = heapq.heappop(heap) # popping out the first element from heap

        if effort > dist[r][c]: # is current effort is greater than previous then skip
            continue

        if r == rows - 1 and c == cols - 1: # destination node, last node
            return effort

        for dr, dc in directions: # now do bfs from current node
            nr, nc = r + dr, c + dc # new row , new coulmn = current + directions(row , column)
            if 0 <= nr < rows and 0 <= nc < cols: # out off bound rows cols prevention
                new_effort = max(effort, abs(heights[r][c] - heights[nr][nc])) # take the max effort to reach to cell as it will go in bottom of heap
                if new_effort < dist[nr][nc]:
                    dist[nr][nc] = new_effort
                    heapq.heappush(heap, (new_effort, nr, nc))

    return dist[rows - 1][cols - 1]


# ============================================================
# PROBLEM 4: SWIM IN RISING WATER
# ============================================================

def swimInWater(grid: List[List[int]]) -> int:
    """
    Dijkstra where the cost to enter a cell is grid[r][c].
    dist[r][c] = minimum time to reach (r, c) = max elevation on path.
    """
    n = len(grid)
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = grid[0][0]
    heap = [(grid[0][0], 0, 0)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while heap:
        t, r, c = heapq.heappop(heap)

        if t > dist[r][c]:
            continue

        if r == n - 1 and c == n - 1:
            return t

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                new_t = max(t, grid[nr][nc])
                if new_t < dist[nr][nc]:
                    dist[nr][nc] = new_t
                    heapq.heappush(heap, (new_t, nr, nc))

    return dist[n - 1][n - 1]


# ============================================================
# PROBLEM 5: FIND CITY WITH SMALLEST NEIGHBORS
# ============================================================

def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    """
    Floyd-Warshall for all-pairs shortest paths, then count reachable
    cities within threshold for each city.
    Return city with fewest reachable; ties go to higher index.
    """
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    best_city = -1
    best_count = INF

    for city in range(n):
        count = sum(1 for j in range(n) if j != city and dist[city][j] <= distanceThreshold)
        if count <= best_count:
            best_count = count
            best_city = city

    return best_city


if __name__ == "__main__":
    print("networkDelayTime:", networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2), "Expected: 2")
    print("findCheapestPrice:", findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1), "Expected: 700")
    print("minimumEffortPath:", minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]), "Expected: 2")
    print("swimInWater:", swimInWater([[0,2],[1,3]]), "Expected: 3")
    print("findTheCity:", findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4), "Expected: 3")
