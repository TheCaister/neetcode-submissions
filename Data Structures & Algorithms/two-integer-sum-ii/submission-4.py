# sorted, exhaustive search is quadratic
# however, can we use the fact they're sorted to our advantage?
# if we take random 2 indexes, if the sum is too large, we could either move the left or right down
# similarly, if sum too small, we move either right or left up, we'd never do it the other way
# what if we have pointers on the outer sides? this way, we can more definitely move left and right in one direction
# move left up only if sum is too small, and same for right.
# eventually, we'll reach correct conclusion



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]