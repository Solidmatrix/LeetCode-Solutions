class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == '' and (p == '' or p == '*'):
            return True
        if s == '' or p == '':
            return False
        matrix = [([False] * len(s)) for i in xrange(len(p))]
        
        if p[0] == '?' or p[0] == s[0]:
            matrix[0][0] = count =  True
        else:
            count = False
        if p[0] == '*':
            for j in xrange(len(s)):
                matrix[0][j] = True
        if not matrix[0][0]:
            return False
        
        for i in xrange(1, len(p)):
            if (p[i] == '?' or p[i] == s[0]) and not count and matrix[i-1][0]:
                matrix[i][0] = count = True
            elif p[i] == '*' and matrix[i-1][0]:
                matrix[i][0] = True
                
            for j in xrange(1, len(s)):
                if p[i] == '*':
                    matrix[i][j] = matrix[i-1][j] or matrix[i][j-1]
                elif p[i] == '?' or p[i] == s[j]:
                    matrix[i][j] = matrix[i-1][j-1]
            
        return matrix[len(p)-1][len(s)-1]
            
                
        