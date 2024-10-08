class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        def dfs(node):
            nonlocal idx
            if not node:
                return True
            if node.val != voyage[idx]:
                return False

            idx += 1
            if node.left and node.left.val != voyage[idx]:
                flipped.append(node.val)
                node.left, node.right = node.right, node.left

            return dfs(node.left) and dfs(node.right)

        flipped = []
        idx = 0
        return flipped if dfs(root) else [-1]
