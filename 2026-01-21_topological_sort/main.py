# Main.py - Your Working File
# Task: Topological Sort patterns in DAGs
# Goal: Master ordering + cycle detection in directed graphs

from collections import defaultdict, deque
from typing import List


# ============================================================
# PROBLEM 1: COURSE SCHEDULE
# ============================================================

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    LeetCode #207

    Return True if all courses can be finished.

    Approach: Kahn's Algorithm (BFS Topological Sort)
    - Build graph prereq -> course
    - indegree[course] counts prerequisites remaining
    - Process all indegree-0 nodes
    - If processed count == numCourses => no cycle
    """
    # TODO: Implement Kahn's algorithm
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
    """
    LeetCode #210

    Return one valid topological order of courses.
    Return [] if impossible (cycle exists).
    """
    # TODO: Implement BFS topo sort and return order list
    graph = defaultdict(list)
    indegree = [0] * numCourses

    for course,prereq in prerequisites:
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
    LeetCode #269

    Given words sorted by alien dictionary order, infer one valid order
    of characters. Return "" if invalid.

    Key invalid case:
    If word1 starts with word2 and len(word1) > len(word2), ordering invalid.
    Example: ["abc", "ab"] -> invalid
    """
    # TODO: Build character graph and run topological sort on chars
    indegree = {c: 0 for word in words for c in word}
    graph = defaultdict(set)

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]

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
    LeetCode #310

    Return all roots that form Minimum Height Trees.

    Approach: Trim leaves layer-by-layer (topological peeling on undirected tree)
    until <= 2 nodes remain.
    """
    # TODO: Implement leaf trimming BFS
    if n <= 2:
        return list(range(n))
    
    graph = defaultdict(set)
    for u,v in edges:
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
    LeetCode #1136

    Return minimum semesters needed to complete all courses.
    You can take any number of courses in a semester as long as prerequisites
    are satisfied. Return -1 if impossible.

    Approach: Layered Kahn's algorithm
    Each BFS layer = one semester.
    """
    # TODO: Implement layered BFS topo sort
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


# ============================================================
# SMOKE TESTS
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TOPOLOGICAL SORT - SMOKE TESTS")
    print("=" * 60)

    # Problem 1
    print("\nPROBLEM 1: COURSE SCHEDULE")
    print(canFinish(2, [[1, 0]]), "Expected: True")
    print(canFinish(2, [[1, 0], [0, 1]]), "Expected: False")

    # Problem 2
    print("\nPROBLEM 2: COURSE SCHEDULE II")
    print(findOrder(2, [[1, 0]]), "Expected: [0, 1]")

    # Problem 3
    print("\nPROBLEM 3: ALIEN DICTIONARY")
    print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), "Expected: wertf (or equivalent)")

    # Problem 4
    print("\nPROBLEM 4: MINIMUM HEIGHT TREES")
    print(findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]), "Expected: [1]")

    # Problem 5
    print("\nPROBLEM 5: PARALLEL COURSES")
    print(minimumSemesters(3, [[1, 3], [2, 3]]), "Expected: 2")

    print("\n" + "=" * 60)
    print("Run 'python test_cases.py' for full test suite!")
    print("=" * 60)
