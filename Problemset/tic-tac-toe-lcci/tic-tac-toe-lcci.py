
# @Title: 井字游戏 (Tic-Tac-Toe LCCI)
# @Author: KivenC
# @Date: 2020-07-09 16:23:47
# @Runtime: 56 ms
# @Memory: 13.6 MB

class Solution:
    def tictactoe(self, board: List[str]) -> str:
        n = len(board)
        mapper = {'X': 1, 'O': -1, ' ': 0}
        flag_null = False
        sum_diag_left, sum_diag_right = 0, 0
        sum_row_list = [0] * n
        sum_col_list = [0] * n
        for i in range(n):
            for j in range(n):
                val = mapper[board[i][j]]
                if not flag_null and not val:
                    flag_null = True
                if i == j:
                    sum_diag_left += val
                if i + j == n - 1:
                    sum_diag_right += val
                sum_row_list[i] += val
                sum_col_list[j] += val
        if sum_diag_left == n or sum_diag_right == n:
            return 'X'
        elif sum_diag_left == -n or sum_diag_right == -n:
            return 'O'
        for i in range(n):
            if sum_row_list[i] == n or sum_col_list[i] == n:
                return 'X'
            elif sum_row_list[i] == -n or sum_col_list[i] == -n:
                return 'O'
        if flag_null:
            return "Pending"
        else:
            return "Draw"
