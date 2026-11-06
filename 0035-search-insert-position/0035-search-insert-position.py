class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums.append(target)
        new = sorted(set(nums))
        for i in range(len(new)):
            if new[i] == target:
                return i

