class Solution:
    
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        flipped_nodes = []
        self.idx = 0
        
        def dfs(node):
            if not node or self.idx >= len(voyage):
                return True

            if node.val != voyage[self.idx]:
                return False

            self.idx += 1

            if node.left and node.left.val != voyage[self.idx]:
                flipped_nodes.append(node.val)
                return dfs(node.right) and dfs(node.left)

            return dfs(node.left) and dfs(node.right)

        if dfs(root):
            return flipped_nodes
        else:
            return [-1]
