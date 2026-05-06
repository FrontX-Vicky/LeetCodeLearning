# Main.py - Your Working File
# Task: Implement Union Find (Disjoint Set Union)
# Goal: Master efficient connected component tracking

from typing import List
from collections import defaultdict


# ============================================================
# UNION FIND DATA STRUCTURE
# ============================================================

class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure.

    Efficiently answers: "Are nodes x and y in the same component?"

    Two core operations:
    - find(x): Return root/representative of x's component
    - union(x, y): Merge components containing x and y

    Optimizations:
    - Path Compression: During find, make every node point directly to root
    - Union by Rank: Always attach the shorter tree under the taller one

    Time: O(α(n)) amortized per operation (α = inverse Ackermann ≈ O(1))
    Space: O(n)
    """

    def __init__(self, n: int):
        """Initialize n nodes, each in its own component"""
        # TODO: Initialize parent array (self.parent = list(range(n)))
        # TODO: Initialize rank array (all zeros)
        # TODO: Initialize self.components = n
        pass

    def find(self, x: int) -> int:
        """
        Find root of x's component with path compression.

        Path Compression: If self.parent[x] != x, recursively find the root
        AND reassign self.parent[x] = root along the way.
        This flattens the tree so future finds hit root in one hop.

        Example: chain 0→1→2→3 (root)
        After find(0): 0→3, 1→3, 2→3 (all direct to root)
        """
        # TODO: Implement find with path compression
        # Hint: if self.parent[x] != x:
        #           self.parent[x] = self.find(self.parent[x])
        #       return self.parent[x]
        pass

    def union(self, x: int, y: int) -> bool:
        """
        Merge components of x and y.

        Union by Rank: Attach the tree with lower rank under the one with
        higher rank. If equal, pick one as root and increment its rank.

        Returns:
            True  - merged successfully (x and y were in different components)
            False - already connected (x and y share a root) → CYCLE DETECTED
        """
        # TODO: Implement union by rank
        # 1. root_x = self.find(x), root_y = self.find(y)
        # 2. If root_x == root_y: return False
        # 3. Union by rank (attach lower-rank tree under higher-rank)
        # 4. If equal ranks: pick root_x as root, increment self.rank[root_x]
        # 5. Decrement self.components by 1
        # 6. Return True
        pass

    def connected(self, x: int, y: int) -> bool:
        """Return True if x and y are in the same component"""
        # TODO: return self.find(x) == self.find(y)
        pass


# ============================================================
# PROBLEM 1: NUMBER OF PROVINCES
# ============================================================

def findCircleNum(isConnected: List[List[int]]) -> int:
    """
    Count provinces (connected components) in adjacency matrix.

    LeetCode #547

    Example:
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2   ({0,1} one province, {2} another)

    Approach: Union Find
    1. Initialize UnionFind(n)
    2. Iterate upper triangle (i < j) to avoid double-processing
    3. Union i and j whenever isConnected[i][j] == 1
    4. Return uf.components

    Time: O(n²)  — must process all matrix cells
    Space: O(n)
    """
    # TODO: Implement number of provinces
    pass


# ============================================================
# PROBLEM 2: REDUNDANT CONNECTION
# ============================================================

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    """
    Find the edge that introduces a cycle in an undirected graph.

    LeetCode #684

    Nodes are 1-indexed. Graph starts as a tree (n-1 edges) and one extra
    edge is added — return that extra edge.

    Example:
    edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]   (creates cycle 1→2→3→1)

    Approach: Union Find
    1. Process edges in order
    2. For each (u, v): try uf.union(u, v)
    3. If union returns False → cycle detected → return [u, v]

    Time: O(n α(n)) ≈ O(n)
    Space: O(n)
    """
    # TODO: Implement redundant connection
    # Note: nodes are 1-indexed, so initialize UnionFind(n + 1)
    pass


# ============================================================
# PROBLEM 3: GRAPH VALID TREE
# ============================================================

def validTree(n: int, edges: List[List[int]]) -> bool:
    """
    Return True if n nodes + given edges form a valid tree.

    LeetCode #261

    A valid tree requires:
    1. Exactly n-1 edges  (fewer = disconnected, more = has cycle)
    2. No cycles
    3. All nodes connected

    Example:
    n=5, edges=[[0,1],[0,2],[0,3],[1,4]]  → True
    n=5, edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]  → False (cycle)

    Approach: Union Find
    1. Fast check: if len(edges) != n-1: return False
    2. Union each edge; if any fails → cycle → False
    3. Return True  (n-1 edges + no cycles = exactly 1 component)

    Time: O(n α(n)) ≈ O(n)
    Space: O(n)
    """
    # TODO: Implement valid tree check
    pass


# ============================================================
# PROBLEM 4: NUMBER OF CONNECTED COMPONENTS
# ============================================================

def countComponents(n: int, edges: List[List[int]]) -> int:
    """
    Count connected components in an undirected graph.

    LeetCode #323

    Example:
    n=5, edges=[[0,1],[1,2],[3,4]]
    Output: 2  ({0,1,2} and {3,4})

    n=5, edges=[[0,1],[1,2],[2,3],[3,4]]
    Output: 1

    Approach: Union Find
    1. Start with n components
    2. Union each edge (decrements components when merged)
    3. Return uf.components

    Time: O((n + e) α(n)) ≈ O(n + e)
    Space: O(n)
    """
    # TODO: Implement count connected components
    pass


# ============================================================
# PROBLEM 5: ACCOUNTS MERGE
# ============================================================

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    """
    Merge accounts that share at least one email address.

    LeetCode #721

    Each account: [name, email1, email2, ...]
    Two accounts belong to the same person if they share any email.
    Output: merged accounts with emails sorted, name prepended.

    Example:
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

    Approach: Union Find on email indices
    1. Assign each unique email a unique integer index
    2. For each account, union all its emails together (same account = same component)
    3. Group emails by root component
    4. Sort each group and prepend the account owner's name

    Time: O(NK log(NK))  N = accounts, K = avg emails per account
    Space: O(NK)
    """
    # TODO: Implement accounts merge
    # Hint:
    # email_to_idx = {}   (maps email string → int index)
    # email_to_name = {}  (maps email string → owner name)
    # idx = 0
    # Pass 1: assign indices and names
    # Pass 2: union emails within same account
    # Pass 3: group emails by root using uf.find()
    # Pass 4: sort each group and prepend name
    pass


# ============================================================
# SMOKE TESTS
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("UNION FIND (DISJOINT SET) - SMOKE TESTS")
    print("=" * 60)

    # Test core UnionFind
    print("\n" + "-" * 60)
    print("CORE: UNION FIND DATA STRUCTURE")
    print("-" * 60)
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    print(f"connected(0, 2): {uf.connected(0, 2)}")
    print(f"Expected: True")
    print(f"connected(0, 3): {uf.connected(0, 3)}")
    print(f"Expected: False")
    print(f"components: {uf.components}")
    print(f"Expected: 3")

    # Test 1: Number of Provinces
    print("\n" + "-" * 60)
    print("PROBLEM 1: NUMBER OF PROVINCES")
    print("-" * 60)
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    result = findCircleNum(isConnected)
    print(f"Result: {result}")
    print(f"Expected: 2")

    isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]
    result2 = findCircleNum(isConnected2)
    print(f"All isolated: {result2}")
    print(f"Expected: 3")

    # Test 2: Redundant Connection
    print("\n" + "-" * 60)
    print("PROBLEM 2: REDUNDANT CONNECTION")
    print("-" * 60)
    edges = [[1,2],[1,3],[2,3]]
    result = findRedundantConnection(edges)
    print(f"Redundant edge: {result}")
    print(f"Expected: [2, 3]")

    # Test 3: Graph Valid Tree
    print("\n" + "-" * 60)
    print("PROBLEM 3: GRAPH VALID TREE")
    print("-" * 60)
    print(f"Valid tree: {validTree(5, [[0,1],[0,2],[0,3],[1,4]])}")
    print(f"Expected: True")
    print(f"Has cycle: {validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])}")
    print(f"Expected: False")

    # Test 4: Count Components
    print("\n" + "-" * 60)
    print("PROBLEM 4: NUMBER OF CONNECTED COMPONENTS")
    print("-" * 60)
    print(f"2 components: {countComponents(5, [[0,1],[1,2],[3,4]])}")
    print(f"Expected: 2")
    print(f"1 component: {countComponents(5, [[0,1],[1,2],[2,3],[3,4]])}")
    print(f"Expected: 1")

    # Test 5: Accounts Merge
    print("\n" + "-" * 60)
    print("PROBLEM 5: ACCOUNTS MERGE")
    print("-" * 60)
    accounts = [
        ["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]
    ]
    result = accountsMerge(accounts)
    print(f"Merged to {len(result) if result else 'N/A'} accounts")
    print(f"Expected: 3")

    print("\n" + "=" * 60)
    print("Run 'python test_cases.py' for full test suite!")
    print("=" * 60)
