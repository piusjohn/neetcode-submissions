class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current = 0
        max = current
        for num in nums:
            if num == 1:
                current += 1
            elif num != 1:
                current = 0
            if max < current:
                max = current
        return max
