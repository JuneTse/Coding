# -*- coding: utf-8 -*-
'''
快速排序：
1. 使用分治法的思想
    * 划分
    * 递归的求解
2. 原址排序，不需要额外的空间
3. 主要思想和步骤：
    * 输入数组A
    * 取A中的一个元素作为枢轴pivot
    * 划分：把小于pivot的放到pivot的前面，其他的放到后面 （有很多不同的方法可以做到）
    * 递归
'''

def partion1(A,p,r):
    '''划分方法1:
    1. 去最后一个为枢轴pivot
    2. 定义下标i为初始为开始位置
    3. 从左到右遍历，如果小于pivot就与第i个元素交换 （这样i的左边始终是小于pivot的）
    '''
    pivot=A[r-1]
    i=p
    for j in range(p,r-1):
        if A[j]<pivot:
            #如果比
            A[i],A[j]=A[j],A[i]
            i+=1
    A[i],A[r-1]=A[r-1],A[i]
    return i

def partion2(A,p,r):
    '''划分方法2:
    1. 取第一个为枢轴pivot
    2. 循环
        * 先从右往左遍历找到比pivot小的，放到前面
        * 然后从左到右遍历找到比pivot大的，放到后面
    '''
    pivot=A[p]
    i=p
    j=r-1
    while i<j:
        while i<j and pivot<=A[j]:
            j=j-1
        A[i]=A[j]
        while i<j and pivot>A[i]:
            i+=1
        A[j]=A[i]
    assert i==j
    A[i]=pivot
    return i
        
def quick_sort(A,p,r):
    if p<r:
        s=partion2(A,p,r)
        quick_sort(A,p,s)
        quick_sort(A,s+1,r)
        
A=[2,3,5,4,1,6,9,8]
quick_sort(A,0,len(A))
print(A)



