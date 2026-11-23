class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for item in nums:
            if item != val:
                nums[k] = item
                k += 1
        return