# -*- coding: utf-8 -*-
'''
输入n个数，找到最小的k个
'''
######################### 使用list保存前k个    ############################
#插入排序
def insert_sort(data):
    n=len(data)
    for i in range(2,n):
        key=data[i]
        for j in range(0,i)[::-1]:
            if data[j]>key:
                data[j+1]=data[j]
                data[j]=key
    return data
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput)<k or k==0:
            return []
        # write code here
        topk=insert_sort(tinput[:k])
        for d in tinput[k:]:
            if d<topk[k-1]:
                topk[k-1]=d
                for i in range(k-1)[::-1]:
                    if d<topk[i]:
                        topk[i+1]=topk[i]
                        topk[i]=d
        return topk
    
data=[4,5,1,6,2,7,3,8]
s=Solution()
print(s.GetLeastNumbers_Solution(data,10))


########################### 使用大顶堆保存前k个 ###################################

def adjust_max_heat(data,i,size):
    '''左右孩子都是大顶堆时，根节点不符合大顶堆的要求，调整成为大顶堆
    '''
    large=i
    left=2*i
    right=2*i+1
    if  left<size and data[left]>data[large]:
        large=left
    if right<size and data[right]>data[large]:
        large=right
    if i!=large:
        data[i],data[large]=data[large],data[i]
        adjust_max_heat(data,large,size)
        
#建立大顶堆
def build_max_heat(data):
    '''
    1. 根节点i, 左孩子2i+1, 右孩子2i+2
    2. 自底向上建立堆
    '''
    for i in range(len(data)//2)[::-1]:
        adjust_max_heat(data,i,len(data))
        

class Solution2:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput)<k or k==0:
            return []
        topk=tinput[:k]
        build_max_heat(topk)
        
        for d in tinput[k:]:
            #如果d小于堆顶元素，替换堆顶元素并重新调整堆
            if d<topk[0]:
                topk[0]=d
                adjust_max_heat(topk,0,k)
        
        #排序：堆顶元素放到堆的最后，堆大小减1
        for j in range(1,k)[::-1]:
            topk[j],topk[0]=topk[0],topk[j]
            adjust_max_heat(topk,0,j)
        return topk
s=Solution2()
res=s.GetLeastNumbers_Solution(data,4)
print(res)
        
        
        

        