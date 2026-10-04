class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        result = 0
        for num in hours:
            if num >= target:
                result += 1
        return result