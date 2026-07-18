# brute force, new list, get the middle element
# is there a way we can utilise the length somehow?
# we could have a 2 pointer approach, go up until we reach length.half, then take the mean of the 2 numbers
# if 1 list is bigger than the other, then we can very easily get the median, since we subtract the length of the other
# the tricky case arrives when the 2 lists overlap

# [1, 2, 5, 7, 8]
# [2, 3, 5, 6]
# [1, 2, 2, 3, 5, 5, 6, 7, 8]

# median = 5, 4 elements on each
# arr1 = 5, 3. arr2 = 1, 1
# 5 > 2, update arr1 boundary to 1
# so arr1 = 1, 1. arr2 = 5, 3
# 5 > 2, update arr1 boundary to 1, 1
# arr1 = 2, 2. arr2 = 3
# none of the above conditions pass. this is the median for certain.
# now, to calculate the actual median. it'll be the lower of arr1[i + 1] and arr2[i + 1] if there's an odd num of numbers
# if it's even amount of num, it'll be the mean of the highest of arr1[i] or arr2[i], and the lowest of arr1[i + 1] and arr2[i + 1]

# the median is where the amount to the left and right is total / 2. each left/right is composed of left arr1 + left arr2, same for right
# let's binary search on one of the lists, and get corresponding left on other array
# for each step, let's check if we're at the correct median
# arr1[i] can't be > arr2[i + 1]
# same for arr2, arr2[i] can't be > arr1[i + 1]
# let's say we're binary searching arr1. if arr[i] > arr2[i + 1], we gotta look to the left. we've taken too much of arr1
# same for arr2, is arr2[i] > arr1[i + 1], we took too little of arr1, let's look to the right
# also, if mid of arr1 is over len / 2, we know we took too much of arr1 for sure, let's look to the left
# similarly, if corresponding index in arr2 is too big, we gotta take more of arr1, so let's look to the right



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # total_len = len(nums1) + len(nums2)
        # l, r = 0, len(nums1) - 1

        # while l <= r:
        #     mid = l + ((r - l) // 2)
        #     print(mid)
        #     nums1_len = mid + 1
        #     nums2_len = (total_len // 2) - nums1_len

        #     num1_left = nums

        #     if nums2_len > 0 and nums2[nums2_len - 1] > nums1[nums1_len]:
        #         l = mid + 1
        #     elif nums1[mid] > nums2[nums2_len]:
        #         r = mid - 1
        #     else:
        #         if total_len % 2 == 0:
        #             return (max(nums1[nums1_len - 1], nums2[nums2_len - 1]) + min(nums1[nums1_len], nums2[nums2_len])) / 2
        #         else:
        #             return min(nums1[nums1_len], nums2[nums2_len])

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
                
