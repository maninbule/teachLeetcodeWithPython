'''
https://leetcode.cn/problems/is-subsequence/description/
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in range(len(s)):
            # 现在去匹配s[i]
            while j < len(t) and t[j] != s[i]:
                j += 1
            # j要么越界了： 说明没有字母和s[i]进行匹配了
            # j要么就是走到了t[j] == s[i]的位置了，就是匹配上了
            if j == len(t):
                return False
            j += 1
        return True

'''
时间复杂度： O(n + m) n是s的长度，m是t的长度
空间复杂度：O(1)

'''