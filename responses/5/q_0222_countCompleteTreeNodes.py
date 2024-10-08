# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        def exists(idx, h, node):
            left, right = 0, 2**h - 1
            for _ in range(h):
                pivot = left + (right - left) // 2
                if idx <= pivot:
                    node = node.left
                    right = pivot
                else:
                    node = node.right
                    left = pivot + 1
            return node is not None
        
        h = height(root)
        if h == 1:
            return 1
        
        full_depth = h - 1
        low, high = 1, 2**full_depth - 1
        while low <= high:
            mid = low + (high - low) // 2
            if exists(mid, full_depth, root):
                low = mid + 1
            else:
                high = mid - 1
        
        return (2**full_depth - 1) + low
