# Solutions.py - Reference Implementations
# Day 21: Topological Sort

from collections import defaultdict, deque
from typing import List


# ============================================================
# PROBLEM 1: COURSE SCHEDULE
# ============================================================

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Kahn's algorithm for cycle detection in directed graph.

    If we can process all nodes using indegree-0 queue, graph is acyclic.
    Otherwise a cycle blocks remaining nodes.
    """
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque(i for i in range(numCourses) if indegree[i] == 0)
    processed = 0

    while queue:
        node = queue.popleft()
        processed += 1

        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return processed == numCourses


# ============================================================
# PROBLEM 2: COURSE SCHEDULE II
# ============================================================

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """Return one valid topological order, else []."""
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque(i for i in range(numCourses) if indegree[i] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return order if len(order) == numCourses else []


# ============================================================
# PROBLEM 3: ALIEN DICTIONARY
# ============================================================

def alienOrder(words: List[str]) -> str:
    """
    Build precedence graph among characters from adjacent words.
    Then topological sort chars.
    """
    # Initialize indegree for all unique chars first.
    indegree = {c: 0 for word in words for c in word}
    graph = defaultdict(set)

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]

        # Invalid prefix case.
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""

        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1
                break

    queue = deque(c for c in indegree if indegree[c] == 0)
    order = []

    while queue:
        char = queue.popleft()
        order.append(char)

        for nxt in graph[char]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return "".join(order) if len(order) == len(indegree) else ""


# ============================================================
# PROBLEM 4: MINIMUM HEIGHT TREES
# ============================================================

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    """
    Peel leaves from the outside inward.
    Last remaining 1-2 nodes are centroids (MHT roots).
    """
    if n <= 2:
        return list(range(n))

    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    leaves = deque(node for node in range(n) if len(graph[node]) == 1)
    remaining = n

    while remaining > 2:
        layer_size = len(leaves)
        remaining -= layer_size

        for _ in range(layer_size):
            leaf = leaves.popleft()
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                leaves.append(neighbor)

    return list(leaves)


# ============================================================
# PROBLEM 5: PARALLEL COURSES
# ============================================================

def minimumSemesters(n: int, relations: List[List[int]]) -> int:
    """
    Layered Kahn's algorithm.
    Each BFS layer = one semester.
    """
    graph = defaultdict(list)
    indegree = [0] * (n + 1)

    for pre, course in relations:
        graph[pre].append(course)
        indegree[course] += 1

    queue = deque(i for i in range(1, n + 1) if indegree[i] == 0)
    taken = 0
    semester = 0

    while queue:
        semester += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            taken += 1

            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

    return semester if taken == n else -1


if __name__ == "__main__":
    print("canFinish:", canFinish(2, [[1, 0]]), "Expected: True")
    print("findOrder:", findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]), "Expected valid order")
    print("alienOrder:", alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), "Expected: wertf")
    print("findMinHeightTrees:", findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]), "Expected: [1]")
    print("minimumSemesters:", minimumSemesters(3, [[1, 3], [2, 3]]), "Expected: 2")
