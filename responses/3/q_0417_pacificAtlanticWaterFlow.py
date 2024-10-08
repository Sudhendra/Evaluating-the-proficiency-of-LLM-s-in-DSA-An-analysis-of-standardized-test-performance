class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        pacific = set()
        atlantic = set()
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c, ocean):
            ocean.add((r, c))
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in ocean and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, ocean)
                    
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols-1, atlantic)
        for i in range(cols):
            dfs(0, i, pacific)
            dfs(rows-1, i, atlantic)
        
        return list(pacific.intersection(atlantic))