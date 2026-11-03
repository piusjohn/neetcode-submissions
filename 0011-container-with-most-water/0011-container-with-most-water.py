class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        previous = 0
        left = 0
        right = n -1
        while left < right:
            # current = 0
            width = right - left
            water_height = 0
            if height[left] < height[right]:
                water_height = height[left]
            else:
                water_height = height[right]

            current = width * water_height
            if previous < current:
                previous = current

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return previous

