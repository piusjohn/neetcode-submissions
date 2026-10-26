from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_group = defaultdict(list)
        for string in strs:
            sorted_key = "".join(sorted(string))
            anagrams_group[sorted_key].append(string)
        return list(anagrams_group.values())