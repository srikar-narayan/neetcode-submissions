# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = head
        future = head
        for i in range(n):
            future = future.next
        
        prev = None
        curr = head
        while future:
            prev = curr
            curr = curr.next
            future = future.next
        
        if prev:
            prev.next = curr.next
        else:
            head = head.next
        return head
            

        