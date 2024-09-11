
'''
https://leetcode.cn/problems/running-sum-of-1d-array/description/
'''
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if nums is None:
            return None
        if len(nums) == 0:
            return []
        n = len(nums)
        pre = [0] * n
        # 起点
        pre[0] = nums[0]
        # 开始递推
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
        return pre