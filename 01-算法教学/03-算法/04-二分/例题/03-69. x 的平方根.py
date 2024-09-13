'''
https://leetcode.cn/problems/sqrtx/description/
'''

class Solution:
    def mySqrt(self, y: int) -> int:
        # 搜索条件： 满足x*x <= y  中x的最大值
        # 返回答案： x
        left,right = 0,y
        res = -1
        while left <= right:
            mid = (left + right)//2
            if mid * mid <= y:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res