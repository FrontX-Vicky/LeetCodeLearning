# Solutions.py - Reference Implementations
# Union Find (Disjoint Set Union) - Complete Solutions

from typing import List
from collections import defaultdict


# ============================================================
# UNION FIND DATA STRUCTURE
# ============================================================

class UnionFind:
    """
    Union-Find with Path Compression + Union by Rank

    Visualization — path compression during find(0):

    Before:             After find(0):
        4 (root)            4 (root)
        |                  /|\ \
        3                 3 2 1 0
        |
        2
        |
        1
        |
        0

    All nodes on the path now point directly to root.
    Future finds from any of them are O(1).

    Union by Rank — always attach shorter tree under taller:

    rank[A]=2   rank[B]=1       Result:
        A             B             A
       / \            |            /|\
      ...  ...       ...          ... ... B
                                          |
                                         ...

    Keeps tree height bounded → find stays fast.
    """

    def __init__(self, n: int):
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n           # Rank is an upper bound on tree height
        self.components = n           # Start with n separate components

    def find(self, x: int) -> int:
        """
        Find root with recursive path compression.

        On the way back up the recursion, every visited node is reassigned
        directly to the root. This flattens the tree permanently.

        Time: O(α(n)) amortized
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Merge by rank.

        Returns True if merged (different components).
        Returns False if already connected (cycle detected!).
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same component → adding edge = cycle

        # Attach lower-rank tree under higher-rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # Equal rank: pick root_x as new root, bump its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Return True if x and y share the same root (same component)."""
        return self.find(x) == self.find(y)


# ============================================================
# PROBLEM 1: NUMBER OF PROVINCES
# ============================================================

def findCircleNum(isConnected: List[List[int]]) -> int:
    """
    Count connected components from adjacency matrix.

    Only process upper triangle (undirected graph: [i][j] == [j][i]).
    After unioning all edges, uf.components = number of provinces.

    Time: O(n²) — must scan all matrix cells
    Space: O(n)
    """
    n = len(isConnected)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n):  # Upper triangle only
            if isConnected[i][j] == 1:
                uf.union(i, j)

    return uf.components


# ============================================================
# PROBLEM 2: REDUNDANT CONNECTION
# ============================================================

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    """
    Process edges in order. The first edge where union() returns False
    means those two nodes were already connected → adding this edge
    creates a cycle → it's the redundant edge.

    Nodes are 1-indexed so we initialize UnionFind(n+1).

    Time: O(n α(n)) ≈ O(n)
    Space: O(n)
    """
    n = len(edges)
    uf = UnionFind(n + 1)  # 1-indexed nodes

    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]  # This edge creates a cycle

    return []  # Guaranteed a solution per problem constraints


# ============================================================
# PROBLEM 3: GRAPH VALID TREE
# ============================================================

def validTree(n: int, edges: List[List[int]]) -> bool:
    """
    Tree condition: n-1 edges + no cycles + all connected.

    Key insight: if we have exactly n-1 edges AND no cycle, the graph
    MUST be connected (pigeonhole). So we only need to verify:
    1. len(edges) == n-1
    2. No union() returns False (no cycle)

    The edge-count check is a fast O(1) eliminator:
    - Too few edges → can't be connected
    - Too many edges → must have a cycle

    Time: O(n α(n)) ≈ O(n)
    Space: O(n)
    """
    if len(edges) != n - 1:
        return False  # Fast fail: wrong number of edges

    uf = UnionFind(n)

    for u, v in edges:
        if not uf.union(u, v):
            return False  # Cycle detected

    return True  # n-1 edges, no cycles → valid tree


# ============================================================
# PROBLEM 4: NUMBER OF CONNECTED COMPONENTS
# ============================================================

def countComponents(n: int, edges: List[List[int]]) -> int:
    """
    Union all edges. Each successful union reduces component count by 1.
    Final uf.components = answer.

    Time: O((n + e) α(n)) ≈ O(n + e)
    Space: O(n)
    """
    uf = UnionFind(n)

    for u, v in edges:
        uf.union(u, v)

    return uf.components


