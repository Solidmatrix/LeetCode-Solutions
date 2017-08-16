class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in xrange(2 ** len(nums)):
            binary = bin(i)
            tmp = []
            for j in xrange(2, len(binary)):
                if binary[j] == '1':
                    tmp.append(nums[len(binary)-1-j])
            result.append(tmp)
        return result