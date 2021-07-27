# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        res = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        n = len(res)
        if n == 1:
            return False
        i = 0
        j = n - 1
        while i<j:
            a = res[i] + res[j]
            if a == k:
                return True
            elif a > k :
                j -= 1
            else:
                i += 1
        return False
