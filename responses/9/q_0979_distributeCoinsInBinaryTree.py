class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def distribute(node, moves):
            nonlocal total_moves
            if not node:
                return 0
            left_excess = distribute(node.left, moves)
            right_excess = distribute(node.right, moves)
            total_moves += abs(left_excess) + abs(right_excess)
            return node.val + left_excess + right_excess - 1
        
        total_moves = 0
        distribute(root, total_moves)
        return total_moves
