'''
https://leetcode.cn/problems/path-sum/description/
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.dfs(root,root.val,targetSum)

    def dfs(self,curNode:TreeNode,curPathSum:int,targetSum:int)->bool:
        if not curNode.left and not curNode.right:
            if curPathSum == targetSum:
                return True
            else:
                return False
        if curNode.left:
            res = self.dfs(curNode.left,curPathSum + curNode.left.val,targetSum)
            if res == True:
                return True
        if curNode.right:
            res = self.dfs(curNode.right,curPathSum + curNode.right.val,targetSum)
            if res == True:
                return True
        return False
'''
时间复杂度： O(n) 因为每一个节点只需要访问一次
空间复杂度： O(h) h就是树的最大深度，占用的栈空间
'''