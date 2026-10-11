class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        squared_nums = []
        for i in range(len(nums)):
            if n % (i+1) == 0:
                squared_nums.append(nums[i])
        return sum(x**2 for x in squared_nums)