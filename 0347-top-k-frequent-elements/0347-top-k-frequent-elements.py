class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap = {}
        result = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        def findhighest(hash: dict, k: int) -> list:
            result = []
            
            for i in range(k):
                max = 0
                highest_key = None
                for key, value in hash.items():
                    if value > max:
                        max = value
                        highest_key = key
                result.append(highest_key)
                hash[highest_key] = 0
            return result
        return findhighest(hashmap, k)
                
                
                
            