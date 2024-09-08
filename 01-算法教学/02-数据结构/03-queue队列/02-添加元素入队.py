
from queue import Queue

# O(1)
def add(q:Queue,x):
    q.put(x)
    return q

