# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root : 
            return []
        
        stack = [root]
        path = []
        while stack :
            node = stack.pop()
            if isinstance(node,int):
                path.append(node)
            else : 
                stack.append(node.val)

                if node.right : 
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)
        return path
        
