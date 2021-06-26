# _*_ coding: utf-8 _*_
#二分查找
#时间复杂度Log2(N)


def bin_search(target: list, key):
    low = 0
    high = len(target) - 1
    while low <= high:
        mid = (low+high)//2
        if key < target[mid]:
            high = mid -1
        elif key > target[mid]:
            low = mid + 1
        else:
            return mid

target = [0,2,4,7,8,9,13]

print(bin_search(target, 4))



