

# 入队和出队，是logn时间复杂度
def PriorityQueue_node():
    from queue import PriorityQueue
    class Node:
        def __init__(self,x,y,content):
            self.x = x
            self.y = y
            self.content = content
        def __lt__(self,other): # less
            if self.x != other.x:
                return self.x < other.x
            else:
                return self.y > other.y

    # class Node:
    #     def __init__(self,x):
    #         self.x = x
    #     def __lt__(self, other):
    #         return self.x > other.x

    pq = PriorityQueue()
    # 入队操作
    pq.put(Node(3,2,'banana1'))
    pq.put(Node(3, 1, 'banana2'))
    pq.put(Node(2, 3, 'orange'))

    # 查询队列元素个数
    size = pq.qsize()
    print("队列中的元素个数:", size)  # 输出：队列中的元素个数: 3

    # 出队操作
    while not pq.empty():
        item = pq.get()
        print("出队元素:", item.x,item.y,item.content)

    # 再次查询队列元素个数
    size = pq.qsize()
    print("队列中的元素个数:", size)  # 输出：队列中的元素个数: 0

PriorityQueue_node()
