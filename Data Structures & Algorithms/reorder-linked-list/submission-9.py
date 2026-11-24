# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #split in half
        slow, fast = head, head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        
        #reverse right
        curr, prev = right, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        right_rev = prev

        #merge. head = left, right_rev = right

        dummy = node = ListNode()
        while head:
            val1 = head
            val2 = right_rev
            head = head.next
            if right_rev:
                right_rev = right_rev.next
            node.next = val1
            val1.next = val2
            node = val2  