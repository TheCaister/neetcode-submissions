# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# head should point to none
# a and b. make b point to a.
# might need to look 3 in the future. a, b, and c
# b points to a. get the new c by moving up, and repeat

# 3 2 1 0 None

# None 0 1 2 3
# a    b c
# a <- b c
#      a<-b c
#        a<-b c

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a, b, c = None, None, None

        if head:
            b = head
        
            if head.next:
                c = head.next

        while c:
            # print(f'b val: {b.val}')
            b.next = a

            a = b
            b = c
            c = c.next

        if b:
            b.next = a

        return b
        