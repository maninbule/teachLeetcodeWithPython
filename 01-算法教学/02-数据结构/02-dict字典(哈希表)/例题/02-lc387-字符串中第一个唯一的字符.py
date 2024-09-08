'''
https://leetcode.cn/problems/first-unique-character-in-a-string/description/
'''
from typing import List
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 使用dict对s的字符进行技术
        count = dict()
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        # 再次遍历s，去dict查询第一个只出现一次的元素的索引
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1
