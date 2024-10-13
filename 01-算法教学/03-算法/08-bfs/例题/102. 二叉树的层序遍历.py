'''
https://leetcode.cn/problems/binary-tree-level-order-traversal/
'''
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
二叉树bfs的步骤：
1. 创建队列
2. 把root节点放入队列
3. 使用循环，反复从队列取出当前层的节点，取出当前层每一个节点，他会带动下一层节点再次入队
4. 当队列为空，就结束循环
'''
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return res
'''
时间复杂度: O(n) n就是二叉树的节点个数
空间复杂度: O(n) 需要存储每一个节点的值
'''
