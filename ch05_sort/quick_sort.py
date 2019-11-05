# -*- encoding: utf-8 -*-

def quick_sort(alist,first,last):
    if first>=last:
        return alist
    mid_val = alist[first]
    low, high = first, last
    while low < high:
        while low < high and alist[high] >= mid_val:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_val:
            low += 1
        alist[high] = alist[low]
    alist[low]=mid_val
    quick_sort(alist,first,low-1)
    quick_sort(alist,low+1,last)
    return alist

if __name__ == '__main__':
    l = [45, 86, 69, 6, 7, 98, 24, 86, 75, 3, 465, 364, 343, 5, 99,123,500]
    print(quick_sort(l,0,len(l)-1))
