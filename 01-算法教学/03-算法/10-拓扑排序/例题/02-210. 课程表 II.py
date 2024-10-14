'''
https://leetcode.cn/problems/course-schedule-ii/description/
'''
from typing import List

from collections import deque
class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        q = deque()
        indegree = [0] * n
        adj = [[] for i in range(n)]
        for x,y in pre:
            # x <- y
            adj[y].append(x)
            indegree[x] += 1
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        order = []
        while len(q) > 0:
            cur = q.popleft()
            order.append(cur)
            for nexty in adj[cur]:
                indegree[nexty] -= 1
                if indegree[nexty] == 0:
                    q.append(nexty)
        if len(order) != n:
            return []
        else:
            return order