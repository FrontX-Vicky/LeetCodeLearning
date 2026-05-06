# Day 20: Union Find (Disjoint Set Union)

**Date**: January 20, 2026  
**Focus**: Master Union Find for dynamic connectivity problems  
**Difficulty**: Medium–Hard  

---

## 📚 Problems to Solve

### Problem 1: Number of Provinces
**LeetCode**: [#547 - Number of Provinces](https://leetcode.com/problems/number-of-provinces/)

Given an `n×n` adjacency matrix `isConnected`, return the number of provinces (connected components).

**Example**:
```python
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2   # {0,1} are one province, {2} is another

isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3   # all isolated
```

**Key Insights**:
- Process upper triangle only (undirected, so [i][j] == [j][i])
- Union i and j whenever `isConnected[i][j] == 1`
- Final component count = answer

---

### Problem 2: Redundant Connection
**LeetCode**: [#684 - Redundant Connection](https://leetcode.com/problems/redundant-connection/)

A tree with `n` nodes (1-indexed) has been given `n` edges instead of `n-1`. Find and return the last edge that creates a cycle.

**Example**:
```python
edges = [[1,2],[1,3],[2,3]]
Output: [2,3]   # adding [2,3] creates cycle 1→2→3→1

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

**Key Insights**:
- Process edges in order
- `union(u, v)` returns False when already connected → that edge is redundant
- Return the first edge that fails to union

---

### Problem 3: Graph Valid Tree
**LeetCode**: [#261 - Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)

Given `n` nodes and a list of undirected edges, return `True` if they form a valid tree.

**Example**:
```python
n=5, edges=[[0,1],[0,2],[0,3],[1,4]]
Output: True

n=5, edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: False   # cycle exists
```

**A valid tree requires ALL of**:
1. Exactly `n - 1` edges
2. All nodes connected (single component)
3. No cycles

**Key Insights**:
- Check `len(edges) != n-1` first as fast elimination
- Union each edge; if any union fails → cycle → not a tree

---

### Problem 4: Number of Connected Components
**LeetCode**: [#323 - Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)

Given `n` nodes (0-indexed) and a list of undirected edges, count connected components.

**Example**:
```python
n=5, edges=[[0,1],[1,2],[3,4]]
Output: 2   # {0,1,2} and {3,4}

n=5, edges=[[0,1],[1,2],[2,3],[3,4]]
Output: 1   # all connected
```

**Key Insights**:
- Start with `n` components
- Each successful `union()` decrements count by 1
- Return final count

---

### Problem 5: Accounts Merge
**LeetCode**: [#721 - Accounts Merge](https://leetcode.com/problems/accounts-merge/)

Each account is `[name, email1, email2, ...]`. Two accounts belong to the same person if they share any email. Merge them and return sorted email lists with the person's name.

**Example**:
```python
accounts = [
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]
]
Output: [
    ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
    ["John","johnnybravo@mail.com"],
    ["Mary","mary@mail.com"]
]
```

**Key Insights**:
- Emails are nodes; shared email between accounts → union those accounts
- Map each unique email to an integer index for Union Find
- Group emails by root component, sort, prepend name

---

## 🎯 What is Union Find?

Union Find (Disjoint Set Union / DSU) efficiently answers:
> "Are nodes X and Y in the same connected component?"

### Structure:
```
Initial (5 nodes):     After union(0,1), union(1,2):
0  1  2  3  4          0→2  1→2  2  3  4
(each its own root)    (0 and 1 both point to root 2)
```

### Two Core Operations:

**1. `find(x)` — O(α(n)) with path compression**:
```python
def find(self, x):
    if self.parent[x] != x:
        self.parent[x] = self.find(self.parent[x])  # Path compression
    return self.parent[x]
```

**2. `union(x, y)` — O(α(n)) with union by rank**:
```python
def union(self, x, y):
    root_x, root_y = self.find(x), self.find(y)
    if root_x == root_y:
        return False  # Already connected (cycle!)
    # Attach smaller tree under larger
    if self.rank[root_x] < self.rank[root_y]:
        self.parent[root_x] = root_y
    elif self.rank[root_x] > self.rank[root_y]:
        self.parent[root_y] = root_x
    else:
        self.parent[root_y] = root_x
        self.rank[root_x] += 1
    self.components -= 1
    return True
```

---

## 🔑 Key Concepts

### Path Compression
```
Before find(0):    After find(0):
    4                  4
    |                /|\ \
    3               3 2 1 0
    |
    2
    |
    1
    |
    0
```
Every node visited during `find` now points directly to root → future finds O(1).

### Union by Rank
Always attach the shorter tree under the taller tree. Keeps tree height bounded at O(log n).

### Time Complexity with Both Optimizations
- O(α(n)) per operation where α = inverse Ackermann function
- α(n) < 5 for all practical n → effectively O(1)
- Build: O(n), All operations: O(α(n)) ≈ O(1) amortized

### Union Find vs BFS/DFS

| Scenario | Union Find | BFS/DFS |
|----------|-----------|---------|
| "Are X and Y connected?" | ✅ O(α(n)) | ✅ O(V+E) |
| "How many components?" | ✅ O(n) | ✅ O(V+E) |
| "Does edge create cycle?" | ✅ O(α(n)) | ✅ O(V+E) |
| "Shortest path?" | ❌ | ✅ BFS |
| "Actual path between nodes?" | ❌ | ✅ DFS/BFS |
| Edges added dynamically | ✅ | ❌ (re-traverse) |

---

## 💡 Common Patterns

### Pattern 1: Count Components
```python
uf = UnionFind(n)
for u, v in edges:
    uf.union(u, v)
return uf.components
```

### Pattern 2: Cycle Detection
```python
uf = UnionFind(n)
for u, v in edges:
    if not uf.union(u, v):
        # This edge creates a cycle
        return [u, v]
```

### Pattern 3: Valid Tree Check
```python
if len(edges) != n - 1:
    return False
uf = UnionFind(n)
for u, v in edges:
    if not uf.union(u, v):
        return False  # Cycle
return True
```

### Pattern 4: Non-integer Nodes (map to indices)
```python
email_to_idx = {}
idx = 0
for account in accounts:
    for email in account[1:]:
        if email not in email_to_idx:
            email_to_idx[email] = idx
            idx += 1

uf = UnionFind(idx)
for account in accounts:
    first = email_to_idx[account[1]]
    for email in account[2:]:
        uf.union(first, email_to_idx[email])
```

---

## 🎓 Learning Objectives

By the end of Day 20, you should be able to:

1. ☐ Implement UnionFind with path compression and union by rank
2. ☐ Explain why `union()` returning `False` means a cycle was detected
3. ☐ Apply Union Find to connected component counting
4. ☐ Use Union Find for cycle detection in undirected graphs
5. ☐ Map non-integer nodes (emails, strings) to indices for Union Find
6. ☐ Decide when to use Union Find vs BFS/DFS

---

## 📖 Resources

- **Visualizations**:
  - [VisuAlgo - Union Find](https://visualgo.net/en/ufds)

- **Reading**:
  - [Union Find - Wikipedia](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
  - [CP-Algorithms: DSU](https://cp-algorithms.com/data_structures/disjoint_set_union.html)

- **Practice**:
  - LeetCode Union Find Tag: https://leetcode.com/tag/union-find/

---

## ✅ Success Criteria

- [ ] Implement UnionFind class with path compression + union by rank
- [ ] Solve all 5 problems
- [ ] Understand cycle detection via `union()` return value
- [ ] Handle non-integer node mapping (Accounts Merge)
- [ ] Know when Union Find beats BFS/DFS
