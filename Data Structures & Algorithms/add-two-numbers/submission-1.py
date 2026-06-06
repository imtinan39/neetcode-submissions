# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        head = l1
        prev = None
        carry = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            l1.val = total % 10
            carry = total // 10
            prev = l1
            l1 = l1.next
            l2 = l2.next

        if l2:
            prev.next = l2
            l1 = l2

        while l1:
            total = l1.val + carry
            l1.val = total % 10
            carry = total // 10
            prev = l1
            l1 = l1.next

        if carry:
            prev.next = ListNode(carry)

        return head
