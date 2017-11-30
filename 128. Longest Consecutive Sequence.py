class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = {}.fromkeys(nums).keys()
        dict = [{}, {}]
        for i in nums:
            if i+1 in dict[0] and i-1 in dict[1]:
                dict[0][dict[1][i-1]] = dict[0][i+1]
                dict[1][dict[0][i+1]] = dict[1][i-1]
                del dict[0][i+1]
                del dict[1][i-1]
            elif i+1 in dict[0]:
                dict[0][i] = dict[0][i+1]
                dict[1][dict[0][i]] = i
                del dict[0][i+1]
            elif i-1 in dict[1]:
                dict[1][i] = dict[1][i-1]
                dict[0][dict[1][i]] = i
                del dict[1][i-1]
            else:
                dict[0][i] = i
                dict[1][i] = i
        maxn = -1-sys.maxint
        for i in dict[0]:
            maxn = max(maxn, dict[0][i] - i)
        return maxn + 1           