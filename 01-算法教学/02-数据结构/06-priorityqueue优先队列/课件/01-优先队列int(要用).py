


'''

使用队列存入元组的方式：
最后一个元素是具体的内容，前面的都是优先级,数字越小优先级越大
PriorityQueue： 默认是从小到大排序，就是小的数，优先级更高
'''
from queue import PriorityQueue
def PriorityQueue_int():
    pq = PriorityQueue()
    pq.put(3)
    pq.put(1)
    pq.put(2)

    # 查询队列元素个数
    size = pq.qsize()
    print("队列中的元素个数:", size)  # 输出：队列中的元素个数: 3

    # 出队操作
    while not pq.empty():
        item = pq.get()
        print("出队元素:", item)

    # 再次查询队列元素个数
    size = pq.qsize()
    print("队列中的元素个数:", size)  # 输出：队列中的元素个数: 0


PriorityQueue_int()