class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        missing = []
        num_set = set(nums)
        for i in range(1, len(nums)+1):
            if i not in num_set:
                missing.append(i)
        return missing
             

        