class Solution(object):
    def firstMissingPositive(self, nums):
        ans = 1
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == ans:
                ans+=1
                i+=1
        return ans