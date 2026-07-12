# naive way would be to set to 0 when an operation is done, and increment everything else
# then when a put exceeds, remove the node with the highest counter
# so this means for each node, also store their time in use
# for gets, if we use hashmap it'd be o(n) to increment all items
# for puts, it's o(n) time to update all, scan through and remove


# quick way to get = hashmap
#  quick way to update the least recently used, some fandangoing with linked lists
#  by moving the least recently used to the end of a list efficiently, everything else lines up naturally for picking off
#  we need 2. insert and remove. insert, we always insert at the end. remove, we do some fandangoing

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.capacity = capacity

        # for scaffolding, we connect left and right
        self.left.next = self.right
        self.right.prev = self.left

    def remove_node(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert_at_end(self, node: Node):
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.prev, node.next = prev, self.right
        

    def get(self, key: int) -> int:
        if key in self.cache:
            found_node = self.cache[key]
            self.remove_node(found_node)
            self.insert_at_end(found_node)

            return found_node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])

        new_node = Node(key, value)
        
        # print(new_node)
        self.cache[key] = new_node
        self.insert_at_end(new_node)

        # handle for capacity
        if len(self.cache) > self.capacity:
            chud_node = self.left.next
            self.remove_node(chud_node)
            del self.cache[chud_node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)