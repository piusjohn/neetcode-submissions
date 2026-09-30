class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        operation = []
        targetindex = 0
        for num in range(1, n +1):
            if num in target:
                operation.append("Push")
                targetindex += 1
            else:
                operation.append("Push")
                operation.append("Pop")
            if targetindex == len(target):
                break
        return operation