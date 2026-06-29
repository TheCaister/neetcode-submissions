# brute force is cubic time complexity
# or, we can simplify it a bit by scanning for each value, and for each val find the 2sum of the rest of the values to reduce it to n^2
# here, for each element n, we do an o(n) 2sum search. this ONLY works if the array is sorted, which takes o n log n time for good algorithms
# and usually, needs o(n) for some sorting algorithms, but still collapses to n^2
# to be honest, is there a better way? apparently, this is an industry wide question
# brute force - check everything
# better way, if we can get the complements of each one in better time complexity, then that would be cool
# this can be achieved thorugh sorting, where we can definitely move pointers towards the goal
# the fact that we don't have to return indices is also nice
# another potential way, same time complexity would be to do n^2 combinations, and figure out a constant way to get the last element


# so
# sort the list
# for each element x, target is x + y + z = 0, or y + z. current target is -x
# do an inner loop to find the l and r and therefore y + z
# for each iteration, if l + r = -x, we add it to the list, then move the pointers. we need to rermember to move past duplicates as well
# if l + r is too small, we gotta go bigger, so we move l up. opposite case for r
#

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                cur_result = v + nums[l] + nums[r]

                if cur_result < 0:
                    l += 1
                elif cur_result > 0:
                    r -= 1
                else:
                    result.append([v, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

        return result