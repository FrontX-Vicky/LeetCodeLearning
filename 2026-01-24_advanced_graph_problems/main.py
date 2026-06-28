from collections import defaultdict
from collections import deque
from typing import List
import collections

# ============================================================
# PROBLEM 1: RECONSTRUCT ITINERARY (Eulerian Path)
# LeetCode #332 - Hard
# ============================================================

def findItinerary(tickets: List[List[str]]) -> List[str]:
    """
    Given a list of airline tickets represented by pairs of departure
    and arrival airports [from, to], reconstruct the itinerary in order.
    All of the tickets belong to a man who departs from "JFK".
    If there are multiple valid itineraries, return the one with the
    smallest lexical order when read as a single string.
    """
    # TODO: Implement Eulerian Path algorithm (Hierholzer's Algorithm)
    adj = collections.defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        adj[src].append(dst)
    
    res = []
    def dfs(src):
        while adj[src]:
            dst = adj[src].pop()
            dfs(dst)
        res.append(src)
    
    dfs("JFK")
    return res[::-1]


# ============================================================
# PROBLEM 2: IS GRAPH BIPARTITE? (Graph Coloring)
# LeetCode #785 - Medium
# ============================================================

def isBipartite(graph: List[List[int]]) -> bool:
    """
    There is an undirected graph with n nodes, where each node is numbered
    between 0 and n - 1. You are given a 2D array graph, where graph[u]
    is an array of nodes that node u is adjacent to.
    Return true if and only if it is bipartite.
    """
    # TODO: Implement BFS or DFS graph coloring
    n = len(graph)
    colors = [0] * n 

    for i in range(n):
        if colors[i] != 0:
            continue
        
        #BFS
        q = collections.deque([i])
        colors[i] = 1

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if colors[nei] == colors[node]:
                    return False
                if colors[nei] == 0:
                    colors[nei] = -colors[node]
                    q.append(nei)
    
    return True


# ============================================================
# PROBLEM 3: WORD LADDER (Bidirectional BFS)
# LeetCode #127 - Hard
# ============================================================

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    A transformation sequence from word beginWord to word endWord using a
    dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
    - Every adjacent pair of words differs by a single letter.
    - Every si for 1 <= i <= k is in wordList.
    Given two words, beginWord and endWord, and a dictionary wordList,
    return the number of words in the shortest transformation sequence.
    """
    # TODO: Implement shortest path using BFS
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    
    q = deque([(beginWord, 1)])

    while q:
        word, steps = q.popleft()
        if word == endWord:
            return steps
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i + 1:]
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    q.append((new_word, steps + 1))

    return 0



# ============================================================
# PROBLEM 4: CRITICAL CONNECTIONS IN A NETWORK (Tarjan's)
# LeetCode #1192 - Hard
# ============================================================

def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    """
    There are n servers numbered from 0 to n - 1 connected by undirected server-to-server 
    connections forming a network where connections[i] = [a, b] represents a connection between servers a and b.
    A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
    Return all critical connections in the network in any order.
    """
    # TODO: Implement Tarjan's Bridge-Finding Algorithm
    adj = defaultdict(list)
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)

    discovery = [-1] * n
    lowest = [-1] * n
    res = []
    time = 0

    def dfs(node, parent):
        nonlocal time
        discovery[node] = lowest[node] = time
        time += 1

        for nei in adj[node]:
            if nei == parent:
                continue
            if discovery[nei] == -1:
                dfs(nei, node)
                lowest[node] = min(lowest[node], lowest[nei])
                if lowest[nei] > discovery[node]:
                    res.append([node, nei])
            else:
                lowest[node] = min(lowest[node], discovery[nei])
    
    dfs(0, -1)
    return res


def main():
    print("=" * 60)
    print("DAY 24: ADVANCED GRAPH PROBLEMS")
    print("=" * 60)
    print("Run `python test_cases.py` to test your solutions!")
    print("=" * 60)

if __name__ == "__main__":
    main()
