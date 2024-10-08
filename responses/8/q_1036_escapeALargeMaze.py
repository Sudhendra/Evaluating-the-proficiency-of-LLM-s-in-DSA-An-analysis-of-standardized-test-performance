class Solution:
    def isEscapePossible(self, blocked, source, target):
        if not blocked:
            return True
        
        blocked_set = set(tuple(b) for b in blocked)

        def is_valid(x, y):
            return 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in blocked_set
        
        def dfs(x, y, visited):
            if len(visited) > 20000 or (x, y) == tuple(target):
                return False
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    if dfs(new_x, new_y, visited):
                        return True
            return False

        return dfs(source[0], source[1], set(tuple(source)))
