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
        
        def backtrack(node, i, j):
            char = board[i][j]
            cur_node = node.children.get(char)
            
            if not cur_node:
                return
            
            if cur_node.word:
                result.append(cur_node.word)
                cur_node.word = None
            
            board[i][j] = "#"  # Mark as visited
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != "#":
                    backtrack(cur_node, x, y)
            
            board[i][j] = char  # Reset the board back
            
        root = build_trie()
        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(root, i, j)
        
        return result
