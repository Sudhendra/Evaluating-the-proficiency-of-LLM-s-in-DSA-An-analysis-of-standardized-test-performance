from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pacific = set()
        atlantic = set()

        def dfs(row, col, ocean):
            ocean.add((row, col))
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in ocean and heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, ocean)

        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols - 1, atlantic)

        for j in range(cols):
            dfs(0, j, pacific)
            dfs(rows - 1, j, atlantic)

        return list(pacific.intersection(atlantic))
