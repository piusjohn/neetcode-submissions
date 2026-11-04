class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        result = []
        left = 0
        right = len(numbers) - 1
        sum = 0
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                result.append(left+1)
                result.append(right+1)
                return result
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1

