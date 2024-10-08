from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(s1, s2):
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2:
                        return False
            return diff == 2 or diff == 0
        
        def dfs(node, visited, graphs):
            visited.add(node)
            for neighbor in graphs[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, graphs)
        
        n = len(strs)
        graphs = {i: [] for i in range(n)}

        for i in range(n):
            for j in range(i+1, n):
                if is_similar(strs[i], strs[j]):
                    graphs[i].append(j)
                    graphs[j].append(i)
        
        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i, visited, graphs)
                count += 1
        
        return count
