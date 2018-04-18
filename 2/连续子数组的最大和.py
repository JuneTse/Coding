# -*- coding: utf-8 -*-
"""
连续子数组的最大和
1. 题目
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。你会不会被他忽悠住？(子向量的长度至少是1)

2. 思路：分治法
    * 将数组分为左右两部分：left, right，分为三种情况
    (1) 最大和在left中，递归
    (2) 最大和在right中，递归
    (3) 最大和跨越left和right
"""

def midMax(A,s,e,mid):
    leftMax=A[mid-1]
    leftTemp=0
    for d in A[s:mid][::-1]:
        leftTemp+=d
        if leftTemp>leftMax:
            leftMax=leftTemp
    rightMax=A[mid]
    rightTemp=0
    for d in A[mid:e]:
        rightTemp+=d
        if rightMax<rightTemp:
            rightMax=rightTemp
    return rightMax+leftMax

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if array is None:
            return None
        mid=len(array)//2

        l=len(array)
        if l==0:
            return 0
        if l==1:
            return array[0]
        else:
            left=self.FindGreatestSumOfSubArray(array[:mid])
            right=self.FindGreatestSumOfSubArray(array[mid:])
            mid=midMax(array,0,l,mid)
            return max([mid,left,right])
        
        
a=[6,-3,-2,7,-15,1,2,2]
s=Solution()
res=s.FindGreatestSumOfSubArray(a)
print(res)
