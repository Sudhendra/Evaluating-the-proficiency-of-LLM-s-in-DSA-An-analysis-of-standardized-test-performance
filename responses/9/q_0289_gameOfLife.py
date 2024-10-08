class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        def count_live_neighbors(x, y):
            count = 0
            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (board[nx][ny] == 1 or board[nx][ny] == 2):
                    count += 1
            return count

        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)

                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 2
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 3

        for i in range(m):
            for j in range(n):
                board[i][j] %= 2
