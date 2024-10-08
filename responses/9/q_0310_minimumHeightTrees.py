from collections import defaultdict, deque

class Solution:
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        degrees = [0] * n
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degrees[a] += 1
            degrees[b] += 1
        
        leaves = deque([i for i in range(n) if degrees[i] == 1])
        
        while n > 2:
            n -= len(leaves)
            new_leaves = deque()
            
            while leaves:
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        new_leaves.append(neighbor)
            
            leaves = new_leaves
        
        return list(leaves)
