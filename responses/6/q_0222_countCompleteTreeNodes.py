class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def count_nodes(node):
            if not node:
                return 0
            left_depth = 0
            right_depth = 0
            left_node = node
            right_node = node
            while left_node:
                left_depth += 1
                left_node = left_node.left
            while right_node:
                right_depth += 1
                right_node = right_node.right
            if left_depth == right_depth:
                return 2 ** left_depth - 1
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        return count_nodes(root)
