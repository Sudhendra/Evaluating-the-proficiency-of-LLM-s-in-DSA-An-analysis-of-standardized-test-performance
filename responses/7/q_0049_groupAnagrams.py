from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            anagrams[key].append(word)
        
        return list(anagrams.values())
