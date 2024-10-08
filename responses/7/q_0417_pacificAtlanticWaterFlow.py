from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        
        def dfs(r, c, ocean):
            ocean[r][c] = True
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n and not ocean[new_r][new_c] and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, ocean)
        
        pacific = [[False] * n for _ in range(m)]  # reachable cells from Pacific Ocean
        atlantic = [[False] * n for _ in range(m)]  # reachable cells from Atlantic Ocean
        
        for i in range(m):
            dfs(i, 0, pacific)  # check left edge
            dfs(i, n - 1, atlantic)  # check right edge
        
        for j in range(n):
            dfs(0, j, pacific)  # check top edge
            dfs(m - 1, j, atlantic)  # check bottom edge
        
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        
        return result
