'''
https://leetcode.cn/problems/course-schedule/
'''

from typing import List
'''
1. 创建一个队列
2. 创建一个indegree[]数组，indegree[i] 就表示第i个点的入度次数
3. 建立一个邻接表adj[] adj[i] = [a,b,c] 就是表示a,b,c是点i的相邻点
4. 遍历所有的边，A->B, 把为B的点进行入度 + 1
5. 循环所有点，把入度为0的点，进行入队
6. 循环：
    当队列不为空，就取出队头的点，这个点出去的时候，把所指向的点的入度-1
    当发现-1之后，所指向的点入度为0了，就也加入队列
7. 结束循环之后，看一下出队的点有多少个，如果小于n，就表示图里面有环，
    如果等于n，就图里面没有环
    出队的顺序，就是拓扑序列
'''
from collections import deque
class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
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
        count = 0
        while len(q) > 0:
            cur = q.popleft()
            count += 1
            for nexty in adj[cur]:
                indegree[nexty] -= 1
                if indegree[nexty] == 0:
                    q.append(nexty)
        if count == n:
            return True
        else:
            return False

'''
time: O(n) n是点的个数
space: O(n)
'''








