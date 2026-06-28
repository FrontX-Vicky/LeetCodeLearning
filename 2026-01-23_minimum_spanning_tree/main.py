# Main.py - Your Working File
# Task: Minimum Spanning Tree patterns
# Goal: Master Kruskal's and Prim's algorithms for MST problems

import heapq
from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank   = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])    # path compression 
        return self.parent[x]

    def union(self, x, y):
        py, px = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


# ============================================================
# PROBLEM 1: MIN COST TO CONNECT ALL POINTS
# ============================================================

def minCostConnectPoints(points: List[List[int]]) -> int:
    """
    LeetCode #1584

    Return the minimum cost to connect all points where cost between
    two points is their Manhattan distance.

    Approach: Prim's Algorithm
    - Start from node 0
    - Use a min-heap of (cost, node)
    - Always pick the cheapest edge to an unvisited node
    - Manhattan distance: |x1-x2| + |y1-y2|
    """
    # TODO: Implement Prim's algorithm on a complete graph
    n = len(points)
    visited = set()
    heap = [(0, 0)]   #cost, node_index
    total = 0

    while len(visited) < n:
        cost, i = heapq.heappop(heap)
        if i in visited:
            continue
        visited.add(i)
        total += cost
        for j in range(n):
            if j not in visited:
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, (dist, j))
    
    return total

# ============================================================
# PROBLEM 2: KRUSKAL'S MST (UNION FIND)
# ============================================================

def minimumSpanningTree(n: int, edges: List[List[int]]) -> int:
    """
    Custom problem — given n nodes and weighted undirected edges,
    return the total weight of the MST. Return -1 if not connected.

    Approach: Kruskal's Algorithm
    - Sort all edges by weight ascending
    - Use Union-Find: add edge if it connects two different components
    - Stop when n-1 edges are added (or exhaust all edges)
    """
    # TODO: Implement Kruskal's with Union-Find
    edges.sort(key=lambda e: e[2])
    uf = UnionFind(n)
    total, count = 0,0

    for u, v, w in edges:
        if uf.union(u, v):
            total += w
            count += 1
            if count == n - 1:
                return total
    
    return total if count == n - 1 else -1

# ============================================================
# PROBLEM 3: OPTIMIZE WATER DISTRIBUTION IN A VILLAGE
# ============================================================

def minCostToSupplyWater(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    """
    LeetCode #1168

    n houses. Can drill a well at house i for wells[i-1] cost, OR
    lay a pipe between houses for pipes[j] = [house1, house2, cost].
    Return minimum total cost to supply water to all houses.

    Approach: Model wells as edges from virtual node 0
    - Add virtual node 0 connected to each house i with cost wells[i-1]
    - Run Kruskal's on all edges (pipes + virtual well edges)
    """
    # TODO: Add virtual node and run Kruskal's MST
    all_edges = []
    for i, cost in enumerate(wells):
        all_edges.append((cost, 0, i + 1))
    for h1, h2, cost in pipes:
        all_edges.append((cost, h1, h2))

    all_edges.sort()
    uf = UnionFind(n + 1)
    total = 0

    for cost, u, v in all_edges:
        if uf.union(u, v):
            total += cost
    
    return total


# ============================================================
# PROBLEM 4: FIND CRITICAL AND PSEUDO-CRITICAL EDGES IN MST
# ============================================================

def findCriticalAndPseudoCriticalEdges(
    n: int, edges: List[List[int]]
) -> List[List[int]]:
    """
    LeetCode #1489

    Find all critical edges (removal increases MST weight) and
    pseudo-critical edges (appear in some but not all MSTs).

    Approach: Kruskal's + edge inclusion/exclusion testing
    - Baseline: run full Kruskal's to get MST weight
    - Critical: remove edge i → MST weight increases or graph disconnects
    - Pseudo-critical: force edge i in → MST weight stays the same
    """
    # TODO: Implement edge classification with Kruskal's
    indexed = sorted(enumerate(edges), key=lambda x: x[1][2])

    def krushkal(skip=-1, force=-1):
        uf = UnionFind(n)
        total, count = 0,0
        if force != -1:
            orig_idx = indexed[force][0]
            u, v, w = edges[orig_idx]
            uf.union(u, v)
            total += w
            count += 1

        for i, (orig_idx, (u, v, w)) in enumerate(indexed):
            if i == skip:
                continue
            if uf.union(u, v):
                total += w
                count += 1
        return total if count == n - 1 else float('inf')

    baseline = krushkal()
    critical, pseudo = [], []

    for i in range(len(indexed)):
        orig_idx = indexed[i][0]
        if krushkal(skip = i) > baseline:
            critical.append(orig_idx)
        elif krushkal(force = i) == baseline:
            pseudo.append(orig_idx)
        
    return [sorted(critical), sorted(pseudo)]


# ============================================================
# PROBLEM 5: CONNECTING CITIES WITH MINIMUM COST
# ============================================================

def minimumCost(n: int, connections: List[List[int]]) -> int:
    """
    LeetCode #1135

    There are n cities. connections[i] = [city1, city2, cost].
    Return the minimum cost to connect all cities, or -1 if impossible.

    Approach: Kruskal's Algorithm
    - Sort edges by cost
    - Union-Find to avoid cycles
    - Need exactly n-1 edges for n cities
    """
    # TODO: Implement Kruskal's MST, return -1 if not fully connected
    connections.sort(key=lambda e: e[2])
    uf = UnionFind(n + 1)
    total, count = 0, 0

    for u, v, w in connections:
        if uf.union(u, v):
            total += w
            count += 1
            if count == n - 1:
                return total
    
    return -1


# ============================================================
# SMOKE TESTS
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("MINIMUM SPANNING TREE - SMOKE TESTS")
    print("=" * 60)

    print("\nPROBLEM 1: MIN COST CONNECT POINTS (Prim's)")
    print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]), "Expected: 20")

    print("\nPROBLEM 2: MINIMUM SPANNING TREE (Kruskal's)")
    print(minimumSpanningTree(4, [[0,1,1],[1,2,2],[0,2,4],[2,3,3]]), "Expected: 6")

    print("\nPROBLEM 3: WATER DISTRIBUTION")
    print(minCostToSupplyWater(3, [1,2,2], [[1,2,1],[2,3,1]]), "Expected: 3")

    print("\nPROBLEM 4: CRITICAL AND PSEUDO-CRITICAL EDGES")
    print(findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]),
          "Expected: [[0,1],[2,3,4,5]]")

    print("\nPROBLEM 5: CONNECTING CITIES")
    print(minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]]), "Expected: 6")

    print("\n" + "=" * 60)
    print("Run 'python test_cases.py' for full test suite!")
    print("=" * 60)
