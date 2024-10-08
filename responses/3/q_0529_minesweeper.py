class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def reveal_square(i, j):
            if board[i][j] == 'M':
                board[i][j] = 'X'
            elif board[i][j] == 'E':
                mines_adjacent = sum(1 for x in range(i-1, i+2) for y in range(j-1, j+2) 
                                     if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'M')
                if mines_adjacent > 0:
                    board[i][j] = str(mines_adjacent)
                else:
                    board[i][j] = 'B'
                    for x in range(i-1, i+2):
                        for y in range(j-1, j+2):
                            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'E':
                                reveal_square(x, y)
        
        reveal_square(click[0], click[1])
        return board