class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)-1
        
        while low <= high:
            m = low + (high - low)/2

            if nums[m] == target:
                return m
            if nums[m] < target:
                low = m + 1
            if nums[m] > target:
                high = m -1
        return -1