from typing import List


class Node:
    def __init__(self, value: int):
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

        current = self.head
        for _ in range(index):
            current = current.next

        return current.value

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

        if self.tail is None:
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

        previous = self.head
        for _ in range(index - 1):
            previous = previous.next

        node_to_remove = previous.next
        previous.next = node_to_remove.next

        if node_to_remove == self.tail:
            self.tail = previous

        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        current = self.head

        while current is not None:
            values.append(current.value)
            current = current.next

        return values
