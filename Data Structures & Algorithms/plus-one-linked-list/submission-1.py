# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy=ListNode()
        prev=None
        cur=head

        while cur is not None:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        
        carry=0

        curr=dummy
        count=0

        while prev or carry:
            digit_1 = prev.val if prev else 0
            digit_2 = 1 if count==0 else 0
            count=1

            total = digit_1 + digit_2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

            if prev:
                prev = prev.next
        current=dummy.next
        previous=None
        while current is not None:
            tmp=current.next
            current.next=previous
            previous=current
            current=tmp
        return previous



        