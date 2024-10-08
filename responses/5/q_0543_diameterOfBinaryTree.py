class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0

        def dfs(node):
            if not node:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)

            self.longest_path = max(self.longest_path, left_path + right_path)

            return max(left_path, right_path) + 1

        dfs(root)

        return self.longest_path
