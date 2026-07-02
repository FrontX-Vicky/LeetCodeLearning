# Day 21: Topological Sort

**Date**: January 21, 2026  
**Focus**: Ordering problems on Directed Acyclic Graphs (DAGs)  
**Difficulty**: Medium–Hard

---

## 📚 Problems to Solve

### Problem 1: Course Schedule
**LeetCode**: [#207 - Course Schedule](https://leetcode.com/problems/course-schedule/)

Given `numCourses` and `prerequisites`, return `True` if you can finish all courses.

**Example**:
```python
numCourses = 2
prerequisites = [[1, 0]]
# 0 -> 1, possible
Output: True

numCourses = 2
prerequisites = [[1, 0], [0, 1]]
# cycle
Output: False
```

---

### Problem 2: Course Schedule II
**LeetCode**: [#210 - Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

Return one valid order to finish all courses. If impossible, return `[]`.

**Example**:
```python
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3]  # or [0,2,1,3]
```

---

### Problem 3: Alien Dictionary
**LeetCode**: [#269 - Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)

Given sorted words in an alien language, derive a valid character order.

**Example**:
```python
words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

---

### Problem 4: Minimum Height Trees
**LeetCode**: [#310 - Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)

Find all roots that produce minimum tree height.

**Example**:
```python
n = 4
edges = [[1,0],[1,2],[1,3]]
Output: [1]
```

---

### Problem 5: Parallel Courses
**LeetCode**: [#1136 - Parallel Courses](https://leetcode.com/problems/parallel-courses/)

Given prerequisite relations, return minimum semesters to finish all courses, or `-1` if impossible.

**Example**:
```python
n = 3
relations = [[1,3],[2,3]]
Output: 2
```

---

## 🎯 What is Topological Sort?

Topological sort is a linear ordering of vertices in a **DAG** such that for every edge `u -> v`, `u` appears before `v`.

Topological sort exists **iff no directed cycle exists**.

---

## 🔑 Core Approaches

### 1) Kahn's Algorithm (BFS + indegree)

- Compute indegree for each node
- Push all nodes with indegree 0 into queue
- Repeatedly pop, append to order, decrement neighbors indegrees
- If processed count < total nodes, cycle exists

**Time**: O(V + E)  
**Space**: O(V + E)

### 2) DFS with 3-color cycle detection

- `0 = unvisited`, `1 = visiting`, `2 = visited`
- DFS each node
- If DFS reaches a `visiting` node, cycle exists
- Add node to order in postorder

**Time**: O(V + E)  
**Space**: O(V + E)

---

## 💡 Patterns to Remember

1. Build graph as adjacency list.
2. Track indegree for BFS topo problems.
3. `processed == n` means acyclic for Kahn's algorithm.
4. Directed cycle detection = impossible schedule/order.
5. For trees (MHT), repeatedly trim leaves layer by layer.

---

## ✅ Success Criteria

- [x] Implement topological sort with Kahn's algorithm
- [x] Detect directed cycles correctly
- [x] Return valid ordering when possible
- [x] Handle edge cases (isolated nodes, disconnected DAGs)
- [x] Solve all 5 problems

---

## 📝 Wrap-Up Notes

**Test Results**: 25/25 passed

### Key Takeaways

- **Kahn's algorithm** is the go-to for all 4 of these problems — build graph + indegree, queue indegree-0 nodes, process layer by layer.
- **Cycle detection** is a free byproduct: if `processed < n` after Kahn's, a cycle blocked the remaining nodes.
- **Alien Dictionary** is just topo sort on a char graph — the tricky part is building edges correctly from adjacent word pairs and catching the invalid prefix edge case (`["abc", "ab"]`).
- **Minimum Height Trees** doesn't need a directed graph — it's Kahn's applied to an undirected tree by trimming leaves inward until ≤ 2 nodes remain (those are always the centroids).
- **Parallel Courses** = layered BFS: process the whole queue per semester, increment semester counter each round.

### Patterns Locked In

| Pattern | When to use |
|---|---|
| `processed == n` | Cycle detection (Kahn's) |
| `len(order) == numCourses` | Valid topo order check |
| `remaining -= layer_size` then `while remaining > 2` | MHT leaf trimming |
| `semester += 1` per BFS layer | Min time / parallel scheduling |
