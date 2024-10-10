'''
https://leetcode.cn/problems/valid-palindrome/description/?envType=problem-list-v2&envId=two-pointers
'''

'''
输入： 字符串
输出： bool
限制：只考虑字母和数字，字母不区分大小写

1. 转换字符串，转换成只保留数字和字母的，字母全部用小写表示
2. 对转换过后的字符串，做双指针算法
3. 定义左右指针，同时往中间走，一边走，一边看左右指针所指向的字符是否一样
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for c in s: # O(n)
            if c.isalpha() or c.isdigit():
                t += c.lower()
        # t就是转换之后的字符串了
        left,right = 0,len(t)-1
        while left < right: # O(n)
            if t[left] != t[right]:
                return False
            left += 1
            right -= 1
        return True
'''
时间复杂度：O(n) 转换字符串花费O(n) 双指针遍历的时候也是O(n) 
空间复杂度: O(n)
'''