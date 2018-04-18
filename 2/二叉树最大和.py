# -*- coding: utf-8 -*-

'''
二叉树各个路径的最大和
1. 题目
给定一棵二叉树，求各个路径的最大和，路径可以以任意节点作为起点和终点。

2. 思路
    * 先求出每个节点出发到左右子树的最大和
    * 然后遍历每个节点：求出经过该节点的路径的最大和
    * 经过一个节点的最大和有三种情况：
        > 1. 该节点本身
        > 2. 如果左孩子节点出发的最大和大于0，则该节点本身+左孩子几点出发的最大和
        > 3. 如果右孩子节点出发的最大和大于0，则在加上右孩子节点出发的最大和
    * 求出经过每个节点的最大和中最大的值

'''

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.maxPath=None
        
def maxSumPath(root):
    '''
    求每个从每个节点出发到左右孩子节点的最大和，存在在该节点的maxPath属性中
    '''
    if root is None:
        return 0
    else:
        if root.maxPath is not None:
            return root.maxPath
        else:
            left=maxSumPath(root.left)
            right=maxSumPath(root.right)
            root.maxPath=max(root.val,left+root.val,right+root.val)
            return root.maxPath
    
    
        
root=TreeNode(1)
root.left=TreeNode(2)
root.left.right=TreeNode(4)
root.left.left=TreeNode(6)
root.right=TreeNode(-5)
root.right.right=TreeNode(6)

maxSumPath(root)

def pre(root):
    '''求所有路径的最大和
    '''
    if root is None:
        return 0
    else:
        mid=root.val
        if root.left is not None and root.left.maxPath>0:
            mid+=root.left.maxPath
        if root.right is not None and root.right.maxPath>0:
            mid+=root.right.maxPath
        left=pre(root.left)
        right=pre(root.right)
        return max(left,right,mid)
        
print(pre(root))