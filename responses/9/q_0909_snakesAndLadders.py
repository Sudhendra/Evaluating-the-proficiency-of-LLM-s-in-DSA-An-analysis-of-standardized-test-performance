from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]) -> int:
        n = len(board)
        visited = set()
        target = n * n
        moves = 0
        queue = deque([(1, 0)])  # (position, moves)

        while queue:
            pos, moves = queue.popleft()
            if pos == target:
                return moves

            for i in range(1, 7):
                next_pos = pos + i
                if next_pos > target:
                    break

                row, col = (n - 1 - (next_pos - 1) // n, (next_pos - 1) % n)
                if row % 2 == n % 2:
                    col = n - 1 - col

                if board[row][col] != -1:
                    next_pos = board[row][col]

                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))

        return -1
