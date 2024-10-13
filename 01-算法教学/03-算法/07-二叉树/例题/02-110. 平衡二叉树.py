'''
https://leetcode.cn/problems/balanced-binary-tree/description/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.dfs(root)
        return self.res

    def dfs(self,curNode:TreeNode)->int:
        if curNode is None:
            return 0
        leftHeight = self.dfs(curNode.left)
        rightHeight = self.dfs(curNode.right)
        if abs(leftHeight - rightHeight) > 1:
            self.res = False
        return 1 + max(leftHeight,rightHeight)

