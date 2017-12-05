class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            dict1 = {}
            dict2 = {}
            for j in xrange(9):
                if board[i][j] != '.' and board[i][j] in dict1:
                    return False
                dict1[board[i][j]] = 1
                if board[j][i] != '.' and board[j][i] in dict2:
                    return False
                dict2[board[j][i]] = 1
        
        for i in xrange(9):
            dict1 = {}
            for j in xrange(3):
                for k in xrange(3):
                    x = i/3*3 + j
                    y = i%3*3 + k
                    if board[x][y] != '.' and board[x][y] in dict1:
                        return False
                    dict1[board[x][y]] = 1
        return True