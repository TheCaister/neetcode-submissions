# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# as we're building up the new list, let's prepare dummy pointer so that we don't lose track
# keep building until either list is exhausted, then attach it to the remaining one

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        tracker = result

        while list1 and list2:
            if list1.val < list2.val:
                
                tracker.next = list1
                list1 = list1.next
            else:
                tracker.next = list2
                list2 = list2.next
            
            tracker = tracker.next
        
        if not list1:
            tracker.next = list2
        
        if not list2:
            tracker.next = list1

        return result.next
