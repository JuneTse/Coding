# -*- coding: utf-8 -*-
#归并排序
'''
1. 归并排序：
    * 分治法： 分解->解决->合并
2. 步骤：
    * 输入数组A[p:q]
    * 分解成A[p:r],A[r:q]
    * 递归的分解A[p:r],A[r:q]
    * 两个有序数组，合并成一个有序数组
    * 合并的时候需要使用额外的空间
        
'''

def merge(A,p,q,r):
    a=A[p:r]
    b=A[r:q]
    i=0
    j=0
    k=p
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            A[k]=a[i]
            i+=1
        else:
            A[k]=b[j]
            j+=1
        k+=1
    if i<len(a):
        for d in a[i:]:
            A[k]=d
            k+=1
    elif j<len(b):
        for d in b[j:]:
            A[k]=d
            k+=1
    return A

def merge_sort(A,p,q):
    if p+1<q:
        r=(p+q)//2
        merge_sort(A,p,r)
        merge_sort(A,r,q)
        merge(A,p,q,r)
        
A=[3,4,1,2,5,0,3,4]

merge_sort(A,0,8)
print(A)
        



