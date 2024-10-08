from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        word_count = Counter(words)
        return [word for word, count in word_count.items() if count == 1]
