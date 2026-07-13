class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False

        # l, r = 0, len(matrix) * len(matrix[0]) - 1
        
        # while l <= r:
        #     mid = l + ((r - l) // 2)

        #     row = mid // len(matrix)
        #     col = mid % len(matrix[0])
            
        #     mid_num = matrix[row][col]

        #     if mid_num < target:
        #         l = mid + 1
        #     elif mid_num > target:
        #         r = mid - 1
        #     else:
        #         return True

        # return False
        