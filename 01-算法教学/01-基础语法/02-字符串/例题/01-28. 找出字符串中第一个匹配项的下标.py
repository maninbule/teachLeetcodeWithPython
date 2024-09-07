'''
https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        for i in range(n): # 匹配的起点
            if i + len(needle) > n: #防止越界
                break
            # 取出长度为len(needle)的子字符串
            # 两个索引做差，就是slice的长度
            substr = haystack[i:i + len(needle)]
            if substr == needle:
                return i
        return -1