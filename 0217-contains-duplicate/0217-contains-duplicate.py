class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = hashmap.get(num, 0) +1
        for key in hashmap:
            if hashmap[key] >= 2:
                return True
        
        return False