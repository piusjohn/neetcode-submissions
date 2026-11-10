class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        nums = [int(d) for d in str(num)]
        for val in nums:
            if val != 0 and num % val == 0:
                count += 1
        return count