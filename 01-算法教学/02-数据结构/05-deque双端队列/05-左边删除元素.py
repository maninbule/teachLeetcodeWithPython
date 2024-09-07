

from collections import deque

def removeLeft(dq:deque):
    if len(dq) > 0:
        dq.popleft()
    return dq