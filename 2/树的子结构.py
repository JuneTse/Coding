# -*- coding: utf-8 -*-
"""
树的子结构
1. 题目
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
2. 思路
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        def isAHasBTree(A,B):
            if B is None:
                return True
            if A is None:
                return False
            if A.val!=B.val:
                return False
            left=isAHasBTree(A.left,B.left)
            right=isAHasBTree(A.right,B.right)
            return left and right
        res=False
        if pRoot1!=None and pRoot2!=None:
            if(pRoot1.val==pRoot2.val):
                res=isAHasBTree(pRoot1,pRoot2)
            if res is False:
                res=isAHasBTree(pRoot1.left,pRoot2)
            if res is False:
                res=isAHasBTree(pRoot1.right,pRoot2)
            return res
        return res
        