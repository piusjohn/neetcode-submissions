class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        previous = 0
        current = 0
        for c in sentences:
            
        
            current = len(c.split())
            if current > previous:
                previous = current
        return previous

        