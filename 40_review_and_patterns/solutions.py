from typing import List
from collections import Counter, defaultdict, deque

class CapstoneProblems:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
            
        dict_t = Counter(t)
        required = len(dict_t)
        
        l, r = 0, 0
        formed = 0
        window_counts = defaultdict(int)
        
        ans = float("inf"), None, None
        
        while r < len(s):
            character = s[r]
            window_counts[character] += 1
            
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
                
            while l <= r and formed == required:
                character = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                    
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                    
                l += 1
                
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0
