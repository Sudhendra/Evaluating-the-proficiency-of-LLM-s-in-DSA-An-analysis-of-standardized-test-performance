from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(heights), len(heights[0])

        def dfs(row, col, ocean):
            if (row, col) in ocean:
                return
            ocean.add((row, col))
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n and heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, ocean)

        pacific = set()
        atlantic = set()

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)

        for i in range(n):
            dfs(0, i, pacific)
            dfs(m - 1, i, atlantic)

        return list(pacific.intersection(atlantic))
