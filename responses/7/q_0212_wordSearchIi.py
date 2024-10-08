from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board, i, j, word, index):
            if index == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False

            temp, board[i][j] = board[i][j], '#'
            res = (dfs(board, i + 1, j, word, index + 1) or
                   dfs(board, i - 1, j, word, index + 1) or
                   dfs(board, i, j + 1, word, index + 1) or
                   dfs(board, i, j - 1, word, index + 1))
            board[i][j] = temp
            return res

        def exist(board, word):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0] and dfs(board, i, j, word, 0):
                        return True
            return False

        result = []
        for w in words:
            if exist(board, w):
                result.append(w)
        return result
