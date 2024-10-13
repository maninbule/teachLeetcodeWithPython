'''
https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/description/?envType=problem-list-v2&envId=breadth-first-search
'''
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
思路：
正常bfs即可
得到[[3],[9,20],[15,7]]
对这个数组进行翻转得到答案
[[15,7],[9,20],[3]]
'''
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            size = len(q)
            val_of_level = []
            for i in range(size):
                curNode = q.popleft()
                val_of_level.append(curNode.val)
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            res.append(val_of_level)
        left,right = 0,len(res)-1
        while left < right:
            res[left],res[right] = res[right],res[left]
            left += 1
            right -= 1
        return res