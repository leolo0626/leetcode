class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root :
            return []
        stack = [root]
        
        result = []
        while stack : 
            node = stack.pop()
            result.append(node.val)
            
#             if node.right is None and node.left is None : 
#                 return result
            
            if node.right : 
                stack.append(node.right)
            
            if node.left :
                stack.append(node.left)
        
        return result
