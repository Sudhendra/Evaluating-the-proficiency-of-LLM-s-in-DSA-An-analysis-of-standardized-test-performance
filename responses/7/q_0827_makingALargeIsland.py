from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, index):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1:
                return 0
            grid[r][c] = index
            return 1 + sum(dfs(grid, nr, nc, index) for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)))

        area = {}  # Map index to area size
        index = 2  # Start index for assigning different groups (1 is reserved for original 1s)
        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area[index] = dfs(grid, r, c, index)
                    res = max(res, area[index])
                    index += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    seen = set()
                    cur_area = 1
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 0 and grid[nr][nc] not in seen:
                            seen.add(grid[nr][nc])
                            cur_area += area[grid[nr][nc]]
                    res = max(res, cur_area)

        return res

# Unit Tests
solution = Solution()
print(solution.largestIsland([[1,0],[0,1]]))  # Output: 3
print(solution.largestIsland([[1,1],[1,0]]))  # Output: 4
print(solution.largestIsland([[1,1],[1,1]]))  # Output: 4
