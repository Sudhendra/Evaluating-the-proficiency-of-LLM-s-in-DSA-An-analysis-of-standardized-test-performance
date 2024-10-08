from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_count = Counter(s1.split()) + Counter(s2.split())
        return [word for word, count in words_count.items() if count == 1]
