'''
https://leetcode.cn/problems/binary-tree-right-side-view/
'''
from typing import List, Optional

'''
思路：在bfs的基础上，存储每一层的最后一个节点即可
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            size = len(q)
            for i in range(size):
                curNode = q.popleft()
                if i == size - 1:
                    res.append(curNode.val)
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
        return res