class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums:
            n = abs(i)-1
            if nums[n] > 0:
                nums[n] = -nums[n]
        for i in xrange(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result