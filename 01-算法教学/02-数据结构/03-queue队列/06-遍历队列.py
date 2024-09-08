
from queue import Queue
def trverseQueue(q:Queue):
    while not q.empty():
        item = q.get()  # 出队 [2,3]  [3]  []
        print("出队元素:", item)

