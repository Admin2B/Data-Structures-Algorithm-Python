# -*- encoding: utf-8 -*-
from bubble_sort import bubble_sort
def bin_search(alist,item):
    n=len(alist)
    if n>0:
        mid=n//2
        if alist[mid]==item:
            return True
        elif item<alist[mid]:
            return bin_search(alist[:mid],item)
        else:
            return bin_search(alist[mid+1:],item)
    return False

def bin_search_(alist,item):
    n=len(alist)
    first,last=0,n-1
    while first <= last:
        mid=(first+last)//2
        if alist[mid]==item:
            return True
        elif item<alist[mid]:
            last=mid-1
        else:
            first=mid+1
    return False


if __name__=='__main__':
    l = [45, 86, 69, 6, 7, 98, 24, 86, 75, 3, 465, 364, 343, 5, 99,123,500]
    bubble_sort(l)
    print(bin_search(l,5))
    print(bin_search(l,600))
    print(bin_search_(l, 650))
    print(bin_search_(l, 86))

