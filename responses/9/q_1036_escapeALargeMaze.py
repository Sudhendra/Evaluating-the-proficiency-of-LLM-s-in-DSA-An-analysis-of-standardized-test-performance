class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        from collections import deque
        
        visited = set()
        for b in blocked:
            visited.add(tuple(b))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(sx, sy, tx, ty):
            queue = deque([(sx, sy)])
            visited.add((sx, sy))
            while queue:
                x, y = queue.popleft()
                if x == tx and y == ty:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 10**6 and 0 <= ny < 10**6 and (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                if len(visited) >= 2 * len(blocked) + 10:
                    return True
            return False
        
        return bfs(source[0], source[1], target[0], target[1]) and bfs(target[0], target[1], source[0], source[1])
