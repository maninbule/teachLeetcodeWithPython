'''
https://leetcode.cn/problems/minimize-maximum-of-array/description/
'''
import copy
from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        left,right = min(nums),max(nums)
        ans = -1
        while left <= right:
            mid = (left + right)//2
            tmp = copy.copy(nums)
            ok = True
            for i in range(len(tmp)-1,-1,-1):
                if tmp[i] > mid:
                    if i - 1>=0:
                        more = tmp[i] - mid
                        tmp[i-1] += more
                    else:
                        ok = False
            if ok:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
