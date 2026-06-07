# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        first=head
        res=[]

        while first is not None:
            res.append(first.val)
            first=first.next
        
        first=head
        while first is not None:
            if res.pop()!=first.val:
                return False
            first=first.next
        return True
        