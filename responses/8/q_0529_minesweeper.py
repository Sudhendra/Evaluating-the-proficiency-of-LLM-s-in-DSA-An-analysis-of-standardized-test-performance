from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def reveal_adjacent(board, r, c):
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'E':
                mines = sum(board[x][y] == 'M' for x in range(r-1, r+2) for y in range(c-1, c+2) if 0 <= x < len(board) and 0 <= y < len(board[0]))
                board[r][c] = 'B' if mines == 0 else str(mines)
                if mines == 0:
                    for x in range(r-1, r+2):
                        for y in range(c-1, c+2):
                            reveal_adjacent(board, x, y)

        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            reveal_adjacent(board, r, c)
        
        return board
