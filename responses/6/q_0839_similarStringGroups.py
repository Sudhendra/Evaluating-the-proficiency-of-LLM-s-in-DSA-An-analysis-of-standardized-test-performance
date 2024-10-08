from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(s1, s2):
            diff_count = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 2:
                        return False
            return True
        
        def dfs(node):
            visited.add(node)
            for nei, _ in graph.get(node, []):
                if nei not in visited:
                    dfs(nei)
        
        graph = {}
        for i, s1 in enumerate(strs):
            for j, s2 in enumerate(strs):
                if i != j and is_similar(s1, s2):
                    graph.setdefault(i, []).append((j, 0))
        
        visited = set()
        groups = 0
        for i in range(len(strs)):
            if i not in visited:
                dfs(i)
                groups += 1
        
        return groups
