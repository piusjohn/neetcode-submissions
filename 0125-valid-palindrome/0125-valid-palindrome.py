class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_S = "".join(c.lower() for c in s if c.isalnum())
        if new_S == "".join(reversed(new_S)):
            return True
        else:
            return False