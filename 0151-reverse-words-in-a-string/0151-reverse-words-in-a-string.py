class Solution:
    def reverseWords(self, s: str) -> str:
        tresult = []
        result = ""
        temp = s.split()
        for word in reversed(temp):
            tresult.append(word)
        result = " ".join(tresult)
        return result