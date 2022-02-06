# My Solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (not root) :
             return []
        queue = [[root]]
        res = []
        while (queue) :
            nodes = queue.pop(0)
            inner_queue = []
            inner_result = []
            for i in range(len(nodes)):
                node = nodes[i]
                inner_result.append(node.val)
                if (node.left) :
                    inner_queue.append(node.left)
                
                if (node.right) :
                    inner_queue.append(node.right)
                    
            res.append(inner_result)
            if(len(inner_queue) == 0 ) : 
                break
            queue.append(inner_queue)

        return res
  # Online Solution
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         q=deque()
        
#         q.append(root)
        
#         res=[]
#         while len(q)>0:
#             sz=len(q)
#             t=[]
#             while sz:
#                 curr=q.popleft()
#                 t.append(curr.val)
                
#                 if curr.left:
#                     q.append(curr.left)
#                 if curr.right:
#                     q.append(curr.right)
                
#                 sz-=1
#             res.append(t)
                
#         return res
