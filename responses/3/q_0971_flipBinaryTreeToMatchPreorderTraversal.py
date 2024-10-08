from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        def dfs(node, idx):
            nonlocal res, voyage

            if not node:
                return idx

            if node.val != voyage[idx]:
                return -1

            if node.left and node.left.val != voyage[idx + 1]:
                res.append(node.val)
                idx = dfs(node.right, dfs(node.left, idx + 1))
            else:
                idx = dfs(node.left, dfs(node.right, idx + 1))

            return idx

        res = []
        return res if dfs(root, 0) != -1 else [-1]
