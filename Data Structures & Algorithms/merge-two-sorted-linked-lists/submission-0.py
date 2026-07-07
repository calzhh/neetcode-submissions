# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        merge = new
        while list1 or list2:
            if not list1:
                new.next = ListNode(list2.val)
                list2 = list2.next
            elif not list2:
                new.next = ListNode(list1.val)
                list1 = list1.next
            elif list1.val >= list2.val:
                new.next = ListNode(list2.val)
                list2 = list2.next
            elif list2.val > list1.val:
                new.next = ListNode(list1.val)
                list1 = list1.next
            new = new.next
        return merge.next
