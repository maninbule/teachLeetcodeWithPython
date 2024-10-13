'''
https://leetcode.cn/problems/find-largest-value-in-each-tree-row/description/
'''
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            size = len(q)
            mx = None
            for i in range(size):
                curNode = q.popleft()
                if mx is None:
                    mx = curNode.val
                else:
                    mx = max(mx,curNode.val)
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            res.append(mx)
        return res
'''
时间复杂度：O(n) 每个点都需要访问一次，n是节点的个数
空间复杂度：O(h) h就是树的高度，因为每一层只需要存储一个最大值
'''
