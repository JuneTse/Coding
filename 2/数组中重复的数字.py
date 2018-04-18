# -*- coding: utf-8 -*-
"""
数组中重复的数字
1. 题目
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

2. 思路
(1) 使用辅助数组存放每个数字的次数： C[i]存放数组i的次数

"""

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        C=[0]*len(numbers)
        for d in numbers:
            C[d]+=1
        for i in range(len(numbers)):
            if C[i]>1:
                duplication[0]=i
                return True
        return False
        
a=[2,1,3,0,4]
s=Solution()
s.duplicate(a,[-1])

        

