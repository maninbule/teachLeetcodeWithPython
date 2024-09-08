'''
https://leetcode.cn/problems/merge-similar-items/description/
'''
from typing import List

class Solution:
    # 假如items n个元素，items是m个元素
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # 创建一个dict存储价值和数量
        count = dict()
        for x,y in items1:  # O(n)
            count[x] = y
        for x,y in items2: # O(m)
            if x in count: # O(1)
                count[x] += y
            else:
                count[x] = y
        # for dict.items()
        res = []
        for key,value in count.items(): # O(n + m)
            res.append([key,value])
        # 再排序
        res.sort(key = lambda x:x[0]) # O((n + m) * log(n + m))
        return res

# 时间复杂度： O((n + m) * log(n + m))
