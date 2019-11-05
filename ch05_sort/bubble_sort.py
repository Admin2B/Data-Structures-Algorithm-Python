# -*- encoding: utf-8 -*-

def bubble_sort(alist):
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(n -1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:
            return alist
    return alist


if __name__ == '__main__':
    # l = [3,1,6,5,7]
    l = [45, 86, 69, 6, 7, 98, 24, 86, 75, 3, 465, 364, 343, 5, 99,123,500]
    print(bubble_sort(l))
