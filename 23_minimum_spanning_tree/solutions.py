# Solutions.py - Reference Implementations
# Day 23: Minimum Spanning Tree (Kruskal's + Prim's)

import heapq
from typing import List


# ============================================================
# UNION-FIND (shared utility for Kruskal's problems)
# ============================================================

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank   = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False                                   # already connected
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


# ============================================================
# PROBLEM 1: MIN COST TO CONNECT ALL POINTS — Prim's O(n² log n)
# ============================================================

def minCostConnectPoints(points: List[List[int]]) -> int:
    """
    Prim's algorithm on a dense complete graph.
    Key insight: no need to pre-build all edges — generate lazily from heap.
    """
    n = len(points)
    visited = set()
    heap = [(0, 0)]          # (cost, node_index)
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
# PROBLEM 2: KRUSKAL'S MST
# ============================================================

def minimumSpanningTree(n: int, edges: List[List[int]]) -> int:
    """
    Classic Kruskal's: sort by weight, union-find to skip cycles.
    Need exactly n-1 edges for a spanning tree.
    """
    edges.sort(key=lambda e: e[2])
    uf = UnionFind(n)
    total, count = 0, 0

    for u, v, w in edges:
        if uf.union(u, v):
            total += w
            count += 1
            if count == n - 1:
                return total

    return total if count == n - 1 else -1


# ============================================================
# PROBLEM 3: WATER DISTRIBUTION — virtual node trick
# ============================================================

def minCostToSupplyWater(n: int, wells: List[int], pipes: List[List[int]]) -> int:
    """
    Model well drilling as an edge from virtual node 0 to house i.
    Then run Kruskal's on all edges (pipes + virtual well edges).
    """
    all_edges = []
    for i, cost in enumerate(wells):
        all_edges.append((cost, 0, i + 1))          # virtual node 0 → house i+1
    for h1, h2, cost in pipes:
        all_edges.append((cost, h1, h2))

    all_edges.sort()
    uf = UnionFind(n + 1)                            # nodes 0..n
    total = 0

    for cost, u, v in all_edges:
        if uf.union(u, v):
            total += cost

    return total


# ============================================================
# PROBLEM 4: CRITICAL AND PSEUDO-CRITICAL EDGES
# ============================================================

def findCriticalAndPseudoCriticalEdges(
    n: int, edges: List[List[int]]
) -> List[List[int]]:
    """
    1. Get baseline MST weight.
    2. Critical:        remove edge i → MST weight goes up (or graph disconnects).
    3. Pseudo-critical: force edge i in → MST weight stays the same.
    """
    # Attach original index before sorting
    indexed = sorted(enumerate(edges), key=lambda x: x[1][2])

    def kruskal(skip=-1, force=-1):
        uf = UnionFind(n)
        total, count = 0, 0
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

    baseline = kruskal()
    critical, pseudo = [], []

    for i in range(len(indexed)):
        orig_idx = indexed[i][0]
        if kruskal(skip=i) > baseline:          # removing it raises cost → critical
            critical.append(orig_idx)
        elif kruskal(force=i) == baseline:      # forcing it keeps cost same → pseudo
            pseudo.append(orig_idx)

    return [sorted(critical), sorted(pseudo)]


# ============================================================
# PROBLEM 5: CONNECTING CITIES — Kruskal's with 1-indexed cities
# ============================================================

def minimumCost(n: int, connections: List[List[int]]) -> int:
    """
    Same as Problem 2 but cities are 1-indexed.
    Need n-1 edges to connect n cities.
    """
    connections.sort(key=lambda e: e[2])
    uf = UnionFind(n + 1)                  # cities 1..n
    total, count = 0, 0

    for u, v, w in connections:
        if uf.union(u, v):
            total += w
            count += 1
            if count == n - 1:
                return total

    return -1
