'''
https://leetcode.cn/problems/binary-search/?envType=problem-list-v2&envId=binary-search
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 确定搜索空间
        left,right = 0,len(nums)-1
        res = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] <= target:
                res = mid
                left = mid + 1 # [mid + 1,right] 范围内继续去找更加接近target的index
            else: # target < nums[mid]
                right = mid - 1 # [left,mid - 1]
        if res == -1 or nums[res] != target:
            return -1
        else:
            return res