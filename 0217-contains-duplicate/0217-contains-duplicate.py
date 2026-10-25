class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n_set = len(set(nums))
        n = len(nums)
        if n != n_set:
            return True
        else:
            return False

