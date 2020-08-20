
# @Title: 扫雷游戏 (Minesweeper)
# @Author: KivenC
# @Date: 2020-08-20 22:50:22
# @Runtime: 224 ms
# @Memory: 16.4 MB

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # # bfs
        # i, j = click
        # if board[i][j] == 'M':
        #     board[i][j] = 'X'
        #     return board
        # m, n = len(board), len(board[0])
        # delta = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        # queue = [click]
        # while queue:
        #     i, j = queue.pop()
        #     count = 0
        #     for delta_i, delta_j in delta:
        #         ii, jj = i + delta_i, j + delta_j
        #         if 0 <= ii < m and 0 <= jj < n:
        #             count += (board[ii][jj] == 'M')
        #     if count > 0:
        #         board[i][j] = str(count)
        #     else:
        #         board[i][j] = 'B'
        #         for delta_i, delta_j in delta:
        #             ii, jj = i + delta_i, j + delta_j
        #             # 当 count 为零时，将四周为 'E' 的格子加入队列
        #             if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == 'E':
        #                 queue.append([ii, jj])
        # return board

        # dfs
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        m, n = len(board), len(board[0])
        delta = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        def dfs(board, i, j):
            count = 0
            for delta_i, delta_j in delta:
                ii, jj = i + delta_i, j + delta_j
                if 0 <= ii < m and 0 <= jj < n:
                    count += (board[ii][jj] == 'M')
            if count > 0:
                board[i][j] = str(count)
            else:
                board[i][j] = 'B'
                for delta_i, delta_j in delta:
                    ii, jj = i + delta_i, j + delta_j
                    if 0 <= ii < m and 0 <= jj < n and board[ii][jj] == 'E':
                        dfs(board, ii, jj)
        dfs(board, i, j)
        return board

