from typing import List

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(i, j, word, visited, index):
            if word[index] != board[i][j]:
                return False

            if index == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                    if (new_i, new_j) not in visited:
                        if backtrack(new_i, new_j, word, visited, index + 1):
                            result = True
                            break
                    
            visited.remove((i, j))
            return result

        found_words = set()
        for word in words:
            word_found = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if backtrack(i, j, word, set(), 0):
                        word_found = True
                        break
                if word_found:
                    found_words.add(word)
                    break
                    
        return list(found_words)
