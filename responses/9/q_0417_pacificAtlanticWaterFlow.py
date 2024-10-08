from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        def dfs(r, c, prev_height, reachable):
            if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]) or (r, c) in reachable or heights[r][c] < prev_height:
                return

            reachable.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc, heights[r][c], reachable)

        pacific_reachable = set()
        atlantic_reachable = set()

        for r in range(len(heights)):
            dfs(r, 0, float('-inf'), pacific_reachable)
            dfs(r, len(heights[0]) - 1, float('-inf'), atlantic_reachable)

        for c in range(len(heights[0])):
            dfs(0, c, float('-inf'), pacific_reachable)
            dfs(len(heights) - 1, c, float('-inf'), atlantic_reachable)

        return list(pacific_reachable.intersection(atlantic_reachable))
