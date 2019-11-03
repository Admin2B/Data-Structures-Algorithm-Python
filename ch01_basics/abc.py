# -*- encoding: utf-8 -*-
"""
@File    : abc.py
@Time    : 2019/11/3 0003 15:47
@Author  : xxx
@Email   : no email
@Software: PyCharm
"""
import time

# def abc():
#     for a in range(0,1001):
#         for b in range(0,1001):
#             for c in range(0,1001):
#                 if a+b+c==1000 and a**2+b**2==c**2:
#                     print(a,b,c)

def abc():
    for a in range(0,1001):
        for b in range(0,1001):
            c=1000-a-b
            if a**2+b**2==c**2:
                print(a,b,c)

from timeit import Timer
def test1():
    li = []
    for i in range(10000):
        li.append(i)

def test2():
    li=[]
    for i in range(10000):
        li = li +[i]
def test3():
    li = [i for i in range(10000)]

def test4():
    li=list(range(10000))
def test5():
    li=[]
    for i in range(10000):
        li.extend([i])
def test6():
    li=[]
    for i in range(10000):
        li.append(i)

def test7():
    li=[]
    for i in range(10000):
        li.insert(0,i)

if __name__=='__main__':
    # start_time=time.time()
    # abc()
    # end_time=time.time()
    # print("work time:",end_time-start_time)

    timer1=Timer("test1()","from __main__ import test1")
    print ("append:",timer1.timeit(1000))

    timer2 = Timer("test2()", "from __main__ import test2")
    print("+:", timer2.timeit(1000))

    timer3 = Timer("test3()", "from __main__ import test3")
    print("[i for i in range()]:", timer3.timeit(1000))

    timer4 = Timer("test4()", "from __main__ import test4")
    print("list(range()):", timer4.timeit(1000))

    timer5 = Timer("test5()", "from __main__ import test5")
    print("extend:", timer5.timeit(1000))

    timer6 = Timer("test6()", "from __main__ import test6")
    print("append:", timer6.timeit(1000))

    timer7 = Timer("test7()", "from __main__ import test7")
    print("insert:", timer7.timeit(1000))



