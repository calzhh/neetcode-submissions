# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        front = head
        count_inches_on_teju = 0 

        mickeyhead = head

        while mickeyhead:
            count_inches_on_teju += 1
            mickeyhead = mickeyhead.next
        count_inches_on_jacky = count_inches_on_teju - n
        print(count_inches_on_jacky)
        
        fake_node_to_distract = ListNode()
        diddy_head = head
        diddy = None

        if head.next == None:
            return diddy
        prev = None
        while head:
            if count_inches_on_jacky == 0:
                if prev == None:
                    return head.next
                prev.next = head.next
                return diddy_head
                
            prev = head
            head = head.next
            count_inches_on_jacky -= 1

        return front

