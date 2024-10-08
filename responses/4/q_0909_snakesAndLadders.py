from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        visited = set()
        moves = 0
        queue = [(1, 0)]

        while queue:
            for _ in range(len(queue)):
                cell, moves = queue.pop(0)
                if cell == target:
                    return moves

                if cell in visited:
                    continue
                visited.add(cell)

                for i in range(1, 7):
                    next_cell = cell + i
                    if next_cell > target:
                        break
                    row, col = (n - 1) - (next_cell - 1) // n, (next_cell - 1) % n
                    next_move = board[row][col] if row % 2 != n % 2 else board[row][n - col - 1]
                    queue.append((next_move, moves + 1) if next_move != -1 else (next_cell, moves + 1))

        return -1
