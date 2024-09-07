
from queue import Queue
def remove(q:Queue):
    if q.qsize() > 0:
        return q.get()
    return None