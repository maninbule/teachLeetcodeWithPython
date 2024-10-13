'''
https://leetcode.cn/problems/linked-list-cycle/description/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
1. 定义快慢指针，慢的一移动走1步，快的一次移动走2步
2. 放的位置，快指针先走，慢指针后走
3. 如果没有环，那么就是一条直线，肯定是快指针优先遇到链表末尾None
4. 如果有环，当两个指针走到环内的时候，由于速度的不同，相对距离会依次减少
    最终相遇。如果相遇了，就说明有环
5. 在环内他们的相对距离最大是n-1，所以最多再走n-1步，就一定相遇了
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        "c".end
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
'''
时间复杂度: O(n) 环外节点每个指针只会访问一次，同时在环内的时候，最多走n-1步 
空间复杂度: O(1) 
'''
