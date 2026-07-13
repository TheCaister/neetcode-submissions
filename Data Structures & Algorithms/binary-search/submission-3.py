# if when getting mid we round down, (r - l // 2)
# when updating window let's move left to mid + 1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            mid_num = nums[mid]

            if mid_num > target:
                r = mid - 1
            elif mid_num < target:
                l = mid + 1
            else:
                return mid
        
        return -1