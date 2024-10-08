class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        left_root_val = preorder[1]
        index_left_root_post = postorder.index(left_root_val)
        
        root.left = self.constructFromPrePost(preorder[1:index_left_root_post+2], postorder[:index_left_root_post+1])
        root.right = self.constructFromPrePost(preorder[index_left_root_post+2:], postorder[index_left_root_post+1:-1])
        
        return root
