class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            self.moves += abs(left_excess) + abs(right_excess)
            return node.val + left_excess + right_excess - 1
        
        dfs(root)
        return self.moves
