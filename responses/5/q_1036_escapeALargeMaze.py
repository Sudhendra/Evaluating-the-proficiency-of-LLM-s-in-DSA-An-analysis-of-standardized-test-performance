from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True
        
        def dfs(x, y, target_x, target_y, visited, blocked_set, steps):
            if (x, y) == (target_x, target_y):
                return True
            if steps == 0 or (x, y) in blocked_set or (x, y) in visited:
                return False

            visited.add((x, y))
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 10**6 and 0 <= new_y < 10**6:
                    if dfs(new_x, new_y, target_x, target_y, visited, blocked_set, steps - 1):
                        return True

            return False

        blocked_set = set(tuple(coord) for coord in blocked)

        source_x, source_y = source
        target_x, target_y = target

        if dfs(source_x, source_y, target_x, target_y, set(), blocked_set, min(len(blocked), 200)):
            return True
        
        if dfs(target_x, target_y, source_x, source_y, set(), blocked_set, min(len(blocked), 200)):
            return True

        return False
