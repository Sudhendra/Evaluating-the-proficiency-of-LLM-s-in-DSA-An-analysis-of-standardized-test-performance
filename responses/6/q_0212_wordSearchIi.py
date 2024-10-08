from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def build_trie():
            root = TrieNode()
            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.word = word
            return root
        
        def dfs(node, i, j):
            char = board[i][j]
            if char not in node.children:
                return
            node = node.children[char]
            if node.word:
                result.add(node.word)

            board[i][j], tmp = '#', char
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                    dfs(node, new_i, new_j)
            board[i][j] = tmp

        root = build_trie()
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(root, i, j)
        return list(result)
