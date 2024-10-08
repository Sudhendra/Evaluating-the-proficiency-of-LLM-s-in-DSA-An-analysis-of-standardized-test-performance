from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        def count_adjacent_mines(row, col):
            count = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    count += 1
            return count

        def reveal_empty_squares(row, col):
            if board[row][col] != 'E':
                return
            mine_count = count_adjacent_mines(row, col)
            if mine_count == 0:
                board[row][col] = 'B'
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        reveal_empty_squares(nr, nc)
            else:
                board[row][col] = str(mine_count)

        click_r, click_c = click
        if board[click_r][click_c] == 'M':
            board[click_r][click_c] = 'X'
        else:
            reveal_empty_squares(click_r, click_c)

        return board
