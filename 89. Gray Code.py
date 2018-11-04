class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

    def grayCode(self, n):
        if n == 0:
            return [0]
        
        code = self.grayCode(n-1)
        result = []
        result.extend(code)
        code.reverse()
        add = pow(2, n-1)
        code = map(lambda x: x + add, code)
        result.extend(code)
        return result
        
        