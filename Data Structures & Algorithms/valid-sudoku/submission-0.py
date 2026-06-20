# we can do it brute force, ngl dunno if there's another way
# all 9 horizontals and verticals = 18
# all 3*3 grids - 9
# so 27 things to check altogether

# maybe for all verticals and horizontals, just keep adding to set
# before adding to set, if exists, return false

# for 3*3, it's a mini thing, where we can scan like a snake
# and do the same thing

# go through all blocks 3 times basically
# for each cell, we do constant inserts, lookups
# so o(n), where n is number of cells or o(x * y)
# const memory, we only need up to 9 elements in the set

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tmp_set = set()
        
        # rows
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur_cell = board[i][j]

                if cur_cell in tmp_set:
                    return False
                elif cur_cell != '.':
                    tmp_set.add(cur_cell)
            
            tmp_set = set()

        # columns
        for j in range(len(board[0])):
            for i in range(len(board)):
                cur_cell = board[i][j]
            
                if cur_cell in tmp_set:
                    return False
                elif cur_cell != '.':
                    tmp_set.add(cur_cell)
            
            tmp_set = set()

        # 3 x 3s
        for x in range(0, len(board), 3):
            for y in range(0, len(board[0]), 3):
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        cur_cell = board[i][j]
            
                        if cur_cell in tmp_set:
                            return False
                        elif cur_cell != '.':
                            tmp_set.add(cur_cell)
                tmp_set = set()


        return True

# 
        