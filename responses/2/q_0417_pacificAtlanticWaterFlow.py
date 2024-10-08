from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, ocean):
            if (r, c) in ocean:
                return
            ocean.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, ocean)

        for r in range(rows):
            dfs(r, 0, pacific_reachable)
            dfs(r, cols-1, atlantic_reachable)

        for c in range(cols):
            dfs(0, c, pacific_reachable)
            dfs(rows-1, c, atlantic_reachable)

        return list(pacific_reachable.intersection(atlantic_reachable))
