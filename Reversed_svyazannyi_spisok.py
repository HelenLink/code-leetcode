"""Given the head of a singly linked list, reverse the list, and return the reversed list."""
class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head:ListNode)-> ListNode:
        prev, cur = None, head

        while cur:
            cur.next = prev
            prev = cur
            cur = cur.next
        return prev

