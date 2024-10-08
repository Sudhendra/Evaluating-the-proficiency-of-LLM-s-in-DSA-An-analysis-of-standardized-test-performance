class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, sum_so_far):
            if not node:
                return 0
            sum_so_far = (sum_so_far << 1) + node.val
            if not node.left and not node.right:
                return sum_so_far
            return dfs(node.left, sum_so_far) + dfs(node.right, sum_so_far)
        
        return dfs(root, 0)