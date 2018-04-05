# -*- coding: utf-8 -*-
"""
堆排序
1. 堆
    * 存储在数组中
    * 根节点i, 左孩子节点为2i+1,右孩子节点为2i+2 （下标从0开始时）
    * 满足条件：根节点的值大于（小于）左右孩子节点的值
2. 调整堆
    * 当左右孩子都满足堆的定义,父节点不满足时，调整成一个合法的堆
    * 从父节点和左右孩子节点中找到最大的，如果父节点不是最大的值就与最大值节点交换
    * 递归的调整
    
3. 步骤：
(1) 建立大（小）顶堆
    * 自底向上调整堆
(2) 排序
    * 堆顶元素与最后的元素交换，堆大小减1
    * 调整堆
"""

def adjust_heap(A,i,size):
    left=i*2+1
    right=i*2+2
    largest=i
    if left<size and A[largest]<A[left]:
        largest=left
    if right<size and A[largest]<A[right]:
        largest=right
    if largest!=i:
        A[i],A[largest]=A[largest],A[i]
        adjust_heap(A,largest,size)

def heap_sort(A):
    #1. 自底向上建立大顶堆
    l=len(A)
    for i in range(l//2)[::-1]:
        adjust_heap(A,i,l)
    #2. 排序
    for j in range(0,l)[::-1]:
        A[j],A[0]=A[0],A[j] #交换
        adjust_heap(A,0,j)
        
A=[2,3,1,0,4,5,7]
heap_sort(A)
print(A)