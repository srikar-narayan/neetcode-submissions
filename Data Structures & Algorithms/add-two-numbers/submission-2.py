# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        while l1 or l2:
            if l1:
                dig1 = l1.val
                l1 = l1.next
            else:
                dig1 = 0
            if l2:
                dig2 = l2.val
                l2 = l2.next
            else:
                dig2 = 0
            
            summ = (dig1 + dig2) % 10
            node.next = ListNode(summ)
            node = node.next
            if dig1 + dig2 >= 10:
                if l1:
                    l1.val += 1
                elif l2:
                    l2.val += 1
                else:
                    node.next = ListNode(1)
        return dummy.next

                
            
        