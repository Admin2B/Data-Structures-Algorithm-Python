# -*- encoding: utf-8 -*-

def select_sort(alist):
    min_index=0
    n=len(alist)
    for j in range(n-1):
        min_index=j
        for i in range(j+1,n):
            if alist[min_index]>alist[i]:
                min_index=i
        alist[j],alist[min_index]=alist[min_index],alist[j]
    return alist


if __name__=='__main__':
    l = [45, 86, 69, 6, 7, 98, 24, 86, 75, 3, 465, 364, 343, 5, 99, 123, 500]
    print(select_sort(l))