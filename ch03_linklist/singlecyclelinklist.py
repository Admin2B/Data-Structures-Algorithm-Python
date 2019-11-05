# -*- encoding: utf-8 -*-
from singlelinklist import SingleLinkList, Node

class SingleCycleLinkList(SingleLinkList):
    def __init__(self, node=None):
        self._SingleLinkList__head = node
        if node:
            node.next = node


    def length(self):
        if self.is_empty():
            return 0
        cur = self._SingleLinkList__head
        count = 1
        while cur.next is not self._SingleLinkList__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self._SingleLinkList__head
        while cur.next is not self._SingleLinkList__head:
            print(cur.item, end=" ")
            cur = cur.next
        print(cur.item)

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._SingleLinkList__head = node
            node.next = node
        else:
            cur = self._SingleLinkList__head
            while cur.next is not self._SingleLinkList__head:
                cur = cur.next
            node.next = self._SingleLinkList__head
            self._SingleLinkList__head=node
            cur.next = self._SingleLinkList__head

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._SingleLinkList__head = node
            node.next = node
        else:
            cur = self._SingleLinkList__head
            while cur.next is not self._SingleLinkList__head:
                cur = cur.next
            node.next = self._SingleLinkList__head
            cur.next = node


    def remove(self, item):
        if self.is_empty():
            return
        cur = self._SingleLinkList__head
        pre = None
        while cur.next is not self._SingleLinkList__head:
            if cur.item == item:
                if cur == self._SingleLinkList__head:
                    rear=self._SingleLinkList__head
                    while rear.next is not self._SingleLinkList__head:
                        rear=rear.next
                    self._SingleLinkList__head = cur.next
                    rear.next=self._SingleLinkList__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.item is item:
            if cur is self._SingleLinkList__head:
                self._SingleLinkList__head = None
            else:
                pre.next = cur.next

    def search(self, item):
        if self.is_empty():
            return False
        cur = self._SingleLinkList__head
        while cur.next is not self._SingleLinkList__head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        if cur.item is item:
            return True
        return False


if __name__=='__main__':
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.add(8)
    ll.insert(-1, 9)
    ll.travel()
    ll.insert(3, 100)
    ll.travel()
    ll.insert(10, 200)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
