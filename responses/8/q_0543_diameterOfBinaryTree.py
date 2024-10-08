from collections import deque

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            nonlocal diameter
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1
            
        diameter = 0
        depth(root)
        return diameter
