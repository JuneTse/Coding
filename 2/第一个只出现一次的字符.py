# -*- coding: utf-8 -*-
"""
第一个只出现一次的字符
1. 题目
在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        ones=set()
        repeat=set()
        for c in s:
            if c in ones:
                repeat.add(c)
            else:
                ones.add(c)
        i=0
        for c in s:
            if c not in repeat:
                return i
            i+=1
        return -1
