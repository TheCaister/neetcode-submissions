# we could find the minimum first, then do some fancy modulo magic and treat it like a normal binary search
# or, do a binary search after we find pivot

# if mid > left, then look to the right
# if mid < left, then look to the left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = 0
        lowest_index = -1
        lowest_num = float('inf')

        while l <= r:
            if nums[l] < nums[r]:
                lowest_chunk_index = l

                if nums[lowest_chunk_index] < lowest_num:
                    lowest_num = nums[lowest_chunk_index]
                    lowest_index = lowest_chunk_index
                    break

            mid = l + ((r - l) // 2)
            mid_num = nums[mid]

            if mid_num < lowest_num:
                lowest_num = mid_num
                lowest_index = mid

            if mid_num >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        print(lowest_index)

        if target >= nums[lowest_index] and target <= nums[-1]:
            l = lowest_index
            r = len(nums) - 1
        else:
            l = 0
            r = lowest_index - 1

        print(f'lowest_index: {lowest_index}, l: {l}, r: {r}')
        
        while l <= r:
            mid = l + ((r - l) // 2)
            mid_num = nums[mid]

            if target > mid_num:
                l = mid + 1
            elif target < mid_num:
                r = mid - 1
            else:
                return mid

        return -1
