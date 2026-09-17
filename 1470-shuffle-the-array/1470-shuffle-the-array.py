class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        firsthalf = nums[:n]
        secondhalf = nums[n:]
        for i in range(n):
            result.append(firsthalf[i])
            result.append(secondhalf[i])
        return result
