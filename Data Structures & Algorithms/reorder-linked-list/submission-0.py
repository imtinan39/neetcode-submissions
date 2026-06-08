# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

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
            nxt = second.next
            second.next = None
            li.append(second)
            second = nxt

        first = head
        while li:
            tmp = first.next
            node = li.pop()
            first.next = node
            node.next = tmp

            if tmp is None:
                break
            first = tmp
