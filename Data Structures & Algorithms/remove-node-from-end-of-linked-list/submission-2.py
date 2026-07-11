# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# seems that we can't get the nth from the end without traversing the whole list
#  1. get the length of the length by incrementing counter
#  2. prepare 2 pointers a at None and b at head, and start moving them up until b hits the nth position
#  3. a = b.next
# when to stop b? at length - n. this should work as long as b start w/ 0. treat b like index

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a, b = None, head

        length = 0
        cur_index = 0

        while b:
            length += 1
            b = b.next
        
        b = head

        while cur_index < length - n:
            a = b
            b = b.next
            cur_index += 1
        
        if a:
            a.next = b.next
            return head
        else:
            return b.next