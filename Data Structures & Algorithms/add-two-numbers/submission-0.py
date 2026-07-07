# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ""
        second = ""

        while l1:
            first += str(l1.val)
            l1 = l1.next
            
        while l2:
            second += str(l2.val)
            l2 = l2.next

        first = int(first[::-1])
        second = int(second[::-1])


        total = (first + second)
        
        dummy = genius = ListNode(0)

        for single_dight in str(total)[::-1]:
            dummy.next = ListNode(single_dight)
            dummy = dummy.next

        return genius.next