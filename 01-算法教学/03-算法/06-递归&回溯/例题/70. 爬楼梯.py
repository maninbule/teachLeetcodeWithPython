'''
https://leetcode.cn/problems/climbing-stairs/
'''

class Solution:
    def __init__(self):
        self.record = dict() # {n:answer of n}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in self.record:
            return self.record[n]
        ans1 = self.climbStairs(n-1)
        ans2 = self.climbStairs(n-2)
        self.record[n] = ans1 + ans2
        return ans1 + ans2

'''
时间复杂度：O(n) 
空间复杂度: O(h) h是递归树的高度，占用了栈空间
'''