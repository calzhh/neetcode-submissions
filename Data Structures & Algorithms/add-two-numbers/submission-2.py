# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = genius = ListNode(0)
        while l1 and l2:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0 
            total = first + second + carry
            carry = 0 
            if total >= 10:
                carry = int(str(total)[0])
                total = int(str(total)[1])
            dummy.next = ListNode(total)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            first = l1.val if l1 else 0
            total = first + carry
            carry = 0
            if total >= 10:
                carry = int(str(total)[0])
                total = int(str(total)[1])
            dummy.next = ListNode(total)
            dummy = dummy.next
            l1 = l1.next
        while l2:
            second = l2.val if l2 else 0 
            total = second + carry
            carry = 0
            if total >= 10:
                carry = int(str(total)[0])
                total = int(str(total)[1])
            dummy.next = ListNode(total)
            dummy = dummy.next
            l2 = l2.next

        if carry > 0:
            dummy.next = ListNode(carry)
        return genius.next