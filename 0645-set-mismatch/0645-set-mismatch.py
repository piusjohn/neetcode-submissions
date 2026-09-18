class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nlist = nums
        missing = 0
        for i in range(1, len(nums)+1):
             #fixedlist.append(i)
            if i not in nums:
                missing = i
            if i in nlist:
                nlist.remove(i)
        nlist.append(missing)
        return nlist