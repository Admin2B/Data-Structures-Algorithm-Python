# -*- encoding: utf-8 -*-

def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    left_ptr, right_ptr = 0, 0
    result = []
    while left_ptr<len(left) and right_ptr<len(right):
        if left[left_ptr] <= right[right_ptr]:
            result.append(left[left_ptr])
            left_ptr += 1
        else:
            result.append(right[right_ptr])
            right_ptr += 1
    result += left[left_ptr:]
    result += right[right_ptr:]
    return result

if __name__ == '__main__':
    l = [45, 86, 69, 6, 7, 98, 24, 86, 75, 3, 465, 364, 343, 5, 99, 123, 500]
    print(l)
    print(merge_sort(l))

