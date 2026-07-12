# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# so you have an output list. maybe at each turn, you pull from all lists, and pick out the one with
# the smallest num. increment that list, then keep repeating. n^2 * m or list length * length of 1 list
# main challenge/potential improvement here is to find a way to efficiently find the list with smallest num
# you could possibly do something w/ min heap, where it's num -> node tuples. so we populate this heap, then pick from it
# so that's (n*m) * log (m * n)

# or, we could implement the merge sort algorithm
# this is... also n log n

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        def mergeLists(l1, l2):
            dummy = ListNode()
            tracker = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tracker.next = l1
                    l1 = l1.next
                else:
                    tracker.next = l2
                    l2 = l2.next
                
                tracker = tracker.next

            if l1:
                tracker.next = l1
            if l2:
                tracker.next = l2

            return dummy.next


        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                merged_lists.append(mergeLists(l1, l2))
            
            lists = merged_lists


        return lists[0]
        