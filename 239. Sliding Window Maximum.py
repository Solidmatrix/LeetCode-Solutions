class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []:
            return []
        result = []
        array = nums[:k]
        array.sort()
        result.append(array[-1])
        for i in xrange(k, len(nums)):
            array[array.index(nums[i-k])] = nums[i]
            array.sort()
            result.append(array[-1])
        return result
        