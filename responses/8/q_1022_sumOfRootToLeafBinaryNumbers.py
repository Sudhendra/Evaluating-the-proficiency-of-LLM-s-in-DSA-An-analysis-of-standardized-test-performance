class Solution:
    def sumRootToLeaf(self, root: TreeNode, val: int = 0) -> int:
        if not root:
            return 0
        val = val * 2 + root.val
        if not root.left and not root.right:
            return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)
