class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def dfs(node):
            nonlocal index
            if not node:
                return True
            if node.val != voyage[index]:
                return False
            index += 1
            if node.left and node.left.val != voyage[index]:
                flipped.append(node.val)
                node.left, node.right = node.right, node.left
            return dfs(node.left) and dfs(node.right)

        flipped = []
        index = 0
        if not dfs(root):
            return [-1]
        return flipped
