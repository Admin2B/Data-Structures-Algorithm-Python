# -*- encoding: utf-8 -*-

def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:  # gap>0
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return alist


if __name__ == '__main__':
    l=[45, 86, 69, 6, 7, 98, 24, 86, 75, 3, 465, 364, 343, 5, 99,123,500]

    print(shell_sort(l))