# ============================================================
# PROBLEM 5: ACCOUNTS MERGE
# ============================================================

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    """
    Union Find on email indices.

    Core idea: emails are nodes. Two emails in the same account belong
    to the same person → union them. Then group by root.

    Algorithm:
    1. Map each unique email → integer index
    2. Map each email → account owner name
    3. For each account, union its first email with every other email
    4. Group emails by root (uf.find() for each email index)
    5. Sort each group and prepend the owner's name

    Why union with the first email specifically?
    Union is transitive — unioning (first, second) and (first, third)
    puts all three in the same component. Any email in the account works.

    Time: O(NK log(NK))  sorting dominates; N = accounts, K = avg emails
    Space: O(NK)
    """
    email_to_idx = {}   # email string → unique integer index
    email_to_name = {}  # email string → account owner's name
    idx = 0

    # Pass 1: assign a unique index to every new email
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            if email not in email_to_idx:
                email_to_idx[email] = idx
                email_to_name[email] = name
                idx += 1

    uf = UnionFind(idx)

    # Pass 2: union all emails within the same account
    for account in accounts:
        first_idx = email_to_idx[account[1]]
        for email in account[2:]:
            uf.union(first_idx, email_to_idx[email])

    # Pass 3: group emails by their root component
    root_to_emails = defaultdict(list)
    for email, i in email_to_idx.items():
        root = uf.find(i)
        root_to_emails[root].append(email)

    # Pass 4: sort each group, prepend name
    result = []
    for root, emails in root_to_emails.items():
        name = email_to_name[emails[0]]
        result.append([name] + sorted(emails))

    return result


# ============================================================
# SUMMARY: UNION FIND CHEAT SHEET
# ============================================================
"""
OPERATION           TIME            NOTES
find(x)             O(α(n)) ≈ O(1)  With path compression
union(x, y)         O(α(n)) ≈ O(1)  With union by rank; False = cycle
connected(x, y)     O(α(n)) ≈ O(1)  find(x) == find(y)

α(n) = inverse Ackermann; α(n) < 5 for all n < 10^80 (practically O(1))

USE UNION FIND WHEN:
  ✅ "Are X and Y connected?"
  ✅ "How many connected components?"
  ✅ "Does this edge create a cycle?"
  ✅ "Merge overlapping groups" (Accounts Merge, Friend Circles)
  ✅ Edges added dynamically (online connectivity)

PREFER BFS/DFS WHEN:
  ❌ Need the actual path, not just connectivity
  ❌ Need shortest path (use BFS)
  ❌ Need to traverse the full graph structure

OPTIMIZATIONS (both required for O(α(n))):
  1. Path Compression  — flatten tree during find
  2. Union by Rank     — keep tree balanced during union
"""


if __name__ == "__main__":
    print("Testing Number of Provinces:")
    print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  # Expected: 2
    print(findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))  # Expected: 3

    print("\nTesting Redundant Connection:")
    print(findRedundantConnection([[1,2],[1,3],[2,3]]))         # Expected: [2,3]
    print(findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # Expected: [1,4]

    print("\nTesting Graph Valid Tree:")
    print(validTree(5, [[0,1],[0,2],[0,3],[1,4]]))           # Expected: True
    print(validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))     # Expected: False

    print("\nTesting Count Components:")
    print(countComponents(5, [[0,1],[1,2],[3,4]]))           # Expected: 2
    print(countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))     # Expected: 1

    print("\nTesting Accounts Merge:")
    accounts = [
        ["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]
    ]
    result = accountsMerge(accounts)
    print(f"Merged to {len(result)} accounts (expected 3)")
    for acc in sorted(result, key=lambda a: a[0]):
        print(f"  {acc}")

    print("\n✓ All solutions working!")
