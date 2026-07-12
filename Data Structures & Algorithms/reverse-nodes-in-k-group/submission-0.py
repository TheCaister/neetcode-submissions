# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# having a helper function would definitely be goated
# let's start w/ pointer at head start. then, as long as start isn't None, we keep incrementing a forward pointer until we hit k, then
# with the 2 ranges, we can reverse that bit, return possibly the last pointer from that function, then point it to the new section

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        def getKthNode(start):
            cur_range = k

            while start and cur_range > 0:
                start = start.next
                cur_range -= 1
            
            return start

        while True:
            kth_node = getKthNode(groupPrev)

            if not kth_node:
                break

            groupNext = kth_node.next
            prev = groupNext
            cur = groupPrev.next

            while cur != groupNext:
                next = cur.next
                cur.next = prev

                prev = cur
                cur = next

            tmp = groupPrev.next
            groupPrev.next = kth_node
            groupPrev = tmp


        return dummy.next