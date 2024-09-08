
from queue import Queue
def visit(q:Queue):
    if q.qsize() > 0:
        return q.queue[0]
    return None

q =Queue()
q.put(1)
q.put(2)
q.put(3)

x = q.queue[0]
print(x)
print("size = ",q.qsize())
