# https://leetcode.com/problems/reverse-linked-list/description/
# 206. Reverse Linked List

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousNode = None
        
        while head:
            temp = head.next
            head.next = previousNode
            previousNode = head
            head = temp
        return previousNode
            