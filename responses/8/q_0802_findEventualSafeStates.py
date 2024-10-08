from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2
        
        def dfs(node):
            if colors[node] != WHITE:
                return colors[node] == BLACK
            
            colors[node] = GRAY
            for neighbor in graph[node]:
                if colors[neighbor] == BLACK:
                    continue
                if colors[neighbor] == GRAY or not dfs(neighbor):
                    return False
            
            colors[node] = BLACK
            return True
        
        n = len(graph)
        colors = [WHITE] * n
        return [node for node in range(n) if dfs(node)]

# Example usage
solution = Solution()
result = solution.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])
print(result)  # Output: [2, 4, 5, 6]
