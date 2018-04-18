# -*- coding: utf-8 -*-
"""
顺时针打印矩阵
1. 题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
2. 思路
(1)递归
    * 先顺时针输出当前数组的最外层
    * 递归的输出子数组的最外层
"""

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        col=len(matrix[0])
        row=len(matrix)
        
        def bound(matrix,i1,j1,i2,j2):
            if i1>=i2 or j2<=j1:
                return []
            else:
                res=[]
                for j in range(j1,j2):
                    res.append(matrix[i1][j])
                for i in range(i1+1,i2):
                    res.append(matrix[i][j2-1])
                if i1!=i2-1:
                    for j in range(j1,j2-1)[::-1]:
                        res.append(matrix[i2-1][j])
                if j1!=j2-1:
                    for i in range(i1+1,i2-1)[::-1]:
                        res.append(matrix[i][j1])
                return res+bound(matrix,i1+1,j1+1,i2-1,j2-1)
            
        res=bound(matrix,0,0,row,col)
        return res
    
s=Solution()
#m=[[1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12],
#   [13,14,15,16]]
m=[[1],[2],[3],[4],[5]]
res=s.printMatrix(m)
print(res)
        

