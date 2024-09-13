'''
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 第一个target的index，搜索条件： >= target 的最左边
        left,right = 0,len(nums)-1
        leftans = -1
        while left <= right:
            mid = (left + right)//2
            if target <= nums[mid]:
                leftans = mid
                right = mid - 1
            else:
                left = mid + 1
        if leftans != -1 and nums[leftans] != target:
            leftans = -1
        # 最后一个target的index,搜索条件：<= target 的最右边
        left,right = 0,len(nums)-1
        rightans = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] <= target:
                rightans = mid
                left = mid + 1
            else:
                right = mid - 1
        if rightans != -1 and nums[rightans] != target:
            rightans = -1
        return [leftans,rightans]