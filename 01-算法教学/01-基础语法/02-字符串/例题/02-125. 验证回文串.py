'''
https://leetcode.cn/problems/valid-palindrome/description/?envType=problem-list-v2&envId=string
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for c in s:
            if c.isalpha() or c.isdigit():
                t += c.lower()
        if t == t[::-1]:
            return True
        else:
            return False