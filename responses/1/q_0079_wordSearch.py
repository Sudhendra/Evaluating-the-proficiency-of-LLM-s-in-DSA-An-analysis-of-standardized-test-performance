from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, i, j, word):
            if len(word) == 0:
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
                return False

            tmp, board[i][j] = board[i][j], '#'
            res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
            board[i][j] = tmp

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(board, i, j, word):
                    return True

        return False