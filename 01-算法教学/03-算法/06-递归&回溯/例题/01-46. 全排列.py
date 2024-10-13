'''
https://leetcode.cn/problems/permutations/description/
'''
import copy
from typing import List
'''
递归结构：
    递归的每一层做的事情：
        选择一个之前没有被选则过的数,如果说之前有k个数没有选择过：
            那么这里就有k个分支，
    当选择完n个数的时候，就选出来一种方案
'''
class Solution:
    def __init__(self):
        self.result = []
    def dfs(self,nums:list[int],tag:list[bool],choose:list[int]):
        if len(choose) == len(nums):
            self.result.append([x for x in choose])
            return
        for i in range(len(nums)):
            if tag[i]:continue
            tag[i] = True
            choose.append(nums[i])
            self.dfs(nums,tag,choose)
            choose.pop()
            tag[i] = False
    def permute(self, nums: List[int]) -> List[List[int]]:
        tag = [False] * len(nums)
        choose = []
        self.dfs(nums,tag,choose)
        return self.result
