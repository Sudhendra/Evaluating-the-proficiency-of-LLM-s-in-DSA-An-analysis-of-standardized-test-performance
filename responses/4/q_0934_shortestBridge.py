from collections import deque

class Solution:
    def shortestBridge(self, grid):
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 2
            island.append((i, j))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i + dx, j + dy)

        def bfs():
            depth = 0
            while queue:
                new_queue = []
                for i, j in queue:
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n:
                            if grid[x][y] == 1:
                                return depth
                            elif grid[x][y] == 0:
                                grid[x][y] = 2
                                new_queue.append((x, y))
                queue = new_queue
                depth += 1

        n = len(grid)
        island = []
        queue = deque()
        found = False

        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break

        for x, y in island:
            queue.append((x, y))

        return bfs()

# Example usage
solution = Solution()
output = solution.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]])
print(output)  # Output: 2
