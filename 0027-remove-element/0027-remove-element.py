class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for item in nums[:]:
            if item == val:
                nums.remove(val)

        return len(nums)