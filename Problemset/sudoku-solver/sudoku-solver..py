
# @Title: 解数独 (Sudoku Solver)
# @Author: KivenC
# @Date: 2019-02-24 22:34:30
# @Runtime: 80 ms
# @Memory: 6.6 MB

class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        def Boardcyc(rowaray,colarray,cellarray,dotpos,k):
            if k == len(dotpos):
                return True
            i,j = dotpos[k]
            indexij = i//3*3 + j//3
            res = rowarray[i]&colarray[j]&cellarray[indexij]
            if len(res) == 0:
                return False
            for one in res:
                rowarray[i].remove(one)
                colarray[j].remove(one)
                cellarray[indexij].remove(one)
                board[i][j] = one
                if Boardcyc(rowarray,colarray,cellarray,dotpos,k+1):
                    return True
                else:
                    rowarray[i].add(one)
                    colarray[j].add(one)
                    cellarray[indexij].add(one)
                    board[i][j] = '.'
            return False
        onearray = set(map(str,[1,2,3,4,5,6,7,8,9]))
        rowarray = [onearray.copy() for _ in range(9)]
        colarray = [onearray.copy() for _ in range(9)]
        cellarray = [onearray.copy() for _ in range(9)]
        dotpos = []
        for i in range(9):
            indexi = i//3*3
            for j in range(9):
                if board[i][j] == '.':
                    dotpos.append([i,j])
                else:
                    rowarray[i].remove(board[i][j])
                    colarray[j].remove(board[i][j])
                    cellarray[indexi+j//3].remove(board[i][j])
        if len(dotpos) == 0:
            return True
        #print(rowarray)
        #print(colarray)
        #print(cellarray)
        Boardcyc(rowarray,colarray,cellarray,dotpos,0)
