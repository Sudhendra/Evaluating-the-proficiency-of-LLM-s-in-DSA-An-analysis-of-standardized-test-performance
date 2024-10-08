from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(node, i, j):
            letter = board[i][j]
            cur_node = node[letter]
            result = []
            
            if "end_word" in cur_node:
                result.append(cur_node["end_word"])
                del cur_node["end_word"]
            
            board[i][j] = "#"
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] in cur_node:
                    result.extend(backtrack(cur_node, x, y))
            
            board[i][j] = letter
            
            if not cur_node:
                del node[letter]
            
            return result
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node["end_word"] = word
        
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    res.extend(backtrack(trie, i, j))
        
        return res
