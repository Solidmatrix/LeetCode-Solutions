class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if buildings == []: return []
        def compare(x, y):
            if x[2] < y[2]: return 1
            elif x[2] > y[2]: return -1
            else: return 0
        buildings.sort(compare)
        pos = [[0, sys.maxint]]
        result = []
        p = 1
        
        for [x, y, z] in buildings:
            for i in xrange(p):
                if x <= pos[i][0]: break
            else: i = p
            i -= 1
            for j in xrange(max(0, i), p):
                if y < pos[j][1]: break
            else: y = p
            
            if i == j:
                result.append([x, z])
                pos.insert(i+1, [y, pos[i][1]])
                p += 1
                pos[i][1] = x
                continue
            if i != -1 and x < pos[i][1]:
                result.append([x, z])
                pos[i][1] = x
            if j != p and y > pos[j][0]:
                result.append([pos[j][0], z])
                pos[j][0] = y
            for k in xrange(i+1, j):
                result.append([pos[k][0], z])
            pos = pos[:i+1] + pos[j:]
            p -= j-i-1
        for [x, y] in pos:
            result.append([x, 0])
        result.sort()
        while result[0][1] == 0:
            del result[0]
        i = 0
        while i < len(result)-1:
            if result[i][1] == result[i+1][1]:
                del result[i+1]
            else:
                i += 1
        return result
                
                
                
                
                
                