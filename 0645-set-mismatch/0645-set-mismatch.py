class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nlist = nums
        #fixedlist = []
        missing = 0
        duplicate = 0
        final = 0
        current = final
        for i in range(1, len(nums)+1):
             #fixedlist.append(i)
            if i not in nums:
                missing = i
            if i in nlist:
                nlist.remove(i)
        nlist.append(missing)
        return nlist