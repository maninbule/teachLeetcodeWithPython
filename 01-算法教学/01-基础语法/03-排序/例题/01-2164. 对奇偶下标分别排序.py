'''
https://leetcode.cn/problems/sort-even-and-odd-indices-independently/description/
'''
from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # 奇数索引 降序
        # 偶数索引 升序

        # nums拆成2个数组
        odd = nums[1:len(nums):2]
        even = nums[0:len(nums):2]
        # 分别排序
        odd.sort(key = lambda x:-x)
        even.sort(key = lambda x:x)
        # 合并： 用两个索引分别指向两个数组待加入res数组的元素
        res = []
        i = 0
        j = 0
        while i < len(odd) or j < len(even):
            # 交替执行，加偶数位置，奇数位置的元素
            if j < len(even):
                res.append(even[j])
                j += 1
            if i < len(odd):
                res.append(odd[i])
                i += 1
        return res