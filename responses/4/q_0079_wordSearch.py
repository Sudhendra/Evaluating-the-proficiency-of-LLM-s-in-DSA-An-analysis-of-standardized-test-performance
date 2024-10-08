from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            temp, board[i][j] = board[i][j], '/'
            res = dfs(board, word, i + 1, j, k + 1) or dfs(board, word, i - 1, j, k + 1) or dfs(board, word, i, j + 1, k + 1) or dfs(board, word, i, j - 1, k + 1)
            board[i][j] = temp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, 0):
                    return True
        return False
