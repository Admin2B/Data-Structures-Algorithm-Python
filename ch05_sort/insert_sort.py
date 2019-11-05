# -*- encoding: utf-8 -*-

def insert_sort(alist):
    n=len(alist)
    for j in range(1,n):
        i = j
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
                i -= 1
            else:
                break
    return alist

if __name__=='__main__':
    l=[45, 86, 69, 6, 7, 98, 24, 86, 75, 3, 465, 364, 343, 5, 99,123,500]

    print(insert_sort(l))