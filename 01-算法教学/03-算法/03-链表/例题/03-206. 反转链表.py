'''
https://leetcode.cn/problems/reverse-linked-list/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curNode = head
        while curNode is not None:
            nextNode = curNode.next
            curNode.next = dummy.next
            dummy.next = curNode
            curNode = nextNode
        return dummy.next
