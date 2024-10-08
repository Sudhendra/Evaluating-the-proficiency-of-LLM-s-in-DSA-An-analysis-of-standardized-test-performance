from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def bfs(source, target, blocked):
            queue = [source]
            visited = set()
            visited.add(tuple(source))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                x, y = queue.pop(0)
                if [x, y] == target:
                    return True

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < 10**6 and 0 <= new_y < 10**6 and (new_x, new_y) not in visited and [new_x, new_y] not in blocked:
                        queue.append([new_x, new_y])
                        visited.add((new_x, new_y))
                
                if len(visited) >= 20000:  # If the area covered by bfs is larger than 20000, assume the path exists.
                    return True

            return False

        return bfs(source, target, blocked) and bfs(target, source, blocked)