# _*_ coding: utf-8 _*_

"""
时间复杂度:O(n^2)
空间复杂度：O(1)
"""
lis = [85, 28, 53, 72, 14, 1, 31, 52, 69, 17, 75, 12, 31, 41, 83]
length = len(lis)
print(lis)

def insert_sort(li):
    for i in range(1,length):
        shaobing = li[i]
        j = i-1
        while j >= 0 and li[j] > shaobing:
            li[j], li[j+1] = li[j+1], li[j]
            j -= 1
    return li

a = insert_sort(lis)
print(a)