class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_tree_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def node_exists(idx, height, node):
            left, right = 0, 2**height - 1
            for _ in range(height):
                pivot = left + (right - left) // 2
                if idx <= pivot:
                    node = node.left
                    right = pivot
                else:
                    node = node.right
                    left = pivot + 1
            return node is not None

        height = get_tree_height(root)
        if height == 1:
            return 1
        
        left, right = 1, 2**height - 1
        while left <= right:
            mid = left + (right - left) // 2
            if node_exists(mid, height, root):
                left = mid + 1
            else:
                right = mid - 1
        
        return 2**height - 1 + left - 1