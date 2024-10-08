class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def exists_node(idx, height, node):
            left, right = 0, 2 ** height - 1
            for _ in range(height):
                mid = left + (right - left) // 2
                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None

        if not root:
            return 0

        height = get_height(root)
        if height == 1:
            return 1

        left, right = 1, 2 ** height - 1
        while left <= right:
            mid = left + (right - left) // 2
            if exists_node(mid, height, root):
                left = mid + 1
            else:
                right = mid - 1

        return (2 ** height - 1) + right
