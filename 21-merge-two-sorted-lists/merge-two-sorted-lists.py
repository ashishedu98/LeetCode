# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        head,curr = None,None
        while list1 and list2:
            if list2.val<= list1.val:
                if head==None:
                    head = list2
                    curr = head
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next
            else:
                if head==None:
                    head = list1
                    curr = head
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next
        
        if list1:
            if head==None:
                head = list1
                curr = head
            else:
                curr.next = list1

        if list2:
            if head==None:
                head = list2
                curr = head
            else:
                curr.next = list2
        return head
