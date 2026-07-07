# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_jacky = head
        fast_eric = head

        while slow_jacky:
            try:
                fast_eric = fast_eric.next.next
            except AttributeError:
                return False
            slow_jacky = slow_jacky.next
            if slow_jacky == fast_eric:
                return True
        return False
            
