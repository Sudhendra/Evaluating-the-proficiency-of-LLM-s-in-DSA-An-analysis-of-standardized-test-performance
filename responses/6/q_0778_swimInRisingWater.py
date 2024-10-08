from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def can_reach_destination(grid, time):
            visited = [[False for _ in range(n)] for _ in range(n)]
            min_heap = [(grid[0][0], 0, 0)]
            
            while min_heap:
                elevation, r, c = heappop(min_heap)
                
                if r == n - 1 and c == n - 1:
                    return True
                
                visited[r][c] = True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] <= time:
                        heappush(min_heap, (grid[nr][nc], nr, nc))
            
            return False
        
        left, right = grid[0][0], n * n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if can_reach_destination(grid, mid):
                right = mid
            else:
                left = mid + 1
        
        return left
