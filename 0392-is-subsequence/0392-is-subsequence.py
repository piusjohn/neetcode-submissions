class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer = 0
        if len(s) == 0:
            return True
        for i, char in enumerate(t):
            if char == s[pointer]:
                pointer += 1
            if pointer == len(s):
               return True
                           
        return False
        
