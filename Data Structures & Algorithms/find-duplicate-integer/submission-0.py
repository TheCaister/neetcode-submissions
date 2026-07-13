# we can think of this as a list of indexes to indexes.
# we notice that the values are bounded within a range, so there must be a loop somewhere, aka at least 2 indexes pointing to the same index
# so now, this problem decomposes to finding the starting point of this cycle
# another important thing to note is that you can't have 0 as value, so index 0 is the rocketing point and serves our algorithm well
# 

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

            print(f'slow: {slow}, fast: {fast}')
        
        return slow