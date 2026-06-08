# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        count = 0
        cur = head
        while cur is not None:
            count += 1
            cur = cur.next

        curr = head
        for _ in range((count - 1) // 2):
            curr = curr.next

        second = curr.next
        curr.next = None

        li = []
        while second is not None:
            li.append(ListNode(second.val))
            second = second.next

        first = head
        while li:
            tmp = first.next
            node = li.pop()
            first.next = node
            node.next = tmp

            if tmp is None:
                break
            first = node.next
