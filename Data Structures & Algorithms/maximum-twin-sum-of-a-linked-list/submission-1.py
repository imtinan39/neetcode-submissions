# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        res=[]

        while head is not None:
            res.append(head.val)
            head=head.next
        ans=0
        fast=0
        last=len(res)-1

        while fast<last:
            ans=max(ans,(res[fast]+res[last]))
            fast+=1
            last-=1

        return ans

        