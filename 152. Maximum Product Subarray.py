class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxn = - sys.maxint - 1
        count = 0
        left = 0
        for i in xrange(len(nums)):
            if nums[i] < 0:
                count += 1
            elif nums[i] == 0:
                maxn = max(maxn, self.product(nums, left, i, count))
                left = i + 1
                count = 0
        if left == 0:
            maxn = self.product(nums, 0, len(nums), count)
        else:
            maxn = max(maxn, 0, self.product(nums, left, len(nums), count))
        return maxn
                
    def product(self, nums, left, right, count):
        if left == right:
            return 0
        if count % 2 == 0:
            m = 1
            for i in xrange(left, right):
                m *= nums[i]
            return m
        elif count == 1:
            if right - left == 1:
                return nums[left]
            m1 = m2 = 1
            while nums[left] > 0:
                m1 *= nums[left]
                left += 1
            for i in xrange(left+1, right):
                m2 *= nums[i]
            return max(m1, m2)
        else:
            m1 = m2 = m3 = 1
            while nums[left] > 0:
                m1 *= nums[left]
                left += 1
            m1 *= nums[left]
            right -= 1
            while nums[right] > 0:
                m3 *= nums[right]
                right -= 1
            m3 *= nums[right]
            for i in xrange(left+1, right):
                m2 *= nums[i]
            return max(m1*m2, m2*m3)
                    
                    
                    
                    
                    
            
                