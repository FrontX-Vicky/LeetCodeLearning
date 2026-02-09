# Day 18: Graphs - BFS & DFS

**Date**: January 18, 2026  
**Focus**: Master graph traversal algorithms (Breadth-First Search & Depth-First Search)

---

## 📚 Today's Problems

### Problem 1: Number of Islands
- **LeetCode**: [#200 - Number of Islands](https://leetcode.com/problems/number-of-islands/)
- **Difficulty**: Medium
- **Approach**: DFS or BFS to mark connected components

### Problem 2: Clone Graph
- **LeetCode**: [#133 - Clone Graph](https://leetcode.com/problems/clone-graph/)
- **Difficulty**: Medium
- **Approach**: DFS/BFS with hash map for visited nodes

### Problem 3: Pacific Atlantic Water Flow
- **LeetCode**: [#417 - Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- **Difficulty**: Medium
- **Approach**: DFS/BFS from both oceans

### Problem 4: Course Schedule
- **LeetCode**: [#207 - Course Schedule](https://leetcode.com/problems/course-schedule/)
- **Difficulty**: Medium
- **Approach**: Topological sort, cycle detection

### Problem 5: Surrounded Regions
- **LeetCode**: [#130 - Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
- **Difficulty**: Medium
- **Approach**: DFS/BFS from border O's

### Problem 6: Rotting Oranges
- **LeetCode**: [#994 - Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
- **Difficulty**: Medium
- **Approach**: BFS level-by-level (multi-source BFS)

---

## 🎯 Learning Objectives

1. **Understand Graph Representations**
   - Adjacency list vs adjacency matrix
   - Directed vs undirected graphs
   - Graph node structure

2. **Master DFS (Depth-First Search)**
   - Recursive implementation
   - Iterative with stack
   - Backtracking pattern
   - Visit tracking

3. **Master BFS (Breadth-First Search)**
   - Queue-based level order
   - Shortest path finding
   - Multi-source BFS
   - Layer tracking

4. **Common Graph Patterns**
   - Connected components
   - Cycle detection
   - Topological sorting
   - Island counting
   - Matrix as graph

---

## 🔑 Key Concepts

### Graph Representations

#### Adjacency List (Most Common)
```python
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
```

#### Adjacency Matrix
```python
graph = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]
```

#### Grid as Graph
```python
grid = [
    ['1', '1', '0'],
    ['1', '0', '0'],
    ['0', '0', '1']
]
# Each cell is a node, neighbors are adjacent cells
```

---

### DFS vs BFS Comparison

| Aspect | DFS | BFS |
|--------|-----|-----|
| Data Structure | Stack (or recursion) | Queue |
| Memory | O(h) height | O(w) width |
| Path Type | Not shortest | Shortest path |
| Implementation | Simpler (recursive) | Iterative with queue |
| Use Case | Exhaust all paths | Level-by-level, shortest |

### DFS Template (Recursive)
```python
def dfs(node, visited):
    if node in visited:
        return
    
    visited.add(node)
    # Process node
    
    for neighbor in graph[node]:
        dfs(neighbor, visited)
```

### BFS Template
```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = {start}
    
    while queue:
        node = queue.popleft()
        # Process node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

## 💡 Problem-Solving Patterns

### Pattern 1: Island Counting (Connected Components)
- Use DFS/BFS to mark entire island
- Count number of DFS/BFS calls
- Mark visited cells

### Pattern 2: Multi-Source BFS
- Start BFS from multiple sources simultaneously
- Track levels/distance
- All sources in initial queue

### Pattern 3: Boundary-First Traversal
- Start from borders/edges
- Mark what's reachable from outside
- Process remaining cells

### Pattern 4: Cycle Detection
- Track visiting state: unvisited, visiting, visited
- If reach "visiting" node again → cycle exists
- Used in course schedule problems

---

## 📝 Implementation Notes

### Files Structure
- `main.py` - Your implementations (work here!)
- `solutions.py` - Reference solutions with detailed comments
- `test_cases.py` - Comprehensive test suite

### Graph Directions (for grid problems)
```python
# 4-directional (up, down, left, right)
directions = [(0,1), (0,-1), (1,0), (-1,0)]

# 8-directional (includes diagonals)
directions = [(0,1), (0,-1), (1,0), (-1,0), 
              (1,1), (1,-1), (-1,1), (-1,-1)]
```

### Workflow
1. Read problem descriptions
2. Implement in `main.py`
3. Run: `python main.py` (smoke tests)
4. Run: `python test_cases.py` (full suite)
5. Compare with `solutions.py` if stuck

---

## 🚀 Getting Started

```bash
cd 2026-01-18_graphs_bfs_dfs
python main.py          # Quick smoke test
python test_cases.py    # Full test suite
```

---

## 📖 Resources

- [Graph Traversal Visualization](https://visualgo.net/en/dfsbfs)
- [LeetCode Graph Problems](https://leetcode.com/tag/graph/)
- [Graph Theory Basics](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)

---

## ✅ Success Criteria

- [ ] Understand graph representations
- [ ] Implement DFS (recursive & iterative)
- [ ] Implement BFS with queue
- [ ] Solve all 6 problems
- [ ] Pass all test cases
- [ ] Recognize when to use DFS vs BFS

---

**Next**: Day 19 - Trie (Prefix Tree)
