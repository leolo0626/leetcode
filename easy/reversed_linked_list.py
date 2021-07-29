# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None :
            return head
        
        tempNode = ListNode(head.val)
        while head.next :
            head = head.next
            secondTempNode = ListNode(head.val)
            secondTempNode.next = tempNode
            tempNode = secondTempNode
        
        return tempNode
        
