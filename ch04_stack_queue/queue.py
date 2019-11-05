# -*- encoding: utf-8 -*-

class Queue:
    def __init__(self):
        self.__queue=[]
    def enqueue(self,item):
        self.__queue.append(item)
    def dequeue(self):
        if self.__queue:
            return self.__queue.pop(0)
        else:
            return None
    def is_empty(self):
        return not self.__queue
    def size(self):
        return len(self.__queue)

if __name__=='__main__':
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.is_empty())
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
