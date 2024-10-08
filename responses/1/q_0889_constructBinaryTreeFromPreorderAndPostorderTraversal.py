class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        left_val = preorder[1]
        idx = postorder.index(left_val) + 1
        
        root.left = self.constructFromPrePost(preorder[1:idx+1], postorder[:idx])
        root.right = self.constructFromPrePost(preorder[idx+1:], postorder[idx:-1])
        
        return root