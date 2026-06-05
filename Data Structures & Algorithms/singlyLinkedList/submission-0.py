from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next

        return curr.value

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
            self.length -= 1
            return True

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        node_to_remove = prev.next
        prev.next = node_to_remove.next

        if node_to_remove == self.tail:
            self.tail = prev

        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head

        while curr is not None:
            res.append(curr.value)
            curr = curr.next

        return res