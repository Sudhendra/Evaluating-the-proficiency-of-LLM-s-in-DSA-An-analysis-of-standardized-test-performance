from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(board, r, c):
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return
            if board[r][c] != 'E':
                return

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            mine_count = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 'M':
                    mine_count += 1
                    
            if mine_count == 0:
                board[r][c] = 'B'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 'E':
                        dfs(board, nr, nc)
            else:
                board[r][c] = str(mine_count)

        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            dfs(board, r, c)

        return board
