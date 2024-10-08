from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(board, r, c):
            if board[r][c] == 'E':
                mine_count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= r + dr < len(board) and 0 <= c + dc < len(board[0]):
                            if board[r+dr][c+dc] == 'M':
                                mine_count += 1
                if mine_count == 0:
                    board[r][c] = 'B'
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if 0 <= r + dr < len(board) and 0 <= c + dc < len(board[0]):
                                dfs(board, r+dr, c+dc)
                else:
                    board[r][c] = str(mine_count)
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            dfs(board, click[0], click[1])
        
        return board
