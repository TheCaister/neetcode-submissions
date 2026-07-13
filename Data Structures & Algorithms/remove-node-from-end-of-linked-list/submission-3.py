# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# let's keep same distance between 2 nodes, and also a prev node behind the slow one to prepare for removing
# or maybe not prev node
# let's have dumym, because we could update the head node
# next and next.next, we start at 1. keep going until we hit n

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        slow, fast = dummy, head

        slow.next = head

        while n > 1:
            fast = fast.next
            n -= 1
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        new_node = slow.next.next
        slow.next = new_node


        return dummy.next