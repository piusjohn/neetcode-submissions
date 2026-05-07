class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        # Quick exit if no flowers need to be planted
        if n == 0:
            return True
            
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                # Check neighbors or boundaries
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                right_empty = (i == length - 1) or (flowerbed[i+1] == 0)
                
                if left_empty and right_empty:
                    flowerbed[i] = 1 # Plant the flower
                    count += 1
                    
                    if count >= n:
                        return True
                        
        return count >= n
