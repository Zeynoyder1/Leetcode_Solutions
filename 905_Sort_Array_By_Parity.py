class Solution(object):
    def sortArrayByParity(self, nums):
        
        for i in range(len(nums)):
            if nums[i]%2 == 0:
               temp = nums[i]
               nums.pop(i)
               nums.insert(0,temp) 
               
   
        return nums