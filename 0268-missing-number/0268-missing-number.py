class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing = 0
        newlist = []
        for i in range(len(nums)+1):
            if i in nums:
                newlist = i
            else:
                missing = i
        return missing
