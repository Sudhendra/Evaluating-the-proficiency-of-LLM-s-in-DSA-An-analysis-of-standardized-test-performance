from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board, i, j, word, trie):
            if '#' in trie:
                result.add(trie['#'])
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                return
            tmp = board[i][j]
            node = trie.get(tmp)
            if not node:
                return
            board[i][j] = '*'
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                dfs(board, x, y, word + tmp, node)
            board[i][j] = tmp

        def build_trie(words):
            root = {}
            for word in words:
                node = root
                for char in word:
                    node = node.setdefault(char, {})
                node['#'] = word
            return root

        result = set()
        trie = build_trie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, i, j, '', trie)
        return list(result)