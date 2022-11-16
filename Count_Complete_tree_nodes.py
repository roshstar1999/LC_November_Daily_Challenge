 def countNodes(self, root: Optional[TreeNode]) -> int:
        
        
               
        
        if root==None:
            return 0
        
        return 1 +self.countNodes(root.right)+self.countNodes(root.left)
    
