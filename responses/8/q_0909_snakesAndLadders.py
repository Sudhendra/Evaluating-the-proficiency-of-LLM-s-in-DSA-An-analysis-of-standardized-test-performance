from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        visited = set()
        queue = [(1, 0)]  # (current position, number of moves)

        while queue:
            position, moves = queue.pop(0)
            if position in visited:
                continue
            visited.add(position)

            for i in range(1, 7):
                next_position = position + i
                if next_position > target:
                    break
                
                row, col = (n - 1 - (next_position - 1) // n, (next_position - 1) % n)
                if board[row][col] != -1:
                    next_position = board[row][col]

                if next_position == target:
                    return moves + 1
                
                queue.append((next_position, moves + 1))

        return -1
