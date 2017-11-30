class Solution(object):
    d = {0:0}
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.d:
            return self.d[n]
        minimum = sys.maxint
        i = 1
        while i*i <= n:
            minimum = min(minimum, 1 + self.numSquares(n - i*i))
            i += 1
        self.d[n] = minimum
        return minimum