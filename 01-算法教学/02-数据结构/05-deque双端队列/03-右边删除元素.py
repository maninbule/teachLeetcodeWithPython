
from collections import deque

def removeRight(dq:deque):
    if len(dq) > 0:
        dq.pop()
    return dq