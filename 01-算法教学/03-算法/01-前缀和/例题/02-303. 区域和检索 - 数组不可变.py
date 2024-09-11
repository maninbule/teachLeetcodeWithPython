
'''
https://leetcode.cn/problems/range-sum-query-immutable/description/
'''
from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pre = [0] * n
        self.pre[0] = nums[0]
        for i in range(1,n):
            self.pre[i] = self.pre[i-1] + nums[i]


    def sumRange(self, left: int, right: int) -> int:
        res = self.pre[right]
        if left > 0:
            res -= self.pre[left - 1]
        return res




# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)