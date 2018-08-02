class Solution(object):
        
    def combineOnce(self, start, n, k):
        print(start, n, k)
        result = []
        if k == 1:
            for s in range(start, start + n):
                result.append([s])
                
        else:
            for s in range(1, n - k + 2):
                for t in self.combineOnce(start + s, n - s, k - 1):
                    t.insert(0, start + s - 1)
                    result.append(t)
        return result
        
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.combineOnce(1, n, k)
        
    
            
        