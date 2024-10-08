from collections import Counter

class Solution:
    

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()
        
        count = Counter(words1 + words2)
        
        return [word for word in count if count[word] == 1]
