# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode(0,head)
        last, nLast = head, temp

        while n > 0:
            last = last.next
            n -= 1

        while last:
            last = last.next
            nLast = nLast.next
        
        nLast.next = nLast.next.next
        return temp.next
        
