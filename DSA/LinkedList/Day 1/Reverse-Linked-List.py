# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = None
        current = head

        while current:
            p = current.next
            current.next = n
            n = current
            current = p
        return n
        
