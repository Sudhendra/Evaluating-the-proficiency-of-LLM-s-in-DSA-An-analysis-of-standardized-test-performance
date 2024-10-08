from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        all_keys = set()
        start_row, start_col = -1, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start_row, start_col = i, j
                elif 'a' <= grid[i][j] <= 'f':
                    all_keys.add(grid[i][j])

        target = 2 ** len(all_keys) - 1
        queue = deque([(start_row, start_col, 0, "")])
        visited = set([(start_row, start_col, "")])
        
        while queue:
            row, col, steps, keys = queue.popleft()
            if len(keys) == len(all_keys) and all_keys == set(keys):
                return steps

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                new_keys = keys

                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] != '#':
                    cell = grid[new_row][new_col]

                    if 'a' <= cell <= 'f':
                        new_keys = "".join(sorted(keys + cell))
                    
                    if ('A' <= cell <= 'F' and cell.lower() in keys) or \
                       ('.' == cell or 'a' <= cell <= 'f' or cell.lower() in keys):
                        if (new_row, new_col, new_keys) not in visited:
                            visited.add((new_row, new_col, new_keys))
                            queue.append((new_row, new_col, steps + 1, new_keys))

        return -1
