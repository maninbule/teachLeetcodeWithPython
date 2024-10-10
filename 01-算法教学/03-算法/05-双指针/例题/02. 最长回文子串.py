'''
https://leetcode.cn/problems/longest-palindromic-substring/description/
'''

'''
1.目的：找出所有的回文子串
2.先去找可能的对称轴
3.对于每一个对称轴，定义left，rihgt在对称轴位置，left往左，right往右
    同步移动，直到移动到s[left] != s[right] 或者left，right出现了越界
    然后回文子串就是[left + 1,right-1]这部分，+1 和 -1是因为s[left] != s[right]
4. 更新长度最长的回文子串
'''

class Solution:
    # O(n)
    def getString(self,s:str,left:int,right:int)->str:
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        # s[left],s[right] 不同，或者越界了
        left += 1
        right -= 1
        return s[left:right + 1]
    def longestPalindrome(self, s: str) -> str:
        res = ""
        # 2n- 1个对称轴
        for i in range(len(s)):
            # i就是对称轴
            cur = self.getString(s,i,i)
            if len(cur) > len(res):
                res = cur
            # i和i + 1之间是对称轴
            if i + 1 < len(s):
                cur = self.getString(s,i,i + 1)
                if len(cur) > len(res):
                    res = cur
        return res

'''
时间复杂度: O(n^2) 2n- 1个对称轴，每一个对称轴都要去遍历出最长的回文串
空间复杂度：O(n) 保存答案要新开一个字符串来存储
'''
