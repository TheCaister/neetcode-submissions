"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

#  perhaps the simplest way would be to set up a hashmap
#  this requires fully populating the map

# wait, why can't we do mapping from 1 node in the list to the other? so old -> new mapping
# then, in the second pass we loop through both, and it'll be constant time to get the new node equivalent for random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        index = 0
        dummy = Node(0)
        new_list_tracker = dummy
        old_list_tracker = head

        while old_list_tracker:
            new_node = Node(old_list_tracker.val)
            new_list_tracker.next = new_node
            new_list_tracker = new_list_tracker.next

            old_to_new[old_list_tracker] = new_node

            old_list_tracker = old_list_tracker.next

        new_list_tracker = dummy.next
        old_list_tracker = head

        while new_list_tracker:
            if old_list_tracker.random:
                new_list_tracker.random = old_to_new[old_list_tracker.random]

            new_list_tracker = new_list_tracker.next
            old_list_tracker = old_list_tracker.next
        
        return dummy.next