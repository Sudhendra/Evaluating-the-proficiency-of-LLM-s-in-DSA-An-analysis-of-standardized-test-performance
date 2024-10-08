from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []

        def dfs(board, word, i, j, visited):
            if not word:
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0] or (i, j) in visited:
                return False

            visited.add((i, j))
            res = False
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                res = res or dfs(board, word[1:], x, y, visited)
            visited.remove((i, j))
            return res

        result = []
        for word in words:
            found = False
            for i in range(len(board)):
                for j in range(len(board[0]):
                    if dfs(board, word, i, j, set()):
                        found = True
                        break
            if found:
                result.append(word)
        return result
