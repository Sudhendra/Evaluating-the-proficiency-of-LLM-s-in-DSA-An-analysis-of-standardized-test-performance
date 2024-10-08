from typing import List

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        all_keys = set()
        startRow, startCol = 0, 0

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == '@':
                    startRow, startCol = r, c
                if 'a' <= grid[r][c] <= 'z':
                    all_keys.add(grid[r][c])

        def bfs(r, c, keys):
            queue = [(r, c, keys, 0)]
            visited = set((r, c, keys))

            while queue:
                row, col, collected_keys, steps = queue.pop(0)

                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc

                    if 0 <= new_r < row_len and 0 <= new_c < col_len:
                        cell = grid[new_r][new_c]

                        if cell in collected_keys or cell == '.' or cell == '@':
                            if (new_r, new_c, collected_keys) not in visited:
                                if 'A' <= cell <= 'Z' and cell.lower() not in collected_keys:
                                    continue

                                if cell.islower() and cell not in collected_keys:
                                    new_keys = collected_keys + cell
                                    if set(new_keys) == all_keys:
                                        return steps + 1

                                    queue.append((new_r, new_c, new_keys, steps + 1))
                                    visited.add((new_r, new_c, new_keys))
                                else:
                                    queue.append((new_r, new_c, collected_keys, steps + 1))
                                    visited.add((new_r, new_c, collected_keys))

        result = bfs(startRow, startCol, '')
        return result if result is not None else -1
