from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def is_valid(x, y, blocked_set):
            return 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in blocked_set

        blocked_set = set(map(tuple, blocked))

        def dfs(x, y, blocked_set, visited):
            if (x, y) == tuple(target):
                return True
            if len(visited) >= 200:  # Limiting the search depth to avoid infinite loops
                return False

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, blocked_set) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if dfs(nx, ny, blocked_set, visited):
                        return True

            return False

        return dfs(source[0], source[1], blocked_set, set([(source[0], source[1])])) and dfs(target[0], target[1], blocked_set, set([(target[0], target[1])])
