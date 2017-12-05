class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        sequence = [0] * (n + 1)
        sequence[0] = sequence[1] = 1
        for i in xrange(2, n + 1):
            for j in xrange(i/2):
                sequence[i] += sequence[j] * sequence[i-1-j]
            sequence[i] *= 2
            if i % 2 == 1:
                sequence[i] += sequence[i/2] ** 2
        return sequence[-1]