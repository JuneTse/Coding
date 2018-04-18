# -*- coding: utf-8 -*-
"""
序列化二叉树
1. 题目
请实现两个函数，分别用来序列化和反序列化二叉树
2. 思路
    * 存储节点的值，左右孩子节点的位置

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, root):
        # write code here
        queue=[]
        if root is not None:
            queue.append(root)
        else:
            return ''
        s=[]
        left=[]
        right=[]
        i=0
        while len(queue)-i>0:
            node=queue[i]
            i+=1
            s.append(str(node.val))
            if node.left is not None:
                queue.append(node.left)
                left.append(str(len(queue)-1))
            else:
                left.append('-1')
            if node.right is not None:
                queue.append(node.right)
                right.append(str(len(queue)-1))
            else:
                right.append('-1')
        return ' '.join(s)+"\t"+' '.join(left)+"\t"+' '.join(right)
    def Deserialize(self, s):
        # write code here
        if s is None or s=='':
            return None
        val,left,right=s.split('\t')
        val=list(map(int,val.split()))
        left=list(map(int,left.split()))
        right=list(map(int,right.split()))
        
        def buildTree(val,left,right,i):
            root=TreeNode(val[i])
            if left[i]!=-1:
                root.left=buildTree(val,left,right,left[i])
            if right[i]!=-1:
                root.right=buildTree(val,left,right,right[i])
            return root
        root=buildTree(val,left,right,0)
        return root
    
s=Solution()
t=TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(3)

res=s.Serialize(t)
print(res)

newTree=s.Deserialize(res)
            
