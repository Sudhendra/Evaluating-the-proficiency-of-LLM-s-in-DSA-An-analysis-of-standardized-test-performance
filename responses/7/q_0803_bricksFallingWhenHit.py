class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]) -> List[int]:
        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != 1:
                return 0
            count = 1
            grid[r][c] = 2
            count += sum(dfs(nr, nc) for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)])
            return count

        def is_stable(r, c):
            return r == 0 or any(grid[nr][nc] == 2 for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)])

        result = []
        
        for r, c in hits:
            if grid[r][c] == 0:
                result.append(0)
            else:
                grid[r][c] = 0
                count_before = sum(row.count(1) for row in grid)
                for nc in range(len(grid[0])):
                    dfs(0, nc)
                
                result.append(max(0, sum(not is_stable(r, c) for r, c in hits) - 1))

        return result
