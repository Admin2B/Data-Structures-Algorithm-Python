# -*- encoding: utf-8 -*-
from singlelinklist import SingleLinkList


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkList(SingleLinkList):


    def add(self, item):
        node = Node(item)
        node.next = self._SingleLinkList__head
        self._SingleLinkList__head = node
        node.next.prev = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._SingleLinkList__head = node
        else:
            cur = self._SingleLinkList__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self._SingleLinkList__head
            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        cur = self._SingleLinkList__head
        while cur is not None:
            if cur.item == item:
                if cur == self._SingleLinkList__head:
                    self._SingleLinkList__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next


if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(1)
    print(dll.is_empty())
    print(dll.length())

    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.add(8)
    dll.insert(-1, 9)
    dll.travel()
    dll.insert(3, 100)
    dll.travel()
    dll.insert(10, 200)
    dll.travel()
    dll.remove(100)
    dll.travel()
    dll.remove(9)
    dll.travel()
    dll.remove(200)
    dll.travel()
