# -*- coding: utf-8 -*-
"""
字符串排序
1. 题目
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
2. 思路
(1)递归： 分解成子问题求解
    * 如果len(s)==1：
        输出
    * 否则，分解为s[i], s[0:i]+s[i+1:n]
"""

class Solution:
    def Permutation(self, ss):
        if ss is None:
            return None
        res=[]
        # write code here
        def printStr(pre,s):
            if len(s)==1:
                #print(pre+s[0])
                res.append(pre+s[0])
            s=sorted(s)
            for i in range(len(s)):
                if i>0 and s[i]==s[i-1]:
                    continue
                printStr(pre+s[i],s[0:i]+s[i+1:])
        printStr('',ss)
        return res
        
ss="aab"
solu=Solution()
res=solu.Permutation(ss)
print(res)

