
from queue import Queue

# O(1)
def remove(q:Queue):
    if q.qsize() > 0: # 等同if len(q.queue) > 0:
        return q.get()
    return None

q =Queue()
q.put(1)
q.put(2)
q.put(3)

x = q.get()
print(x)
print("size = ",q.qsize())
