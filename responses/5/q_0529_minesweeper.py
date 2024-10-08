from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def get_adjacent_mines_count(board, r, c):
            mines = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 'M':
                        mines += 1
            return mines

        def reveal_blank(board, r, c):
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'E':
                mines = get_adjacent_mines_count(board, r, c)
                if mines == 0:
                    board[r][c] = 'B'
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            reveal_blank(board, r + dr, c + dc)

                else:
                    board[r][c] = str(mines)

        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            reveal_blank(board, r, c)

        return board
