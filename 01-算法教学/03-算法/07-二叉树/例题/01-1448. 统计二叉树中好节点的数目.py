'''
https://leetcode.cn/problems/count-good-nodes-in-binary-tree/description/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.count = 0
        self.dfs(root,root.val)
        return self.count
    def dfs(self,curNode:TreeNode,MaxOfPath:int):
        if curNode.val == MaxOfPath:
            self.count += 1
        if curNode.left:
            self.dfs(curNode.left, max(curNode.left.val, MaxOfPath))
        if curNode.right:
            self.dfs(curNode.right, max(curNode.right.val, MaxOfPath))