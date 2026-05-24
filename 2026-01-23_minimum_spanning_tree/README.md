# Day 23: Minimum Spanning Tree (Kruskal's + Prim's)

**Date**: January 23, 2026
**Focus**: Connecting nodes at minimum total cost
**Difficulty**: Medium–Hard

---

## Core Concept

A **Minimum Spanning Tree (MST)** of a weighted undirected graph is a subset of edges that:
- Connects all nodes (spanning)
- Has no cycles (tree)
- Has the minimum possible total edge weight

Two classic algorithms to find it:

| | Kruskal's | Prim's |
|---|---|---|
| **Strategy** | Sort edges globally, add cheapest non-cycle edge | Grow a single tree, always add cheapest reachable edge |
| **Data structure** | Union-Find | Min-heap |
| **Best for** | Sparse graphs | Dense graphs |
| **Time** | O(E log E) | O(E log V) |

---

## Problems

### Problem 1: Min Cost to Connect All Points
**LeetCode**: [#1584](https://leetcode.com/problems/min-cost-to-connect-all-points/)

Connect all points on a 2D plane with minimum Manhattan distance total.

**Key insight**: Complete graph (every pair connected) → Prim's is ideal; build edges lazily from the heap.

```
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
```

---

### Problem 2: Minimum Spanning Tree (Kruskal's)
Custom problem — pure Kruskal's implementation practice.

**Template**:
```
Sort edges by weight
For each edge (u, v, w):
    if find(u) != find(v):   ← different components
        union(u, v)
        total += w
        count += 1
```

---

### Problem 3: Optimize Water Distribution
**LeetCode**: [#1168](https://leetcode.com/problems/optimize-water-distribution-in-a-village/)

**Key trick**: Model well-drilling as edges from a **virtual node 0** to each house. Then it's a standard MST on (n+1) nodes.

```
wells  = [1, 2, 2]   →   virtual edges: (0→1, cost 1), (0→2, cost 2), (0→3, cost 2)
pipes  = [[1,2,1],[2,3,1]]
Run Kruskal's on all edges together
```

---

### Problem 4: Critical and Pseudo-Critical Edges
**LeetCode**: [#1489](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)

- **Critical**: removing it increases MST cost → must be in every MST
- **Pseudo-critical**: forcing it in doesn't increase MST cost → in some MSTs but not all

**Approach**: Run Kruskal's 2×(E) times:
- Once skipping edge i → if cost increases, it's critical
- Once forcing edge i → if cost stays same, it's pseudo-critical

---

### Problem 5: Connecting Cities with Minimum Cost
**LeetCode**: [#1135](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)

Standard Kruskal's on 1-indexed cities. Return -1 if fewer than n-1 edges connect all n cities.

---

## Key Patterns to Remember

```
Kruskal's skeleton:
    edges.sort(key=lambda e: e[2])
    uf = UnionFind(n)
    for u, v, w in edges:
        if uf.union(u, v):
            total += w

Prim's skeleton:
    heap = [(0, start)]
    visited = set()
    while len(visited) < n:
        cost, node = heappop(heap)
        if node in visited: continue
        visited.add(node)
        total += cost
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heappush(heap, (weight, neighbor))
```

**Virtual node trick** (P3): when "building from scratch" has a cost, model it as edges from node 0.

---

## Complexity Reference

| Problem | Algorithm | Time | Space |
|---|---|---|---|
| P1 Min Cost Connect | Prim's | O(n² log n) | O(n) |
| P2 MST Kruskal | Kruskal's | O(E log E) | O(V) |
| P3 Water Distribution | Kruskal's + virtual node | O(E log E) | O(V) |
| P4 Critical Edges | Kruskal's × 2E | O(E² log E) | O(V) |
| P5 Connecting Cities | Kruskal's | O(E log E) | O(V) |
