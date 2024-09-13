'''
https://leetcode.cn/problems/search-insert-position/description/
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 搜索条件： < target的最大值
        # 返回答案： < target的最大值的索引 + 1

        left,right = 0,len(nums)-1
        res = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res + 1