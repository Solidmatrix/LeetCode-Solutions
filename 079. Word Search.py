class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[False]*len(board[0]) for i in xrange(len(board))]
        s = word[0]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == s and self.dfs(board, word, visited, i, j, 1):
                    return True
        return False
        
    def dfs(self, board, word, visited, i, j, pos):
        if pos == len(word):
            return True
        s = word[pos]
        visited[i][j] = True
        if i > 0 and board[i-1][j] == s and not visited[i-1][j]:
            if self.dfs(board, word, visited, i-1, j, pos+1):
                return True
        if i < len(board)-1 and board[i+1][j] == s and not visited[i+1][j]:
            if self.dfs(board, word, visited, i+1, j, pos+1):
                return True
        if j > 0 and board[i][j-1] == s and not visited[i][j-1]:
            if self.dfs(board, word, visited, i, j-1, pos+1):
                return True
        if j < len(board[0])-1 and board[i][j+1] == s and not visited[i][j+1]:
            if self.dfs(board, word, visited, i, j+1, pos+1):
                return True
        visited[i][j] = False
        return False
    