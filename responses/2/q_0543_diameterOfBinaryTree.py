class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal max_diameter
            if not node:
                return 0
            left_length = dfs(node.left)
            right_length = dfs(node.right)
            max_diameter = max(max_diameter, left_length + right_length)
            return 1 + max(left_length, right_length)

        max_diameter = 0
        dfs(root)
        return max_diameter