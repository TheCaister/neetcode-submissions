# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# hmm, seems simple enough....?
# for most cases, add
# otherwise, if it's over 9, get the carry over

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tracker = dummy
        carry_over = 0
        
        while l1 or l2:
            l1_num = l2_num = 0

            if l1:
                l1_num = l1.val
            if l2:
                l2_num = l2.val

            l1_l2_sum = l1_num + l2_num + carry_over

            if l1_l2_sum >= 10:
                l1_l2_sum -= 10
                carry_over = 1
            else:
                carry_over = 0
            
            new_node = ListNode(l1_l2_sum)
            tracker.next = new_node
            tracker = tracker.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry_over == 1:
            new_node = ListNode(1)
            tracker.next = new_node

        return dummy.next
        