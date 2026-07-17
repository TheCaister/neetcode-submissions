# for every mid, we'll either be in the left or right portion. let's say if left < mid, we're in the left. and vice versa
# I think there's like 4 permutations on where to start looking
# if left - if target bigger, ALWAYS look to the right. if target smaller, if it's bigger than left, look to the left. otherwise look to the right
# if right portion - if target bigger, if target > right, we look to the left. otherwise, look to the right
# if right portion - if target smaller - ALWAYS look to the left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1            

        while l <= r:
            mid = l + ((r - l) // 2)
            mid_num = nums[mid]
            is_left = True if nums[l] <= mid_num else False

            print(mid)
            print(mid_num)
            print(is_left)

            if mid_num == target:
                return mid

            if is_left:
                if target > mid_num:
                    l = mid + 1
                else:
                    if target >= nums[l]:
                        r = mid - 1
                    else:
                        l = mid + 1
            else:
                if target < mid_num:
                    r = mid - 1
                else:
                    if target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1

            print(f'final l: {l}, final r: {r}')

        return -1