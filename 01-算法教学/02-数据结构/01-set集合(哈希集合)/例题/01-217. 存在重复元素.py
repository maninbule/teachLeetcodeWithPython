'''
https://leetcode.cn/problems/contains-duplicate/description/?envType=problem-list-v2&envId=sorting
'''
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        st = set(nums)
        if n == len(st):
            return False
        else:
            return True

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set()
        for x in nums:
            if x in st:
                return True
            # 不在
            st.add(x)
        return False