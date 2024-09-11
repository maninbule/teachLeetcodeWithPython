'''
https://leetcode.cn/problems/subarray-sum-equals-k/description/
'''
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # pre[right] - pre[left - 1] == k
        # pre[left - 1] = pre[right] - k
        pre = 0
        preCount = dict()
        preCount[pre] = 1
        res = 0
        for i in range(len(nums)):
            pre = pre + nums[i]
            lastpre = pre - k
            if lastpre in preCount:
                res += preCount[lastpre]
            if pre in preCount:
                preCount[pre] += 1
            else:
                preCount[pre] = 1
        return res