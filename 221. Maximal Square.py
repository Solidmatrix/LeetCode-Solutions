class Solution_1(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        line = [0] * n
        maximum = 0
        for i in xrange(m):
            for j in xrange(n):
                line[j] = line[j] + 1 if matrix[i][j] == '1' else 0
            j = 0
            while maximum < n - j:
                if maximum < line[j]:
                    length = line[j]
                    k = 1
                    pos = j
                    while k < length:
                        if line[j+k] < length:
                            if line[j+k] > k + 1 and maximum < line[j+k]:
                                pos = j + k
                                length = line[j+k]
                            else:
                                maximum = max(maximum, line[j+k])
                                j = j + k
                                break
                        elif k == length:
                            pos = j + k
                        k += 1
                    else:
                        maximum = length
                        j = pos
                j += 1
        return maximum * maximum
    

class Solution_2(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        line = [0] * n
        maximum = 0
        for j in xrange(n):
            line[j] = 1 if matrix[0][j] == '1' else 0
            maximum = max(maximum, line[j])
        for i in xrange(1, m):
            prev = line[0]
            line[0] = 1 if matrix[i][0] == '1' else 0
            maximum = max(maximum, line[0])
            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    tmp = line[j]
                    line[j] = min(prev, line[j-1], tmp) + 1
                    maximum = max(maximum, line[j])
                    prev = tmp
                else:
                    line[j] = 0
        return maximum * maximum