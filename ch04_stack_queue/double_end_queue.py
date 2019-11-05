# -*- encoding: utf-8 -*-
class Dequeue:
    def __init__(self):
        self.__dequeue=[]
    def add_front(self,item):
        self.__dequeue.insert(0,item)
    def add_rear(self,item):
        self.__dequeue.append(item)
    def pop_front(self):
        return self.__dequeue.pop(0)
    def pop_rear(self):
        return self.__dequeue.pop()
    def is_empty(self):
        return not self.__dequeue
    def size(self):
        return len(self.__dequeue)


if __name__ == '__main__':
    deq=Dequeue()
    deq.add_front(1)
    deq.add_front(2)
    deq.add_rear(3)
    deq.add_rear(4)
    print(deq.pop_front())
    print(deq.pop_rear())
