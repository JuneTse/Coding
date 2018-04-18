# -*- coding: utf-8 -*-
"""
把数组排成最小的数
1. 描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
2. 思路：
    * 分治法，递归求解
    * 假如数组里有n个数
    * 把原问题分解成n个子问题，n个子问题里的最小值为最终的解
"""

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        def minNumer(numbers):
            if len(numbers)==0:
                return ""
            if len(numbers)==1:
                return numbers[0]
            else:
                minV=int(str(numbers[0])+str(minNumer(numbers[1:])))
                for i in range(len(numbers)):
                    v=int(str(numbers[i])+str(minNumer(numbers[:i]+numbers[i+1:])))
                    if v<minV:
                        minV=v
                return minV
            
        res=minNumer(numbers)
        return res
    
s=Solution()
a=[3,32,321]
res=s.PrintMinNumber(a)
print(res)