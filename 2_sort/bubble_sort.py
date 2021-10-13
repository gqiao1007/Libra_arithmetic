# _*_ coding: utf-8 _*_
"""
最优的时间复杂度为：O( n^2 ) ；
最差的时间复杂度为：O( n^2 )；
平均的时间复杂度为：O( n^2 )；

空间复杂度为：O(n)
"""



li = [54,26,93,17,77,31,44,55,20]
length = len(li)
for i in range(0, length):
    for j in range(length-1-i):
        if li[j]>li[j+1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print(li)