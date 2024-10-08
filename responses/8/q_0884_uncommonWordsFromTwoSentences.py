from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()
        
        counter = Counter(words1) + Counter(words2)
        
        return [word for word, count in counter.items() if count == 1]
