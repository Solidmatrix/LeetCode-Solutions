class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos1 = len(nums) - 2
        pos2 = len(nums) - 1
        while pos1 >= 0:
            if nums[pos1] < nums[pos1+1]:
                break
            pos1 -= 1
        else:
            nums.reverse()
            return
        
        while pos2 > pos1:
            if nums[pos2] > nums[pos1]:
                break
            pos2 -= 1
        
        tmp = nums[pos2]
        nums[pos2] = nums[pos1]
        nums[pos1] = tmp
        
        reverse = nums[pos1+1: len(nums)]
        reverse.reverse()
        nums[pos1+1: len(nums)] = reverse