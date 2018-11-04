class Solution(object):
    def getFactorial(self, n):
        if n == 0:
            return 1
        return n * self.getFactorial(n-1)
    
    def getOnePermutation(self, n, k):
        if n == 0:
            return
        scale = self.getFactorial(n-1)
        order = k / scale
        self.result += str(self.digit[order])
        self.digit.remove(self.digit[order])
        self.getOnePermutation(n-1, k % scale)
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.result = ""
        self.digit = range(1, n+1)
        self.getOnePermutation(n, k-1)
        return self.result
            
        
        