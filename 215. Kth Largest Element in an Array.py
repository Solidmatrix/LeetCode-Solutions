class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        k = len(nums) - k
        mid = self.qsort(nums, left, right)
        while mid != k:
            if mid < k:
                left = mid + 1
            else:
                right = mid - 1
            mid = self.qsort(nums, left, right)
        return nums[k]
        
    def qsort(self, a, start, end):
        if start >= end:
            return start
        i, j = start, end
        self.median(a, start, end)  
        tmp = a[start]  
        while True:  
            while a[j] > tmp and i < j:  
                j -= 1  
            if i < j:  
                a[i] = a[j]  
                i += 1
            while a[i] < tmp and i < j:  
                i += 1
            if i < j:
                a[j] = a[i]
                j -= 1
            else:  
                break  
        a[i] = tmp
        return i

    def median(self, a, start, end):  
        center = (start + end) / 2  
        if a[start] > a[center]:  
            a[start], a[center] = a[center], a[start]  
        if a[start] > a[end]:  
            a[start], a[end] = a[end], a[start]  
        if a[center] > a[end]:  
            a[center], a[end] = a[end], a[center]  
        a[start], a[center] = a[center], a[start]
        
        