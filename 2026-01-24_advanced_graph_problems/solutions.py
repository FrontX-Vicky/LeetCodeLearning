from typing import List
import collections

def findItinerary(tickets: List[List[str]]) -> List[str]:
    # Eulerian Path (Hierholzer's Algorithm)
    adj = collections.defaultdict(list)
    # Sort backwards so we can pop from the end (O(1) pop)
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

def isBipartite(graph: List[List[int]]) -> bool:
    # Graph Coloring (BFS)
    n = len(graph)
    colors = [0] * n # 0: uncolored, 1: color A, -1: color B
    
    for i in range(n):
        if colors[i] != 0:
            continue
        # BFS
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

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    # Bidirectional BFS (or Standard BFS)
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
        
    q = collections.deque([(beginWord, 1)])
    
    while q:
        word, steps = q.popleft()
        if word == endWord:
            return steps
            
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    q.append((new_word, steps + 1))
                    
    return 0

def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    # Tarjan's Bridge-Finding Algorithm
    adj = collections.defaultdict(list)
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
