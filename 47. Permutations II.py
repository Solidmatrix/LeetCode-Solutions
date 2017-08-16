class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 0:
            return result
        nums.sort()
        while True:
            result.append([i for i in nums])
            for i in xrange(len(nums)-2, -1, -1):
                if nums[i] < nums[i+1]:
                    break
            else:
                return result
            for j in xrange(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    break
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            
            reverse = nums[i+1: ]
            reverse.reverse()
            nums[i+1: ] = reverse
            