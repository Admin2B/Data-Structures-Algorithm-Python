# -*- encoding: utf-8 -*-
# from singlelinklist import SingleLinkList, Node
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

# class SingleCycleLinkList(SingleLinkList):
class SingleCycleLinkList:
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node


    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.item, end=" ")
            cur = cur.next
        print(cur.item)

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head=node
            cur.next = self.__head

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < pos - 1:
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next is not self.__head:
            if cur.item == item:
                if cur == self.__head:
                    rear=self.__head
                    while rear.next is not self.__head:
                        rear=rear.next
                    self.__head = cur.next
                    rear.next=self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.item is item:
            if cur is self.__head:
                self.__head=None
            else:
                pre.next = cur.next

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next is not self.__head:
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