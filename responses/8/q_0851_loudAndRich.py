from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for u, v in richer:
            graph[v].append(u)
        
        def dfs(node):
            if dp[node] >= 0:
                return dp[node]
            ans = node
            for neighbor in graph[node]:
                candidate = dfs(neighbor)
                if quiet[candidate] < quiet[ans]:
                    ans = candidate
            dp[node] = ans
            return ans
        
        dp = [-1] * n
        return [dfs(i) for i in range(n)]

# Example usage
solution = Solution()
result = solution.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0])
print(result)  # Output: [5,5,2,5,4,5,6,7]
