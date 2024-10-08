# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        def dfs(node):
            nonlocal idx
            if not node or node.val != voyage[idx]:
                return False
            idx += 1
            if node.left and node.left.val != voyage[idx]:
                flips.append(node.val)
                node.left, node.right = node.right, node.left
            return dfs(node.left) and dfs(node.right)

        flips = []
        idx = 0
        return flips if dfs(root) else [-1]
