from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # Constants
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        MAX_MOVES = 20000

        def is_within_limits(x: int, y: int) -> bool:
            return 0 <= x < 10**6 and 0 <= y < 10**6

        def dfs(x: int, y: int, visited: set) -> bool:
            if len(visited) >= MAX_MOVES or not is_within_limits(x, y) or [x, y] in blocked or (x, y) in visited:
                return False

            visited.add((x, y))

            if [x, y] == target:
                return True

            for dx, dy in DIRECTIONS:
                if dfs(x + dx, y + dy, visited):
                    return True

            return False

        if not blocked: # If there are no blocked cells
            return True

        return dfs(*source, set()), dfs(*target, set())
