'''
https://leetcode.cn/problems/intersection-of-two-arrays/?envType=problem-list-v2&envId=binary-search
'''
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        for i in range(len(nums2)):
            if i - 1>=0 and nums2[i-1] == nums2[i]:
                continue
            # 搜索条件：nums1[j] <= nums2[i] 的最大值
            # 答案：看这个最大值是不是nums2[i],是的话，就存入答案数组
            left,right = 0,len(nums1)-1
            ans = -1
            while left <= right:
                mid = (left + right)//2
                if nums1[mid] <= nums2[i]:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            if ans != -1 and nums1[ans] == nums2[i]:
                res.append(nums2[i])
        return res