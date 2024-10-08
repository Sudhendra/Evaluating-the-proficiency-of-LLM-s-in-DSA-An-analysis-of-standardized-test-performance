from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def reveal_board(board, r, c):
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return
            if board[r][c] != 'E':
                return
            adj_mines = sum(1 for dr in range(-1, 2) for dc in range(-1, 2)
                            if 0 <= r+dr < len(board) and 0 <= c+dc < len(board[0]) and board[r+dr][c+dc] == 'M')
            if adj_mines > 0:
                board[r][c] = str(adj_mines)
            else:
                board[r][c] = 'B'
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if 0 <= r+dr < len(board) and 0 <= c+dc < len(board[0]):
                            reveal_board(board, r+dr, c+dc)

        reveal_board(board, click[0], click[1])
        return board
