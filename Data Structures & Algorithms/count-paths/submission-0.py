# the bottom row, all 1. the right col, all 1
# for any given cell, it's left + bottom path
# we can build from the bottom up, until we reach 0, 0
# we can build up a whole dp grid, but we should only need the last row for our calculations
# start from second last row, starting from last/second last column. initialise prev col to 1. start from second last col.
# cur cell is prev col + last row at corresponding index. update prev col and also the corresponding in last row

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lastRow = [1] * (n - 1)
        lastCol = 1

        for i in range(m - 2, -1, -1):
            lastCol = 1

            for j in range(n - 2, -1, -1):
                cur_res = lastCol + lastRow[j]
                lastCol = lastRow[j] = cur_res
            
            # print(lastRow)

        return lastCol