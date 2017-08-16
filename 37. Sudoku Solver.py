class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
        
    def solve(self, board, x = 0):
        for i in xrange(x, 9):
            for j in xrange(9):
                if board[i][j] == '.':
                    for k in xrange(1, 10):
                        if self.isValid(board, i, j, str(k)):
                            board[i][j] = str(k)
                            result = self.solve(board, i)
                            if len(result):
                                return result
                    board[i][j] = '.'
                    return []
        return board
    
    def isValid(self, board, i, j, c):
        for k in xrange(9):
            x = i/3*3 + k/3
            y = j/3*3 + k%3
            if board[i][k] == c or board[k][j] == c or board[x][y] == c:
                return False
        return True