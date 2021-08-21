# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        treeDict = defaultdict(int)
        res = []
        def helper(node):
            if node is None:
                return "N"
            
            left = helper(node.left)
            right = helper(node.right)
            curstr = left + right + str(node.val) + '+'

            if treeDict[curstr] == 1:
                treeDict[curstr] = 2
                res.append(node)
            else:
                treeDict[curstr] =  treeDict[curstr] + 1
            return curstr
        helper(root)
        return res
