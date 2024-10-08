from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def build_trie(words):
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
            node = node.children.get(char)

            if not node:
                return

            if node.word:
                found_words.add(node.word)

            board[i][j] = "#" # mark as visited

            for x, y in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != "#":
                    dfs(node, x, y)

            board[i][j] = char # backtrack

        root = build_trie(words)
        found_words = set()

        for i in range(len(board)):
            for j in range(len(board[0]):
                dfs(root, i, j)

        return list(found_words)