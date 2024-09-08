'''
https://leetcode.cn/problems/intersection-of-two-arrays/description/
'''
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = set(nums2)
        res = []
        for x in nums1:
            # 如果nums2是set，in的操作就是O(1)
            # 如果nums2是list，in的操作就是O(n)
            if x in nums2:
                res.append(x)
        return res
        # 如果nums2是list，in的操作等同于下面
        # for y in nums2:
        #     if x == y:
        #         res.append(x)