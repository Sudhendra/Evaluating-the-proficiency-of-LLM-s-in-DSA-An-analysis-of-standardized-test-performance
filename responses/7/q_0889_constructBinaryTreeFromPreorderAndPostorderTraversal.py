class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        left_val = preorder[1]
        idx = postorder.index(left_val)
        
        root.left = self.constructFromPrePost(preorder[1:idx+2], postorder[:idx+1])
        root.right = self.constructFromPrePost(preorder[idx+2:], postorder[idx+1:-1])
        
        return root
