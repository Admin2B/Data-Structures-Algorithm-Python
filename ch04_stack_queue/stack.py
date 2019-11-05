# -*- encoding: utf-8 -*-

class Stack:
    def __init__(self):
        self.__stack=[]

    def push(self,item):
        self.__stack.append(item)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        if self.__stack:
            return self.__stack[-1]
        else:
            return None

    def is_empty(self):
        return not self.__stack

    def size(self):
        return len(self.__stack)

if __name__=='__main__':
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

