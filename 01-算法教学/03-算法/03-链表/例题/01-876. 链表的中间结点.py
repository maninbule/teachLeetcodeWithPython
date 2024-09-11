'''

技巧：链表的遍历
https://leetcode.cn/problems/middle-of-the-linked-list/description/
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curNode = head
        while curNode is not None:
            length += 1
            curNode = curNode.next
        curNode = head
        for i in range(length // 2):
            curNode = curNode.next
        return curNode





