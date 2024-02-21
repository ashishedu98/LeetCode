# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        curr = head
        next,prev = None,None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


        