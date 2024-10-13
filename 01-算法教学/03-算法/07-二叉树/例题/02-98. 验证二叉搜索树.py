'''
https://leetcode.cn/problems/validate-binary-search-tree/description/
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder = []
        self.dfs(root)
        for i in range(1,len(self.inorder)):
            if self.inorder[i-1] >= self.inorder[i]:
                return False
        return True
    def dfs(self,curNode:TreeNode):
        if curNode is None:
            return
        if curNode.left:
            self.dfs(curNode.left)
        self.inorder.append(curNode.val)
        if curNode.right:
            self.dfs(curNode.right)