class Solution:
  def plusOne(self, digits: list[int]) -> list[int]:
    n = len(digits)
    # Loop from the last digit back to the first
    for i in range(n - 1, -1, -1):
      digits[i] += 1
      digits[i] %= 10
      if digits[i] != 0:
        return digits

    # If all digits were 9 (e.g., [9, 9] -> [1, 0, 0])
    return [1] + digits
