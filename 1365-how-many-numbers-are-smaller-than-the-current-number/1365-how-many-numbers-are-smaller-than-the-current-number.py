class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = []
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    count+=1
                 
            result.append(count)
            count = 0
    
        return result
