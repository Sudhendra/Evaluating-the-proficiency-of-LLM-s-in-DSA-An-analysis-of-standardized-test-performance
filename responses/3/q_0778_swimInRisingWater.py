class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def can_reach_destination(time):
            visited = [[False] * n for _ in range(n)]
            stack = [(0, 0)]
            
            while stack:
                i, j = stack.pop()
                if i == n - 1 and j == n - 1:
                    return True
                
                visited[i][j] = True
                
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] <= time:
                        stack.append((ni, nj))
            
            return False

        left, right = 0, n*n - 1
        
        while left < right:
            mid = (left + right) // 2

            if can_reach_destination(mid):
                right = mid
            else:
                left = mid + 1
        
        return left