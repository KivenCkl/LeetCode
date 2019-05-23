
# @Title: 有效的数独 (Valid Sudoku)
# @Author: KivenC
# @Date: 2019-02-22 11:19:46
# @Runtime: 68 ms
# @Memory: 6.5 MB

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_ind = (i // 3) * 3 + j // 3
                    
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_ind][num] = boxes[box_ind].get(num, 0) + 1
                    
                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_ind][num] > 1:
                        return False
        return True
