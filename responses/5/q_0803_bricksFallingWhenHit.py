from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])

        # Helper function to check if a brick is stable
        def is_stable(r, c):
            if r == 0:
                return True
            if any(0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2 for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]):
                return True
            return False

        # Helper function to DFS to mark connected stable bricks
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != 1:
                return 0
            count = 1
            grid[r][c] = 2
            count += sum(dfs(nr, nc) for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)])
            return count

        # Mark all hits as empty spaces
        for r, c in hits:
            if grid[r][c] == 1:
                grid[r][c] = 0

        # Mark all top row bricks as stable
        for c in range(cols):
            dfs(0, c)

        # Revert all hit empty spaces back to bricks
        result = []
        for r, c in reversed(hits):
            if grid[r][c] == 0:
                grid[r][c] = 1
                if is_stable(r, c):
                    count = dfs(r, c) - 1
                    result.append(count)
                else:
                    result.append(0)

        return result[::-1]
