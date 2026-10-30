class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array to easily handle duplicates and use two pointers
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            # If the current number is greater than 0, the remaining numbers 
            # will also be greater than 0, so no triplet can sum to 0.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Initialize two pointers
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Sum is too small, move left pointer rightward
                elif total > 0:
                    right -= 1 # Sum is too large, move right pointer leftward
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                     
                    right -= 1
                    
        return res
