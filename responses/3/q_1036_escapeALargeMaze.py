from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def is_escape_possible(grid, source, target):
            blocked_set = set(map(tuple, blocked))

            def bfs(start, destination, limit):
                if start == destination:
                    return True
                visited = set()
                queue = [start]
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                while queue:
                    if len(visited) == limit:
                        return True
                    x, y = queue.pop(0)
                    visited.add((x, y))

                    for dx, dy in directions:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and (new_x, new_y) not in visited and (
                        new_x, new_y) not in blocked_set:
                            if (new_x, new_y) == destination:
                                return True
                            queue.append((new_x, new_y))

                return False

            grid_size = 10 ** 6
            source_grid = [[0] * grid_size for _ in range(grid_size)]
            target_grid = [[0] * grid_size for _ in range(grid_size)]

            source_x, source_y = source
            target_x, target_y = target
            source_grid[source_x][source_y] = 1
            target_grid[target_x][target_y] = 1

            res_source = bfs(source, target, len(blocked))
            res_target = bfs(target, source, len(blocked))

            return res_source and res_target

        return is_escape_possible(blocked, source, target)
