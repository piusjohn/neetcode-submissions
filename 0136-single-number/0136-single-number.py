class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        seen = set()
        duplicates = set()
        for num in nums:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        not_duplicate = seen - duplicates
        return not_duplicate.pop()