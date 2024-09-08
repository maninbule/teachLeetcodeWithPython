
'''
https://leetcode.cn/problems/maximum-nesting-depth-of-the-parentheses/description/
'''

class Solution:
    def maxDepth(self, s: str) -> int:
        sk = []
        res = 0
        for c in s:
            if c == ')':
                sk.pop()
            elif c == '(':
                sk.append('(')
                res = max(res,len(sk))
        return res

# 时间复杂度是:O(n) n就是字符串元素的数量
# 空间复杂度: O(n) ((()))((()))左括号的数量最多可以是一半的字符数量  O(n/2) = O(n)


class Solution:
    def maxDepth(self, s: str) -> int:
        sk = 0
        res = 0
        for c in s:
            if c == ')':
                sk -= 1
            elif c == '(':
                sk += 1
                res = max(res,sk)
        return res
# 时间复杂度是:O(n) n就是字符串元素的数量
# 空间复杂度: O(1)
