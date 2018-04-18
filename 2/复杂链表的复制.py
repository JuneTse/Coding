# -*- coding: utf-8 -*-
"""
复杂链表的复制
1.题目
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
2. 思路
    * 先复制每个节点：node.newNode=RandomListNoe(node.label)
    * 然后给每个节点的next和random赋值：
        (1) node.newNode.next=node.next.newNode
        (2) node.newNode.random=node.random.newNode
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        p=pHead
        while p is not None:
            p.newNode=RandomListNode(p.label)
            p=p.next
        p=pHead
        while p is not None:
            if p.next is not None:
                p.newNode.next=p.next.newNode
            if p.random is not None:
                p.newNode.random=p.random.newNode
            p=p.next
        return pHead.newNode
        
            
