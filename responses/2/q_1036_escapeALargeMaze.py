from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def is_inside(x, y):
            return 0 <= x < 10**6 and 0 <= y < 10**6
        
        def is_escape_possible(start, end, blocks):
            visited = set()
            stack = [start]
            while stack:
                x, y = stack.pop()
                if [x, y] == end:
                    return True
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = x+dx, y+dy
                    if is_inside(new_x, new_y) and [new_x, new_y] not in blocks:
                        stack.append((new_x, new_y))
                
                if len(visited) >= 20000:  # If visited more than 20k squares, probably escape is possible
                    return True
                
            return False
        
        return is_escape_possible(source, target, blocked) and is_escape_possible(target, source, blocked)