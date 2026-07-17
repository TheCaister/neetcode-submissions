# keep track of cur min index

# we're in left half if left < mid

# if we're in the right half, we gotta look to the left
# if we're in the left half, we gotta look to the right

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = float('inf')

        while l <= r:
            if nums[l] <= nums[r]:
                print(f'l: {l}')
                min_num = min(min_num, nums[l])
            
            mid = l + ((r - l) // 2)

            print(f'mid: {mid}')
            
            
            is_left = True if nums[l] <= nums[mid] else False
            
            print(is_left)
            
            min_num = min(min_num, nums[mid])

            if is_left:
                l = mid + 1
            else:
                r = mid - 1

        return min_num
        
