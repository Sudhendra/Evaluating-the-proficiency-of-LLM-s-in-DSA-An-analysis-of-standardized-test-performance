from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def reveal_adjacent_cells(board, r, c):
            rows, cols = len(board), len(board[0])
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'E':
                return

            mine_count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    new_r, new_c = r + i, c + j
                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        if board[new_r][new_c] == 'M':
                            mine_count += 1

            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = 'B'
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        new_r, new_c = r + i, c + j
                        if 0 <= new_r < rows and 0 <= new_c < cols:
                            reveal_adjacent_cells(board, new_r, new_c)

        rows, cols = len(board), len(board[0])
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            reveal_adjacent_cells(board, r, c)

        return board
