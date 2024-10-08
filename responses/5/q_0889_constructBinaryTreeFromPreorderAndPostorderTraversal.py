from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def construct(prestart, poststart, size):
            if size == 0:
                return None

            root = TreeNode(preorder[prestart])
            if size == 1:
                return root

            left_size = 1
            while preorder[prestart + 1] != postorder[poststart + left_size - 1]:
                left_size += 1

            root.left = construct(prestart + 1, poststart, left_size)
            root.right = construct(prestart + left_size + 1, poststart + left_size, size - 1 - left_size)

            return root

        return construct(0, 0, len(preorder))
