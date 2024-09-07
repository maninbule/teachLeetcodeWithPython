
from queue import Queue
def visit(q:Queue):
    if q.qsize() > 0:
        return q.queue[0]
    return None
