# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# easiest way I can think of would be to use a deque, n time and space
# 1 more optimal way is to reverse the 2nd half


# 1. reverse 2nd half, returning head of 2nd half
# 2. start building, alternating between the 2 lists

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        slow = fast = dummy

        slow.next = head

# if odd, slow will be on majority half. if even, slow will be on the boundary
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        # now, prev should be the head of new list
        start = head

        while start and prev:
            after_start = start.next
            after_prev = prev.next
            start.next = prev
            prev.next = after_start

            start = after_start
            prev = after_prev

