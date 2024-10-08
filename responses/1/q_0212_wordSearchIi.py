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
                result.append(node.word)
                node.word = None # Avoid duplicate results
            
            board[i][j] = '#' # Mark as visited
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != '#':
                    dfs(node, x, y)
            board[i][j] = char # Restore the original char
        
        root = build_trie(words)
        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(root, i, j)
        return result