# -*- coding: utf-8 -*-
"""
计数排序
1. 前提条件： 假设数组A中的元素都是0到k之间的数，k=O(n)
2. 思想：
    * 统计数组A中小于元素A[i]的个数，这样就可以得到A[i]排序后的位置
3. 过程
    * 统计元素A[i]出现的个数C[A[i]]
    * 累加得到小于等于A[i]的元素个数：C[A[i]]=C[A[i]]+C[A[i]-1]
"""

def count_sort(A,k):
    l=len(A)
    B=[-1]*l
    C=[0 for i in range(k)]
    # 1. 统计A[i]的元素出现的次数
    for a in A:
        C[a]+=1
    # 2. 累加得到小于等于A[i]的元素个数
    for i in range(1,k):
        C[i]=C[i]+C[i-1]
    # 3. 遍历A,输出有序数组到B
    for a in A:
        #a的位置为C[a]
        B[C[a]-1]=a
        #a的位置减1
        C[a]-=1
    return B

A=[1,2,5,9,6,4,3,2,8,2,1,7,6,4]
B=count_sort(A,10)
print(B)

