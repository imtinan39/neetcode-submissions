class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

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
            first = tmp