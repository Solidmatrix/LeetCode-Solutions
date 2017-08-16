class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        minn = sys.maxint
        maxn = -sys.maxint-1
        for i in xrange(len(nums)):
            minn = min(minn, nums[i])
            maxn = max(maxn, nums[i])
        length = (maxn - minn) * 1.0 / (len(nums)-1)
        if length == 0:
            return 0
        cnt = int((maxn - minn) / length + 1)
        minb = [sys.maxint] * cnt
        maxb = [-sys.maxint-1] * cnt
        for i in xrange(len(nums)):
            id = int((nums[i] - minn) / length)
            minb[id] = min(minb[id], nums[i])
            maxb[id] = max(maxb[id], nums[i])
            res = 0
            premax = maxb[0]
        for i in xrange(1, cnt):
            if minb[i] != sys.maxint:
                res = max(res, minb[i] - premax)
                premax = maxb[i]
        return res
    
    
    