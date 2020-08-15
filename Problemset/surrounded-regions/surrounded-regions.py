
# @Title: 被围绕的区域 (Surrounded Regions)
# @Author: KivenC
# @Date: 2020-08-11 17:36:02
# @Runtime: 48 ms
# @Memory: 15.2 MB

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # # bfs
        # stack = []
        # if not board or not board[0]:
        #     return
        # m, n = len(board), len(board[0])
        # for i in range(m):
        #     for j in [0, n-1]:
        #         if board[i][j] == 'O':
        #             stack.append([i, j])
        # for j in range(1, n-1):
        #     for i in [0, m-1]:
        #         if board[i][j] == 'O':
        #             stack.append([i, j])
        # while stack:
        #     i, j = stack.pop()
        #     board[i][j] = 'A'
        #     for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        #         if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
        #             stack.append([x, y])
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'A':
        #             board[i][j] = 'O'
        #         elif board[i][j] == 'O':
        #             board[i][j] = 'X'

        # dfs
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != 'O':
                return
            board[i][j] = 'A'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(1, n-1):
            dfs(0, j)
            dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

