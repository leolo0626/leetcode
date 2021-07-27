# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
            
        