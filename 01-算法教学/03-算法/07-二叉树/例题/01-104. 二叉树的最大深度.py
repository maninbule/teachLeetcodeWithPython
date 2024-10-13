'''
https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/?envType=problem-list-v2&envId=binary-tree
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 下面是参数传递的方式
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.res = 0
        self.dfs(root,1)
        return self.res
    def dfs(self,curNode:TreeNode,depth:int):
        if not curNode.left and not curNode.right:
            self.res = max(self.res,depth)
            return
        if curNode.left:
            self.dfs(curNode.left,depth + 1)
        if curNode.right:
            self.dfs(curNode.right,depth + 1)



# 下面是通过返回值传递
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.getDepth(root)

    def getDepth(self, curNode: TreeNode):
        if curNode is None:
            return 0
        leftDepth = self.getDepth(curNode.left)
        rightDepth = self.getDepth(curNode.right)
        return 1 + max(leftDepth, rightDepth)
