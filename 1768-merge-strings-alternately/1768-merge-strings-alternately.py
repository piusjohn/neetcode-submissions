class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        temp = []
        result = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                temp.append(word1[i])
            if i < len(word2):
                temp.append(word2[i])
        result = "".join(temp)
        return result
            