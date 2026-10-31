class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        nums.sort()  # Sorting helps easily prevent duplicate permutations like [a, b, c] and [b, a, c]
        
        for i in range(len(nums) - 2):
            if nums[i] > 0: 
                break  # If the first number is positive, the rest cannot sum to 0
                
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                
                if complement in seen:
                    # Storing as a tuple inside a set automatically eliminates duplicates
                    res.add((nums[i], complement, nums[j]))
                
                seen.add(nums[j])
                
        return [list(triplet) for triplet in res]
