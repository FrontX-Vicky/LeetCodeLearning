# Main.py - Your Working File
# Task: Dijkstra's Shortest Path patterns
# Goal: Master weighted shortest-path algorithms on graphs and grids

import heapq
from collections import defaultdict
from typing import List


# ============================================================
# PROBLEM 1: NETWORK DELAY TIME
# ============================================================

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    """
    LeetCode #743

    Return the minimum time for all n nodes to receive a signal
    starting from node k. Return -1 if not all nodes are reachable.

    Approach: Dijkstra from source k
    - Build adjacency list from times
    - Run Dijkstra to find shortest dist to every node
    - Return max dist (= time for last node to receive signal)
    - If any node unreachable, return -1
    """
    # TODO: Build graph and run Dijkstra
    graph = defaultdict(list)

    for u, v, w in times:
        graph[u].append((v, w))
    
    dist = { i : float('inf') for i in range(1, n + 1)}
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
    LeetCode #787

    Find cheapest price from src to dst with at most k stops.
    Return -1 if no such route exists.

    Approach: Bellman-Ford (k+1 relaxation rounds)
    - Each round = one more hop allowed
    - Copy prices[] before each round to avoid chaining within a round
    - After k+1 rounds, check prices[dst]

    Why not Dijkstra? Dijkstra doesn't respect the hop limit naturally.
    """
    # TODO: Implement Bellman-Ford with k+1 rounds
    prices = [float('inf')] * n
    prices[src] = 0

    for _ in range(k + 1):
        temp = prices[:]
        for u, v, w in flights:
            # print(u, v, w)
            print(prices)

            if prices[u] != float('inf'):
                print(temp)
                if prices[u] + w < temp[v]:
                    temp[v] = prices[u] + w
        
        prices = temp
    
    return prices[dst] if prices[dst] < float('inf') else -1


# ============================================================
# PROBLEM 3: PATH WITH MINIMUM EFFORT
# ============================================================

def minimumEffortPath(heights: List[List[int]]) -> int:
    """
    LeetCode #1631

    Find the path from (0,0) to (rows-1,cols-1) that minimises
    the maximum absolute difference between consecutive cells.

    Approach: Dijkstra on grid
    - dist[r][c] = minimum effort (max diff so far) to reach (r, c)
    - Heap key = current max effort
    - Edge weight = max(current_effort, |heights[r][c] - heights[nr][nc]|)
    """
    # TODO: Implement Dijkstra on grid with minimax edge weight
    pass


# ============================================================
# PROBLEM 4: SWIM IN RISING WATER
# ============================================================

def swimInWater(grid: List[List[int]]) -> int:
    """
    LeetCode #778

    Return the minimum time t to travel from (0,0) to (n-1,n-1).
    At time t, you can swim to any cell with elevation <= t.

    Approach: Dijkstra where cost to reach cell = max elevation on path
    - dist[r][c] = minimum max-elevation to reach (r, c)
    - Edge weight = max(current_t, grid[nr][nc])
    """
    # TODO: Implement Dijkstra with max-elevation cost
    pass


# ============================================================
# PROBLEM 5: FIND CITY WITH SMALLEST NEIGHBORS
# ============================================================

def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    """
    LeetCode #1334

    Return the city with the fewest reachable cities within
    distanceThreshold. On ties, return the city with the larger index.

    Approach: Floyd-Warshall (all-pairs shortest paths)
    - Build dist[i][j] matrix
    - Relax: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    - Count reachable cities per city, return city with fewest (or highest index on tie)
    """
    # TODO: Implement Floyd-Warshall then count reachable cities
    pass
