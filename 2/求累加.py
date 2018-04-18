# -*- coding: utf-8 -*-
"""
求1+2+...+n
1. 题目
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
2. 思路
(1) 用try
(2) 用python sum函数
(3) 用&&的短路特性
"""

class Solution1:
    def Sum_Solution(self, n):
        # write code here
        res=n
        try:
            a=1/n
            res+=self.Sum_Solution(n-1)
        except:
            pass
        return res
    
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return sum(list(range(1,n+1)))

s=Solution()
res=s.Sum_Solution(10)
print(res)