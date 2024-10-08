from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = Counter(words[0])
        
        for word in words[1:]:
            common_chars &= Counter(word)
        
        return list(common_chars.elements())
