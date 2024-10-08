class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.flipped = []
        self.index = 0
        
        def dfs(node):
            if not node:
                return True
            
            if node.val != voyage[self.index]:
                return False
            
            self.index += 1
            
            if node.left and node.left.val != voyage[self.index]:
                self.flipped.append(node.val)
                node.left, node.right = node.right, node.left
            
            return dfs(node.left) and dfs(node.right)
        
        return self.flipped if dfs(root) else [-1]
