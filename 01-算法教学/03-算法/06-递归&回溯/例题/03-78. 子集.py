'''
https://leetcode.cn/problems/subsets/description/
'''
from typing import List
import copy

class Solution:
    def __init__(self):
        self.result = []
    def dfs(self,nums:List[int],i:int,choose:list[int]):
        if i >= len(nums):
            self.result.append([x for x in choose])
            return
        # 选择第i个数
        choose.append(nums[i])
        self.dfs(nums,i + 1,choose)
        choose.pop()
        # 不选择第i个数
        self.dfs(nums,i + 1,choose)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        choose = []
        self.dfs(nums,0,choose)
        return self.result