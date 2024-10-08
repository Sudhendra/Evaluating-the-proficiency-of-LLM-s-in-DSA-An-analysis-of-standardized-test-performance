from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        def dfs(node, flip_order):
            nonlocal idx
            if not node:
                return True

            if node.val != voyage[idx]:
                return False

            idx += 1

            if node.left and node.left.val != voyage[idx]:
                flip_order.append(node.val)
                node.left, node.right = node.right, node.left  # flip the nodes
            return dfs(node.left, flip_order) and dfs(node.right, flip_order)

        idx = 0
        flip_order = []
        return flip_order if dfs(root, flip_order) else [-1]
