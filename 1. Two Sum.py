class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in xrange(len(nums)):
            dict[nums[i]] = i
        for i in xrange(len(nums)):
            diff = target - nums[i]
            if diff in dict and i != dict[diff]:
                return [i, dict[diff]]