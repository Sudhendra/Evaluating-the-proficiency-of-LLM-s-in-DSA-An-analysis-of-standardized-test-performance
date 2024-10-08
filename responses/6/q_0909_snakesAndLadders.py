from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n

        def get_position(num):
            row = (num - 1) // n
            col = (num - 1) % n
            if row % 2 == 1:
                col = n - 1 - col
            return row, col

        visited = set()
        queue = deque([(1, 0)])
        while queue:
            num, moves = queue.popleft()
            if num in visited:
                continue
            visited.add(num)

            row, col = get_position(num)
            for i in range(1, 7):
                next_num = num + i
                if next_num > target:
                    break
                next_row, next_col = get_position(next_num)
                if board[next_row][next_col] != -1:
                    next_num = board[next_row][next_col]

                if next_num == target:
                    return moves + 1

                queue.append((next_num, moves + 1))

        return -1
