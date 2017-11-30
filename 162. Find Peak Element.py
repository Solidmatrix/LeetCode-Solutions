class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)-1):
            if nums[i+1] < nums[i]:
                return i
        return len(nums)-1