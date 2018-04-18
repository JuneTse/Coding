# -*- coding: utf-8 -*-
"""
二叉树的镜像
1. 题目
操作给定的二叉树，将其变换为源二叉树的镜像。
2. 思路
(1)递归：递归交换左右字子树
(2)非递归：层次遍历交换左右子树
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
########### 递归 ###########
class Solution1:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root!=None:
            root.left,root.right=root.right,root.left
            self.Mirror(root.left)
            self.Mirror(root.right)
        return root
    
######## 非递归 ##########
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        queue=[]
        if root is not None:
            queue.append(root)
        else:
            return None
        while len(queue)!=0:
            head=queue.pop(0)
            head.left,head.right=head.right,head.left
            if head.left!=None:
                queue.append(head.left)
            if head.right!=None:
                queue.append(head.right)
        return root

s=Solution()

a=[8,6,10,5,7,9,11]

root=TreeNode(8)
root.left=TreeNode(6)
root.left.left=TreeNode(5)
root.left.right=TreeNode(7)
root.right=TreeNode(10)
root.right.left=TreeNode(9)
root.right.left=TreeNode(11)

res=s.Mirror(root)
print(res)