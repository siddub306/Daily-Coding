# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        current.next = head
        k %= length

        back = length - k - 1
        nback = head
        for _ in range(back):
            nback = nback.next
        
        nhead = nback.next
        nback.next = None

        return nhead
