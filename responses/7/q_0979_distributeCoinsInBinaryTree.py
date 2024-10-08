class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            
            total_excess = left_excess + right_excess + node.val - 1
            self.moves += abs(total_excess)
            
            return total_excess
        
        dfs(root)
        
        return self.moves
