class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, total):
            if not node:
                return 0
            
            total = total * 10 + node.val
            
            if not node.left and not node.right:
                return total
            
            return dfs(node.left, total) + dfs(node.right, total)
        
        return dfs(root, 0)
