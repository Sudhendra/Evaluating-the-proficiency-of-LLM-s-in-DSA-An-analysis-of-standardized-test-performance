class Solution:
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(board, r, c):
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return
            if board[r][c] != 'E':
                return
            mines = sum([board[i][j] == 'M' for i in range(r-1, r+2) for j in range(c-1, c+2) if 0 <= i < len(board) and 0 <= j < len(board[0])])
            if mines > 0:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i != r or j != c):
                            dfs(board, i, j)
        
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            dfs(board, r, c)
        return board