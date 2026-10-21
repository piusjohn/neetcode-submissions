class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
       k = len(set(nums))
       unique_num = sorted(set(nums))
       for i in range(k):
        nums[i] = unique_num[i]
       return k
       