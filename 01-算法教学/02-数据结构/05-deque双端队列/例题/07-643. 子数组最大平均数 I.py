
'''
https://leetcode.cn/problems/maximum-average-subarray-i/description/
'''
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        from collections import deque
        q = deque()
        total = 0
        res = None
        for x in nums:
            total += x
            q.append(x)
            if len(q) > k:
                total -= q.popleft()
            if len(q) == k:
                if res is None:
                    res = total / len(q)
                else:
                    res = max(res,total/len(q))
        return res
# time：O(n) space: O(n) 因为k最大可以是n，所有元素都放入了队列