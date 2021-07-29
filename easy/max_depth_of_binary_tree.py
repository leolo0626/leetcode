# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None : 
            return 0
        
        stack = [(1, root)]
        max_level_of_node = 1
        while stack :
            level_of_node ,node = stack.pop()
            max_level_of_node = max(max_level_of_node, level_of_node)
            
            if node is None :
                continue
            
            if node.right :
                stack.append((level_of_node + 1, node.right))
                
            if node.left : 
                stack.append((level_of_node + 1, node.left))
            
        return max_level_of_node
