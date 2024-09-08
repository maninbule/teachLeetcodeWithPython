
'''
01-计算数组中k个连续数字的和

[1,2,3,4,5,6]
k = 3
第1个连续3个数为[1,2,3] = 6
第2个连续3个数为[2,3,4] = 9
第3个连续3个数为[3,4,5] = 12
第4个连续3个数为[4,5,6] = 15
返回 [6,9,12,15]
'''

from queue import Queue
def getSumOfK(arr:list[int],k:int)->list[int]:
    q = Queue()
    total = 0
    res = []
    for x in arr:
        total += x
        q.put(x)
        if q.qsize() > k:
            total -= q.get()
        if q.qsize() == k:
            res.append(total)
    return res

arr = [1,2,3,4,5,6]
print(getSumOfK(arr,3))