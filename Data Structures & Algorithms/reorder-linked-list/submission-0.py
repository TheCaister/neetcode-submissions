# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# easiest way I can think of would be to use a deque, n time and space

from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue_stack = deque()
        dummy = ListNode()


        while head:
            queue_stack.append(head)
            head = head.next

        while queue_stack:
            dummy.next = queue_stack.popleft()
            dummy = dummy.next

            if queue_stack:
                dummy.next = queue_stack.pop()
                dummy = dummy.next
            
            dummy.next = None