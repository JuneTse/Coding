#coding:utf-8

'''
1. 插入排序
    * 原址排序，不需要额外的空间
    * 时间复杂度：O(n^2)
思想：
    * 前k个是有序的
    * 后面n-k个是无序的
    * 第k+1个分别于前面的比较，并后移一位，形成k+1个有序的
'''

def insert_sort(data):
    for k in range(1,len(data)):
        #数组data中前k-1个是有序的
        key=data[k]
        for i in range(0,k)[::-1]:
            if data[i]>key:
                #如果data[i]大于key,data[i]就向后移动一位
                data[i+1]=data[i]
                data[i]=key
            else:
                #否则，就结束循环
                break
        
    return data

data=[4,5,6,3,2,1,9]
data=insert_sort(data)
print(data)