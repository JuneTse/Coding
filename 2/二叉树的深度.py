# -*- coding: utf-8 -*-
"""
二叉树的深度
1. 题目
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
2. 思路
(1) 递归
TreeDepth=1+max(LeftDepth,RightDepth)
(2)非递归：层次遍历
    * 每个节点记录当前的层数
    * child=parent+1
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
######### 递归  ############
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        else:
            leftDepth=self.TreeDepth(pRoot.left)
            rightDepth=self.TreeDepth(pRoot.right)
            return 1+max(leftDepth,rightDepth)
        
        
        
########  非递归  ############       
class Solution1:
    
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        queue=[]
        if pRoot!=None:
            queue.append([pRoot,1])
        depth=1
        while len(queue)!=0:
            head,hDepth=queue.pop(0)
            depth=hDepth
            if head.left!=None:
                queue.append([head.left,hDepth+1])
            if head.right!=None:
                queue.append([head.right,hDepth+1])
        return depth
            
