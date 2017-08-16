class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        pos = i = 0
        result = [str(nums[0])]
        for i in xrange(1, len(nums)):
            if nums[i] - nums[pos] == i - pos:
                continue
            else:
                if i > pos + 1:
                    result[len(result)-1] += "->" + str(nums[i-1])
                result.append(str(nums[i]))
                pos = i
        if nums[i] - nums[pos] == i - pos and i >= pos + 1:
            result[len(result)-1] += "->" + str(nums[i])
        return result