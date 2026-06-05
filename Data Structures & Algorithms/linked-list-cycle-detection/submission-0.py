# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        curr=head

        while curr is not None:
            if curr.val==-100000:
                return True
            else:
                curr.val=-100000
                curr=curr.next
        return False

        