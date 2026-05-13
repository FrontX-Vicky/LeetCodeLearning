# Day 22: Dijkstra's Shortest Path

**Date**: January 22, 2026  
**Focus**: Weighted shortest-path algorithms on graphs  
**Difficulty**: Medium–Hard

---

## 📚 Problems to Solve

### Problem 1: Network Delay Time
**LeetCode**: [#743 - Network Delay Time](https://leetcode.com/problems/network-delay-time/)

Given a directed weighted graph of `n` nodes and a source `k`, return the time for all nodes to receive a signal, or `-1` if impossible.

**Example**:
```python
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4, k = 2
Output: 2
```

---

### Problem 2: Cheapest Flights Within K Stops
**LeetCode**: [#787 - Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

Find the cheapest price from `src` to `dst` using at most `k` stops. Return `-1` if impossible.

**Example**:
```python
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0, dst = 3, k = 1
Output: 700
```

---

### Problem 3: Path With Minimum Effort
**LeetCode**: [#1631 - Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)

Find the path from top-left to bottom-right of a grid that minimises the maximum absolute difference between consecutive cells.

**Example**:
```python
heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2  # path 1->3->5->3->5, max diff = 2
```

---

### Problem 4: Swim in Rising Water
**LeetCode**: [#778 - Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

Given an `n×n` grid where `grid[i][j]` is the elevation, find the minimum time `t` to travel from `(0,0)` to `(n-1,n-1)`.

**Example**:
```python
grid = [[0,2],[1,3]]
Output: 3
```

---

### Problem 5: Find the City With Smallest Number of Neighbors
**LeetCode**: [#1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

Return the city with the fewest reachable cities within `distanceThreshold`. Ties: return the city with the larger index.

**Example**:
```python
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
Output: 3
```

---

## 🎯 What is Dijkstra's Algorithm?

Dijkstra's finds the **shortest path from a single source** to all other nodes in a graph with **non-negative edge weights**.

Core idea: always relax the cheapest unvisited node next (greedy).

---

## 🔑 Core Template

```python
import heapq
from collections import defaultdict

def dijkstra(graph, src, n):
    dist = [float('inf')] * n
    dist[src] = 0
    min_heap = [(0, src)]   # (cost, node)

    while min_heap:
        cost, node = heapq.heappop(min_heap)

        if cost > dist[node]:   # stale entry
            continue

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(min_heap, (new_cost, neighbor))

    return dist
```

**Time**: O((V + E) log V)  
**Space**: O(V + E)

---

## 🔑 Variants

### Bellman-Ford (K-stops constraint)
- Relax all edges `k+1` times
- Each round = one hop/stop limit
- O(V × E) — slower but handles hop limits

### Floyd-Warshall (All-pairs shortest path)
- DP: `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`
- O(V³) — only practical for small graphs

---

## 💡 Patterns to Remember

1. Min-heap always pops the globally cheapest node next.
2. Skip stale heap entries: `if cost > dist[node]: continue`
3. For **K-stops** problems, copy the dist array before each relaxation round (Bellman-Ford style).
4. Grid problems: treat each cell as a node; 4-directional edges.
5. "Minimax path" → Dijkstra where edge weight = `max(current_effort, |a - b|)`.

---

## ✅ Success Criteria

- [ ] Implement Dijkstra's with min-heap correctly
- [ ] Handle stale heap entries
- [ ] Apply Bellman-Ford for K-stops constraint
- [ ] Extend Dijkstra to grid problems
- [ ] Solve all 5 problems
