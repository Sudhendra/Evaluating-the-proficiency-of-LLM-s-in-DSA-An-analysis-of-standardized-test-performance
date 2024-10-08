from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        
        def can_reach_target(t):
            if grid[0][0] > t:
                return False
            
            stack = [(0, 0)]
            while stack:
                x, y = stack.pop()
                if x == n - 1 and y == n - 1:
                    return True
                
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited and grid[new_x][new_y] <= t:
                        stack.append((new_x, new_y))
                        visited.add((new_x, new_y))
                
            return False
        
        left, right = 0, n*n - 1
        while left < right:
            mid = left + (right - left) // 2
            visited.clear()
            if can_reach_target(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
