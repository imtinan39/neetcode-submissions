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
        i = 0
        if self.length == 0 or index > self.length - 1 or index < 0:
            return -1
        else:
            curr = self.head
            for n in range(index + 1):
                if i == index:
                    return curr.value
                curr = curr.next
                i += 1
        
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

        if index < 0 or index > self.length - 1:
            return False
        else:
            if index == 0:
                self.head = self.head.next
                if self.length == 1:
                    self.tail = None
                self.length -= 1
                return True

            curr = self.head
            for i in range(index - 1):
                curr = curr.next

            if curr.next == self.tail:
                self.tail = curr

            curr.next = curr.next.next
            self.length -= 1
            return True

    def getValues(self) -> List[int]:
        res = []

        curr = self.head

        while curr != None:
            res.append(curr.value)
            curr = curr.next
        return res