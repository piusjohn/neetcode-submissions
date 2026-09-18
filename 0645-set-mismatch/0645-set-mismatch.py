class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        actualSum = sum(nums)
        uniqueSum = sum(set(nums))
        expectedSum = n * (n+1) // 2
        duplicate = actualSum - uniqueSum
        missing = expectedSum - uniqueSum

        return [duplicate, missing]