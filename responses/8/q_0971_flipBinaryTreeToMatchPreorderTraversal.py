    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.flipped = []
        self.idx = 0

        def dfs(node):
            if not node:
                return True

            if node.val != voyage[self.idx]:
                return False

            self.idx += 1

            if node.left and node.left.val != voyage[self.idx]:
                self.flipped.append(node.val)
                node.left, node.right = node.right, node.left

            return dfs(node.left) and dfs(node.right)

        return self.flipped if dfs(root) else [-1]
