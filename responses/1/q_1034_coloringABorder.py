class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]:
        def dfs(x, y, target_color):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != target_color:
                return
            visited.add((x, y))
            if any((nx, ny) not in visited and (nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != target_color) for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]):
                border.add((x, y))
            for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (nx, ny) not in visited:
                    dfs(nx, ny, target_color)

        visited, border = set(), set()
        dfs(row, col, grid[row][col])

        for x, y in border:
            grid[x][y] = color

        return grid