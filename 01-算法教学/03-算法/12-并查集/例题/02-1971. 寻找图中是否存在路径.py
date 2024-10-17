'''
https://leetcode.cn/problems/find-if-path-exists-in-graph/description/?envType=problem-list-v2&envId=union-find
'''
from typing import List


class Solution:
    def find(self, x: int):
        if x == self.fa[x]:
            return x
        else:
            root = self.find(self.fa[x])
            self.fa[x] = root  # 优化
            return root

    def union(self, x: int, y: int):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.fa[fx] = fy

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.fa = [i for i in range(n)]
        # 从0到n-1  fa[i] = i 刚开始每个所在集合的root就是它自己，因为还没有加边的时候，每个集合一个元素
        for x, y in edges:
            self.union(x, y)
        return self.find(source) == self.find(destination)
