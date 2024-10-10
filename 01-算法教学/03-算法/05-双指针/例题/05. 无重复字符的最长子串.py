'''
https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
'''


'''
思路：
1. 找每一个以s[right] 结尾的最长不重复子串
2. 定义左右指针left,right
3. right逐步往右边走,使用哈希表来记录走过每个字母出现的次数
4. 如果发现s[right]次数为2了，就需要移动left指针，一直往右走
    直到让s[right]的次数变成1为止
    就求得了以s[right]为结尾的最长不重复子串
5. 就把最长的s[left] 到 s[right] 子串拿出来，只返回长度
'''
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        cnt = defaultdict(int)
        res = 0
        for right in range(len(s)):
            cnt[s[right]] += 1
            while cnt[s[right]] > 1:
                cnt[s[left]] -= 1
                left += 1
            # 到达这里区间[left,right]就是不重复的
            res = max(res,right - left + 1)
        return res
'''
时间复杂度: O(n) 左右指针最多都遍历n个字符，是O(n) + O(n)
空间复杂度：O(n) 因为开辟了一个哈希表
'''