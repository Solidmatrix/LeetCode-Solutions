class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = a = n/5
        while a >= 5:
            a /= 5
            result += a
        return result