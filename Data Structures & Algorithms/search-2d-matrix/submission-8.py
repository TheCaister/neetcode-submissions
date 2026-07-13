class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix) * len(matrix[0]) - 1
        
        while l <= r:
            mid = l + ((r - l) // 2)

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            
            mid_num = matrix[row][col]

            if mid_num < target:
                l = mid + 1
            elif mid_num > target:
                r = mid - 1
            else:
                return True

        return False
        